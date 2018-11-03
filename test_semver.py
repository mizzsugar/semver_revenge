import unittest


class SemVer:
    pass


class TestSemVer(unittest.TestCase):
    def test_major_minor_patchにそれぞれ1と4と2を与えてバージョンオブジェクトを作成(self):
        semver = SemVer(1, 4, 2)
        actual = semver.get_notation()

        expected = "1.4.2"
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
