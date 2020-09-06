from typing import NewType   # Cheat sheet in docs: https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

# Domain Types:
Question = NewType("Question", str)
Answer = NewType("Answer", int)


# Source Code:
def get_the_answer(question: Question) -> Answer:
  ...


# Tests:
def test_the_answer():
  the_question = Question("Life, the Universe, and Everything")
  assert get_the_answer(the_question) == Answer(42)

