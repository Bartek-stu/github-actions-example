import unittest
import mathtools.functions as functions

import pytest

class TestMathFunctions(unittest.TestCase):
    def test_sub(self):
        assert functions.sub(5, 4) == 1
    
    def test_multiply(self):
        assert functions.multiply(3, 4) == 12
    
    def test_divide(self):
        assert functions.divide(10, 2) == 5

    def test_avg(self):
        assert functions.avg(1, 2, 3) == 2

    def test_divisor_is_zero_divide(self):
        with pytest.raises(ValueError) as ex:
            functions.divide(1, 0)
        assert str(ex.value) == "Denominator can't be equal to 0"

    def test_non_numeric_value(self):
        with pytest.raises(TypeError) as ex:
            functions.sub(3, "abc")
        assert str(ex.value) == "Values must be numeric"

if __name__ == "__main__":
    unittest.main()