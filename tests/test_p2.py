from p2.p2 import multibit_negative, multibit_subtractor

def test_multibit_negative():
    # 3 in 3-bit: 0b011 -> [1,1,0]
    A = [1,1,0]
    expected = [1,0,1]  # -3 in 3-bit two's complement
    assert multibit_negative(A) == expected

def test_multibit_subtractor():
    # A - B
    A = [1,1,0]  # 3
    B = [1,0,0]  # 1
    expected = [0,1,0]  # 2
    assert multibit_subtractor(A, B) == expected

    # A == B -> result should be zero
    A = [1,1,0]
    B = [1,1,0]
    expected = [0,0,0]
    assert multibit_subtractor(A, B) == expected

    # B > A -> negative result in two's complement
    A = [1,0,0]  # 1
    B = [1,1,0]  # 3
    expected = [0,1,1]  # -2 in 3-bit
    assert multibit_subtractor(A, B) == expected
