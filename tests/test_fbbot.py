import unittest

from fbbot import return_msg

def test_msg():
    msg = 'hello world'
    assert return_msg(msg) == msg

