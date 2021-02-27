# (C) 2021 Michael Penhalleogn <mike@hematite.tech>, All rights reserved.
from typing import Mapping, Sequence, Any, Tuple
import logging


KEYPAD: Mapping[str, Tuple[Any]] = {str(k): tuple(v) for (k, v) in {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
}.items()}


class T9Sequence:
    """ Holds the "model" of a T9 source sequence, a 2d list-tuple structure of
    keypad options per tuple cell."""
    __keypad: Mapping[str, Tuple[Any]] = {"1": tuple(), "0": (" ")} | KEYPAD

    def __init__(self, v: int):
        """ initlizes the object taking a integer value

        :param v: value to create model from 
        """
        self._value = v
        self._str_value: str = str(v)
        self._cols = self.help_generate_cols()

    def __contains__(self, word: str) -> bool:
        """dunder method to enable contains api
        
        this enables the use of :code:`"foo" in T9Sequence` syntax to be used. 
        first checks that word and self._cols are same length and if so, maps
        if each char in word is in tuple cell of self._cols. Returns all() value
        of boolean list

        :param word: value to be checked
        :returns: boolean value of if word matchs premutation within self._cols.
        """
        if len(self._cols) != len(word):
            logging.debug(f"value {word} is too long")
            return False
        else:
            res = map(self.search_col, enumerate(word))
            logging.debug(f"{list(zip(word, res))} compared to {self._cols}")
            return all(res)

    def search_col(self, v: Sequence) -> bool:
       """ heper function to compare a single character string to cells inside
       self._cols

       :param v: value to compare to _cols cells
       :return: if v is found in _cols
       """
       idx, val = v
       return val in self._cols[idx]


    def help_generate_cols(self) -> Sequence[Sequence[str]]:
        def col_gen(vi: str):
            return list(self.__keypad[vi])
        
        return list(filter(None, map(col_gen, self._str_value)))