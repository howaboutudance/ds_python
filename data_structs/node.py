from collections.abc import Sized, Container
from typing import Collection, Text, MutableSequence
import copy

class Node (Collection):
    def __init__(self, v: int) -> None:
        self._val = v
        self.next = None
        if v is None:
            self.size = 0
        else:
            self.size = 1

    def __iter__(self):
        return self 

    def append(self, v: int):
        n = self
        while n.next is not None:
            n = n.next

        self.size += 1 
        n.next = Node(v)
    
    def __contains__(self, v: int) -> bool:
        n = self
        while n is not None:
            if n._val == v:
                return True
            n = n.next
        
        return False

    def __len__(self) -> int:
        return self.size
    
    def toList(self):
        res = list()
        n = self
        while(n is not None):
            res.append(n._val)
            n = n.next
        return res

    def __str__(self):
        res = ""
        n = self
        while n is not None:
            if n.next is not None:
                res += f"{n._val}, "
            else:
                res += f"{n._val}"
            n = n.next
        return "<" + res + ">"

    def reverse(self):
        cur = self
        cur_next = self.next
        temp = copy.copy(cur)
        temp.next = None
        while cur_next is not None:
            cur = copy.copy(cur_next)
            cur.next = temp
            (temp, cur_next) = (cur, cur_next.next)
        return cur
    
    def __reversed__(self):
        self.reverse()

    def __getitem__(self, idx: int):
        iter = 0
        if idx < 0:
            idx = len(self) + idx
        n = self
        while iter < len(self):
            if iter == idx:
                return n.value
            n = n.next
            iter += 1

        raise IndexError

    def isPalindrome(self):
        orig = self
        reversed = (copy.copy(self)).reverse()
        while orig is not None:
            if orig._val != reversed._val:
                return False
            (orig, reversed) = (orig.next, reversed.next)
        return True


    @property
    def value(self):
        return self._val
    
    @value.setter
    def value(self, v):
        self._val = v
    

if __name__ == "__main__":
    test_array = Node(1)
    test_array.append(2)
    test_array.append(3)
    test_array.append(4)
    print(f"size {len(test_array)}")
    print(f"array is {test_array}")
    print(f"as list is {test_array.toList()}")
    print(f"reversed array is {test_array.reverse()}")
    print(f"{test_array} is a palidrome {test_array.isPalindrome()}")
    pali_array = Node(1)
    pali_array.append(0)
    pali_array.append(0)
    pali_array.append(1)
    print(f"{pali_array} is a palidrome {pali_array.isPalindrome()}")
    pali_odd = Node(1)
    pali_odd.append(0)
    pali_odd.append(1)
    print(f"{pali_odd} is a palidrome {pali_odd.isPalindrome()}")
    test_array.reverse()
    print(f"using reverse {test_array}")
    print(f"1st element of test_array is {test_array.__getitem__(0)}")
    print(f"last element of test_array is {test_array.__getitem__(3)}")
    print(f"last element of test_array is {test_array.__getitem__(-1)}")
    print(f"last element of test_array is {test_array.__getitem__(-3)}")
    print(f"using accessors {test_array[0]}")