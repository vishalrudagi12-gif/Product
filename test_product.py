from product import product_info
def test_product_info():
    result = product_info(101, "Laptop", 5, 45000)

    expected = (
        f"Product ID: 101\n"
        f"Product Name: Laptop\n"
        f"Quantity: 5\n"
        f"Price: 45000"
    )
    assert result == expected 