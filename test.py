import sqlite3
import mainfile
import unittest
import sys
sys.path.append("C:\\Users\\Ancy\\PycharmProjects\\PythonProblems\\src")
class test_demo(unittest.TestCase):
    def test_insertdb(self):
        a = open("department.txt", 'r')
        b = a.read()
        conn = sqlite3.connect(r'C:/Users/Ancy/Desktop/python problems/dept_manager.db')
        c = conn.cursor()
        d = mainfile.mycode(c)
        self.assertEqual(d,b)
if __name__ == '__main__':
    unittest.main()