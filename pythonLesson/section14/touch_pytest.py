import os

import pytest

import caluculation

# unittestより高機能なテストツール
# $ pytest touch_pytest.py


# class TestCal(object):
#     is_releasee = True

#     @classmethod
#     def setup_class(cls):
#         cls.cal = caluculation.Cal()

#     @classmethod
#     def teardown_class(cls):
#         del cls.cal

#     def setup_method(self, method):  # 共通して使う変数の設定
#         print("method = {}".format(method.__name__))
#         # self.cal = caluculation.Cal()

#     def tearDown_method(self, method):  # テスト終了後に行う処理 大きなメモリを使う場合とか
#         print("method = {}".format(method.__name__))
#         # del self.cal

#     def test_add_num_and_double(self):
#         assert self.cal.add_num_and_double(1, 1) == 4

#     def test_add_num_and_double_raise(self):  # 例外のアサート
#         with pytest.raises(ValueError):
#             self.cal.add_num_and_double("1", "1")

#     # @pytest.mark.skip(reason="skip")
#     @pytest.mark.skipif(is_releasee=True)
#     def test_add_num_and_double_raise(self):  # 例外のアサート
#         with pytest.raises(ValueError):
#             self.cal.add_num_and_double("1", "1")


# conftest
# 引数の内容に応じてテスト内容を帰る
# pytest touch_pytest.py --os-name mac -s # 引数内容を出力できる
# class TestCal(object):
#     @classmethod
#     def setup_class(cls):
#         cls.cal = caluculation.Cal()

#     def test_add_num_and_double(self, request):
#         os_name = request.config.getoption("--os-name")
#         print(os_name)
#         if os_name == "mac":
#             print("ls")
#         elif os_name == "windows":
#             print("dir")

#         assert self.cal.add_num_and_double(1, 1) == 4


# fixtures
class TestCal(object):
    @classmethod
    def setup_class(cls):
        cls.cal = caluculation.Cal()
        cls.test_file_name = "test.txt"
        cls.test_dir = "/tmp/test_dir"

    def teardown_class(cls):
        import shutil

        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)

    def test_save_no_dir(self):
        self.cal.save(self.test_dir, self.test_file_name)
        test_file_path = os.path.join(self.test_dir, self.test_file_name)
        assert os.path.exists(test_file_path) is True

    def test_add_num_and_double(self, csv_file):
        print(csv_file)

        assert self.cal.add_num_and_double(1, 1) == 4

    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path) is True

    def test_add_num_and_double_raise(self):  # 例外のアサート
        with pytest.raises(ValueError):
            self.cal.add_num_and_double("1", "1")
