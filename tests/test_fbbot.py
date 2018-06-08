import unittest

from fbbot import FBBot

def test_msg():
    msg = FBBot.msg
    assert msg == 'hello world'

