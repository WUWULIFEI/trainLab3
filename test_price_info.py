import price_info as file

def test_total_cost_shopping():
    result=9.9
    output=file.total_cost_shopping()
    assert(result==output)


def test_cost_of_fruit():
    result=12.0
    output=file.cost_of_fruit('apple', 10)
    assert(result==output)