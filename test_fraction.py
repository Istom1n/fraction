from fraction import get_num_dem


def test_get_num_dem():
    assert get_num_dem(1 / 3) == (1, 3)
    assert get_num_dem(5 / 12) == (5, 12)
    # Reduced fraction
    assert get_num_dem(34 / 354) == (17, 177)
