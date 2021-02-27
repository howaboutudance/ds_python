import pytest
import logging
from data_structs.t9 import T9Sequence

def test_t9_example():
    inp = 8733
    t_obj = T9Sequence(inp)
    assert "tadpole" not in t_obj
    assert "tree" in t_obj 
    assert "used" in t_obj 
    assert "empire" in T9Sequence(336743)
    assert "development" in T9Sequence(33835676368)

def test_t9_cols_gen(caplog):
    caplog.set_level(logging.DEBUG)
    t_obj = T9Sequence(213)
    assert [["a", "b", "c"], ["d", "e", "f"]] == t_obj._cols

def test_t9_one_filter():
    t_obj = T9Sequence(87133)
    assert "tree" in t_obj

def test_t9_space():
    t_obj = T9Sequence(8733044)
    assert "tree hi" in t_obj
    