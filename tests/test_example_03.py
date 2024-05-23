from pytest import mark
import os
from pytest import fixture


@fixture
def manage_file():
    with open('test.txt', 'w') as file:
        file.write('This is a test file')
    yield
    os.remove('test.txt')


def test_file_created(manage_file):
    with open('test.txt', 'w') as file:
        file.write('new text')
    assert os.path.exists('test.txt')


def test_test_file_name(request):
    assert request.fspath.basename == 'test_example_03.py'
