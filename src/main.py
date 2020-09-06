import pytest
from typing import NewType, Set   # Cheat sheet in docs: https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from pathlib import Path
import json

# Domain Types:
DNA = NewType("DNA", str)
RNA = NewType("RNA", str)
Peptide = NewType("Peptide", str)


# Source Code:

def get_antisense(seq: DNA) -> DNA:
  matches = {"C": "G", "G": "C", "A": "T", "T": "A"}
  antisense = "".join(matches[nt] for nt in seq[::-1])
  return DNA(antisense)


def transcribe(seq: DNA) -> RNA:
  matches = {"C": "G", "G": "C", "A": "U", "T": "A"}
  antisense = "".join(matches[nt] for nt in seq[::-1])
  return RNA(antisense)


def get_peptide(codon: str) -> str:
  pep3 = json.loads(Path("data/codons.json").read_text())[codon]
  pep1 = json.loads(Path("data/peptides.json").read_text())[pep3.lower()]
  return pep1


def translate(rna: RNA) -> Set[Peptide]:
  peptides = set()
  for seq in rna[:], rna[1:], rna[2:]:
    nts = iter(seq)
    codons = ["".join(nts) for nts in zip(nts, nts, nts)]
    if codons:
      assert all(len(codon) == 3 for codon in codons)
      protein = "".join(get_peptide(codon) for codon in codons)
      assert protein
      if "M" in protein:
        protein = protein[protein.index("M"):]
        peptides.add(Peptide(protein))
  return peptides


# Tests:
cases = [
  ("ATG", "CAT"),
  ("TTGC", "GCAA"),
  ("GGCTAAAGTCGGC", "GCCGACTTTAGCC"),
]
@pytest.mark.parametrize(("dna1", "dna2"), cases)
def test_dna_antisense_detected(dna1, dna2):
  assert get_antisense(DNA(dna1)) == DNA(dna2)


cases = [
  ("ATG", "CAU"),
  ("TTATGCATC", "GAUGCAUAA"),
]
@pytest.mark.parametrize(("dna", "rna"), cases)
def test_dna_transcription(dna, rna):
  assert transcribe(DNA(dna)) == RNA(rna)


cases = [
  ("AUG", {"M"}),  # type: ignore
  ("AUGCCC", {"MP"}),  # type: ignore
  ("CCC", set()),  # type: ignore
]
@pytest.mark.parametrize(("rna", "peptides"), cases)
def test_rna_translation(rna, peptides):
  # if rna == "AUGCCC":
  #   pytest.skip()
  assert translate(RNA(rna)) == set(map(Peptide, peptides))


cases = [
  ("AUG", "M"),
  ("CCC", "P"),
  ("GGU", "G"),
]
@pytest.mark.parametrize(("codon", "peptide"), cases)
def test_get_peptide_from_codon(codon, peptide):
  assert get_peptide(codon) == peptide
