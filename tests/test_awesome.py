from app.inner.app.inner.awesome import g
from app.inner.inner import f


def test_g():
    assert g(2) == 4
    assert g(1000) == 2000


def test_f():
    assert f(10) == 1010
    assert f(20) == 1020
