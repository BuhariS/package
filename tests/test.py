from my_package import myModule

def test_top_vals():
    assert myModule.top_n_values([3, 7, 5, 9], 2) == [7, 9], 'incorrect'
    assert myModule.top_n_values([3, 7, 5, 9], 3) == [5, 7, 9], 'incorrect'