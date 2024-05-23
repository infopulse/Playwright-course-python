from pytest import mark


def test_ultimate_answer(ultimate_answer):
    assert ultimate_answer == 42


def test_new_ultimate_answer(new_ultimate_answer):
    assert new_ultimate_answer == 43


def test_both_answers(ultimate_answer, new_ultimate_answer):
    assert ultimate_answer == 42
    assert new_ultimate_answer == 43
