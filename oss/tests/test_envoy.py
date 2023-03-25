import unittest
import envoy


class SimpleTest(unittest.TestCase):
    def test_input(self):
        r = envoy.run("sed s/i/I/g", "Hi")
        self.assertEqual(r.std_out.rstrip(), "HI")
        self.assertEqual(r.status_code, 0)


if __name__ == '__main__':
    unittest.main()
