from zoran_coherence.engine import evaluate_relative_invariance

def test_relative_invariance_true():
    assert evaluate_relative_invariance([10, 9, 11], 0.2) is True

def test_relative_invariance_false():
    assert evaluate_relative_invariance([10, 7, 11], 0.2) is False

def test_relative_invariance_single_value():
    assert evaluate_relative_invariance([10], 0.2) is True

def test_relative_invariance_zero_max():
    assert evaluate_relative_invariance([0, 0], 0.2) is False
