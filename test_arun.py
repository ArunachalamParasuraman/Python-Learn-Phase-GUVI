import pytest
from arun_test1 import Add
from arun_test1 import Multiply

def test_Add_Function_1():
    assert(Add(10,20))==30

def test_Add_Function_2():
    assert(Add(10,20))==40

def test_Multiply_Function_1():
    assert(Multiply(5,5))==25

def test_Multiply_Function_2():
    assert(Multiply(5,5))==30
