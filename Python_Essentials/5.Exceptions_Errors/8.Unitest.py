'''
Unit Testing

A module in Python’s standard library called `unittest` contains tools for testing your code.

Unit testing checks if all specific parts of your function’s behavior are correct, 
making integrating them with other parts of our project much more effortless and manageable.
'''
import unittest
import my_test # 想要測試的.py檔案

class MyTest(unittest.TestCase): # 繼承自 unittest.TestCase 的類來定義測試案例
    def test_one(self): # 每個測試案例定義為類中以 test_ 開頭
        text = "sample"
        result = my_test.test_func(text)
        self.assertEqual(result, "Sample")

    def test_two(self):
        text = "just testing"
        result = my_test.test_func(text)
        self.assertEqual(result, "Just Testing")


if __name__ == "__main__":
    unittest.main() # 自動發現並運行所有繼承自 unittest.TestCase 的測試類

'''
在 unittest.TestCase 中，有多種斷言方法 (assertion methods)，用來檢查代碼是否符合預期。常見的有：

1. assertEqual(a, b)：檢查 a == b 是否為真。 
2. assertNotEqual(a, b)：檢查 a != b 是否為真。
3. assertTrue(x)：檢查 x 是否為 True。
4. assertFalse(x)：檢查 x 是否為 False。
5. assertIs(a, b)：檢查 a 是否是 b 的同一個對象。
6. assertIsNot(a, b)：檢查 a 和 b 是否不是同一個對象。
7. assertIsNone(x)：檢查 x 是否是 None。
8. assertIsNotNone(x)：檢查 x 是否不是 None。
9. assertIn(a, b)：檢查 a 是否在 b 中。
10. assertNotIn(a, b)：檢查 a 是否不在 b 中。
11. assertRaises(exception, callable, *args, **kwds)：檢查調用 callable 時是否會引發 exception。

'''