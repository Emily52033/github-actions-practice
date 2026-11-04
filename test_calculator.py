from calculator import add, sub

def test_add():
    assert add(1,2) == 3
    assert add(-1, 5) == 4

def test_sub():
    assert sub(10,3) ==7
    assert sub(2,5) == -3
