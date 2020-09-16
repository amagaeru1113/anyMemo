import unittest

import caluculation

release_name = "lesson"


class CalTest(unittest.TestCase):
    def setUp(self):  # 共通して使う変数の設定
        print("setup")
        self.cal = caluculation.Cal()

    def tearDown(self):  # テスト終了後に行う処理 大きなメモリを使う場合とか
        print("clean up")
        del self.cal

    # @unittest.skip("skip！！！！")  # 何かの条件でテストをしない場合
    @unittest.skipIf(release_name == "lesson", "skip111")
    def test_add_num_and_double(self):
        self.assertEqual(self.cal.add_num_and_double(1, 1), 4)

    def test_add_num_and_double_raise(self):  # 例外のアサート
        cal = self.cal
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double("1", "1")


# python標準のテストモジュール

if __name__ == "__main__":

    unittest.main()
