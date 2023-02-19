import pytest

def test_fail1():
    assert False


def test_pass():
    pass


@pytest.mark.skip
def test_skipped1():
    pass
