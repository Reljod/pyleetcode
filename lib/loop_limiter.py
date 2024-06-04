"""
Author: Reljod Oreta

Library to prevent infinite loop on any loop like while loop or unbounded for loop.

This is specially useful when testing script and running it by assertion using testing libraries since
it breaks infinite loops and allows gracefully failing the tests.
"""

class LoopLimiter:
    def __init__(self, limit: int = 1_000_000, msg="Program might be broken. Loop stopped.") -> None:
        self.limit = limit
        self.msg = msg

    def is_at_limit(self) -> bool:
        if self.limit == 0:
            print(self.msg)
            return True

        self.limit -= 1
        return False
