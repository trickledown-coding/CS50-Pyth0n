from jar import jar

def test_capacity():
    assert(jar.capacity) == 12

def test_withdraw():
    assert(jar.withdraw(5)) == 7