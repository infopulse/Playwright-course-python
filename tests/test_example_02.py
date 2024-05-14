from pytest import mark


@mark.testomatio('@Ta70b9067')
def test_ultimate_answer(ultimate_answer):
    assert ultimate_answer == 42


@mark.testomatio('@T763af140')
def test_new_ultimate_answer(new_ultimate_answer):
    assert new_ultimate_answer == 43


@mark.testomatio('@T73ed88ad')
def test_both_answers(ultimate_answer, new_ultimate_answer):
    assert ultimate_answer == 42
    assert new_ultimate_answer == 43
