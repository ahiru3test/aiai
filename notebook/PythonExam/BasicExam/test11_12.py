import unittest
# import mod

class mod:
  def calc(a,b):
    return a*b

class TestSample(unittest.TestCase):
  def test_it(self):
    actual=mod.calc(2,3)
    print(actual)
    expected = 5
    self.assertEqual(actual,expected)

if (__name__=="__main__"):
  print(mod.calc(2,3))
