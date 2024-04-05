
from app.packages.apptest.containers.MyPackage.MyPackage import g


def test_my_package():
    assert g() == 32