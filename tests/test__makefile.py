import pytest


@pytest.fixture
def project(scope="session"):
    print("Setup")
    yield 1
    print("Teardown")

def test__linting_pass(project):
    print(project)
    assert False

def test__test_pass():
    ...

def test__install_pass():
    ...