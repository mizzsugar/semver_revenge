# from __future__ import annotations

import unittest


class SemVer:
    def __init__(self, major: int, minor: int, patch: int) -> None:
        if major < 0:
            raise ValueError("メジャーバージョンは0以上")
        if minor < 0:
            raise ValueError("マイナーバージョンは0以上")
        if patch < 0:
            raise ValueError("パッチバージョンは0以上")
        
        self.major = major
        self.minor = minor
        self.patch = patch

    def get_notation(self) -> str:
        return str(self.major) + "." + str(self.minor) + "." + str(self.patch)

    def __eq__(self, other) -> bool:
        return self.get_notation() == other.get_notation() \
               and isinstance(other, SemVer)


class TestSemVer(unittest.TestCase):
    def test_major_minor_patchにそれぞれ1と4と2を与えてバージョンオブジェクトを作成(self):
        self.assertEqual("1.4.2", SemVer(1, 4, 2).get_notation())

    def test_major_minor_patchにそれぞれ2と30と400を与えてバージョンオブジェクトを作成(self):
        self.assertEqual("2.30.400", SemVer(2, 30, 400).get_notation())

    def test_同じバージョンを持つ2つのオブジェクトが等しいことを確認(self):
        self.assertTrue(SemVer(1, 4, 2) == SemVer(1, 4, 2))

    def test_違うバージョンを持つ2つのオブジェクトは等しくないことを確認(self):
        self.assertFalse(SemVer(1, 4, 2) == SemVer(2, 30, 400))

    def test_isinstanceの勉強(self):  # 学習テスト
        self.assertFalse(isinstance('hoge', SemVer))
        self.assertTrue(isinstance('hoge', str))
        self.assertTrue(isinstance(SemVer(1, 4, 2), SemVer))

    def test_バージョン番号は0以上の整数でなければならない(self):
        with self.subTest("メジャーバージョン"):
            self.assertRaises(ValueError, lambda: SemVer(-1, 4, 2))

        with self.subTest("マイナーバージョン"):
            self.assertRaises(ValueError, lambda: SemVer(1, -4, 2))

        with self.subTest("パッチバージョン"):
            self.assertRaises(ValueError, lambda: SemVer(1, 4, -2))


if __name__ == "__main__":
    unittest.main()
