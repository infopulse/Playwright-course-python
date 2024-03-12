from pytest import fixture


@fixture
def ultimate_answer():
    return 42


@fixture
def new_ultimate_answer(ultimate_answer):
    return ultimate_answer + 1
