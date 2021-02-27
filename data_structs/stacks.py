from typing import NoReturn, Text
import copy

class Stack:
    def __init__(self, orig: int) -> NoReturn:
        self.value = orig
        self.next = None
        self._min = orig
    
    def pop(self) -> int:
        res = copy.copy(self)

        if self.min == self.value:
            if self.next is None:
                self._min = 0
            n = self.next
            while(n.next is not None):
                if n.value <= self._min:
                    self._min = n.value
                n = self.next

        if self.next is None:
            self.value = None
        else:
            self.value = self.next.value
            self.next = self.next.next


        return res.value

    def push(self, v: int):
        n = self
        self.value = v
        self.next = copy.copy(n)
        if self.min > v:
            self._min = self.value

    def peek(self):
        return self.value
    
    def isEmpty(self):
        return self.value == None
    
    @property
    def min(self):
        return self._min

if __name__ == "__main__":
    test_res = Stack(1)
    test_res.push(4)
    test_res.push(5)
    assert not test_res.isEmpty()
    assert test_res.min == 1
    test_res.push(-1)
    assert test_res.min == -1
    print(test_res.pop())
    print(test_res.pop())
    print(test_res.pop())
    print(test_res.pop())
    print(test_res.isEmpty())
    print(test_res.value)
    assert test_res.isEmpty()
