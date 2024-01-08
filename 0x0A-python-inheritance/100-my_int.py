#!/usr/bin/python3
"""func that defines a class MyInt"""


class MyInt(int):
    """Invert int operators == and !=."""

    def _eq_(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def _ne_(self, value):
        """Override != operator with == behavior."""
        return self.real == value