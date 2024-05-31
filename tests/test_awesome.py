from app.inner.app.inner.awesome import g


def test_g():
    assert g(2) == 4
    assert g(1000) == 2000
