import pytest
from task2.task_two import Number

class TestNumber:
    def setup_method(self):
        self.converter_positive = Number(10)
        self.converter_negative = Number(-10)

    def test_conversion_to_octal(self):
        assert self.converter_positive.conversion_to_octal() == '0o12'
        assert self.converter_negative.conversion_to_octal() == '-0o12'