from pytest import mark


@mark.testomatio('@Te5a947f2')
def test_ultimate_answer(ultimate_answer):
    assert ultimate_answer == 42


@mark.testomatio('@Te4434ddc')
def test_new_ultimate_answer(new_ultimate_answer):
    assert new_ultimate_answer == 43


@mark.testomatio('@T8530464d')
def test_both_answers(ultimate_answer, new_ultimate_answer):
    assert ultimate_answer == 42
    assert new_ultimate_answer == 43
