import unittest


class VersionNumber:
    def __init__(self, value: int):
        if value < 0:
            raise ValueError("バージョン番号は0以上の整数でなければなりません")
        self.value = value


class SemVer:
    def __init__(self, major: VersionNumber, minor: VersionNumber, patch: VersionNumber):
        self.major = major
        self.minor = minor
        self.patch = patch

    def get_notation(self) -> str:
        return str(self.major.value) + "." + str(self.minor.value) + "." + str(self.patch.value)

    def __eq__(self, other) -> bool:
        return self.get_notation() == other.get_notation() \
               and isinstance(other, SemVer)

    @classmethod
    def generate(cls, major: int, minor: int, patch: int):
        return SemVer(VersionNumber(major), VersionNumber(minor), VersionNumber(patch))


class TestSemVer(unittest.TestCase):
    def test_major_minor_patchにそれぞれ1と4と2を与えてバージョンオブジェクトを作成(self):
        self.assertEqual("1.4.2", SemVer.generate(1, 4, 2).get_notation())

    def test_2つのSemVerオブジェクトの等価性を比較できる(self):
        with self.subTest("等しい場合"):
            self.assertTrue(SemVer.generate(1, 4, 2) == SemVer.generate(1, 4, 2))

        with self.subTest("異なる場合"):
            self.assertFalse(SemVer.generate(1, 4, 2) == SemVer.generate(1, 44, 244))

    def test_バージョン番号は0以上の整数であること(self):
        self.assertRaises(ValueError, lambda: VersionNumber(-1))

    def test_オブジェクトを生成しやすくする(self):
        self.assertEqual("1.4.2", SemVer.generate(1, 4, 2).get_notation())


if __name__ == "__main__":
    unittest.main()
