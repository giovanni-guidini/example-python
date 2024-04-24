from app.random_module import say_hello


def test_hello():
    assert say_hello("world") == "Hello world"
    assert say_hello("Tom") == "Hello Tom"
