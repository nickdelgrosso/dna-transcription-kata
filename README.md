# DNA Transcription and Translation Kata

![](/dna_diagram.png)

This is a bioinformatics-related code kata designed for practicing test-driven development in tasks that involve data processing.

## Goal:

Write a program that can take a DNA sequence as input and, as output, show all the hypothetical protein sequences that could be translated from it.

Example:
  - Input DNA Sequence: **AGGACGGGCTAACTCCGCTCGTCACAAAGCGCAATGCAGCTATGGCAGATGTTCATGCCG**
  - Output Protein Sequence: **MNICHSCIALCDERS**

### Specifications:

Below are the specifications in written form.  For a diagram, see the picture **dna_kata_explanation.png** in this folder.

  - DNA sequences are sequences of A, T, C, and G *nucleotides*.
    - *Example DNA Sequence*: ttatttgggcatcc
    - Because DNA is double-stranded, for every dna sequence there is also the **antisense** sequence, which is the sequence reversed and changed in the following pattern: A->T, T->A, C->G, G->C

  - DNA is *transcribed* into RNA sequences, which contain A, U, C, and G *nucleotides*.
    - DNA is read in reverse order.
    - RNA transcription follows the following pattern: A->U, T->A, C->G, G->C.
    - *Example Transcription*: TTATGCATC -> GAUGCAUAA

  - RNA is *translated* into a protein sequence by converting sets of 3 nucleotides (called a *codon*) into a single *peptide*.
    - RNA is read in the forwards direction and can be started from the 1st, 2nd, or 3rd nucleotide.
    - The table "codons.json" contains the relationships between RNA codons and the peptides produced.
    - The first peptide in the protein sequence is always **Met** -- everything beforehand is ignored.
    - The last peptide in the sequence is always the one before a "STOP" codon--everything afterward, including the first STOP, is ignored.
    - If there is no "Met" to start the sequence and no "STOP" to end it, no protein sequence is created at all.  
    - Protein sequences are written as one-letter codes.  The file "peptides.json" contains the relationship between the three- and one-letter codes.
    - *Example Translation from RNA*: ggaugcccaaauaa -> [Met, Pro, Arg] == MPK

Try it out using this [online tool](https://web.expasy.org/translate/) and type in the following sequence: **ttatttgggcatcc** and press the "Translate" button, and look for the protein sequence highlighted in red.
