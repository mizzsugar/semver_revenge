from __future__ import annotations

import unittest


class SemVer:
    def __init__(self, major: int, minor: int, patch: int) -> None:
        self.major = major
        self.minor = minor
        self.patch = patch

    def get_notation(self) -> str:
        return str(self.major) + "." + str(self.minor) + "." + str(self.patch)

    def __eq__(self, other: SemVer) -> bool:
        return True

class TestSemVer(unittest.TestCase):
    def test_major_minor_patchにそれぞれ1と4と2を与えてバージョンオブジェクトを作成(self):
        self.assertEqual("1.4.2", SemVer(1, 4, 2).get_notation())

    def test_major_minor_patchにそれぞれ2と30と400を与えてバージョンオブジェクトを作成(self):
        self.assertEqual("2.30.400", SemVer(2, 30, 400).get_notation())

    def test_同じバージョンを持つ2つのオブジェクトが等しいことを確認(self):
        self.assertTrue(SemVer(1, 4, 2) == SemVer(1, 4, 2))

    def test_違うバージョンを持つ2つのオブジェクトは等しくない(self):
        self.assertFalse(SemVer(1, 4, 2) == SemVer(2, 30, 400))


if __name__ == "__main__":
    unittest.main()
