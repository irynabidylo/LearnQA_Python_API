class TestExample:
    def test_check_math(self):
        a = 5
        b = 9
        expected_sum = 14
        assert a+b == 14,  f"Sum of variables a and b is not equal {expected_sum}"

    def test_check_math2(self):
        a = 5
        b = 8
        expected_sum = 14
        assert a+b == expected_sum, f"Sum of variables a and b is not equal {expected_sum}"
