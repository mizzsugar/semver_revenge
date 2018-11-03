import unittest


class SemVer:
    def __init__(self, major: int, minor: int, patch: int) -> None:
        self.major = major
        self.minor = minor
        self.patch = patch

    def get_notation(self) -> str:
        return str(self.major) + "." + str(self.minor) + "." + str(self.patch)


class TestSemVer(unittest.TestCase):
    def test_major_minor_patchにそれぞれ1と4と2を与えてバージョンオブジェクトを作成(self):
        self.assertEqual("1.4.2", SemVer(1, 4, 2).get_notation())

    def test_major_minor_patchにそれぞれ2と30と400を与えてバージョンオブジェクトを作成(self):
        self.assertEqual("2.30.400", SemVer(2, 30, 400).get_notation())


if __name__ == "__main__":
    unittest.main()
