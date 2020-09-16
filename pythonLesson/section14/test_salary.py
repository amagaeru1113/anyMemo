import unittest
from unittest.mock import MagicMock
from unittest import mock

import salary

# mock httpリクエストで得られるものを仮に設定する


class TestSalary(unittest.TestCase):
    def test_calculations(self):
        s = salary.Salary(year=2019)
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calculation_salary(), 101)
        s.bonus_api.bonus_price.assert_called()
        s.bonus_api.bonus_price.assert_called_once()
        s.bonus_api.bonus_price.assert_called_with(year=2019)
        self.assertEqual(s.bonus_api.bonus_price.call_count, 1)

    def test_calculations_salaly_no_salary(self):
        s = salary.Salary(year=2050)
        s.bonus_api.bonus_price = MagicMock(return_value=0)
        self.assertEqual(s.calculation_salary(), 100)
        s.bonus_api.bonus_price.assert_not_called()

    # MagincMockを使わずに記述可能
    @mock.patch("salary.ThirdPartyBonusRestAPI.bonus_price")
    def test_calculations_salaly_patch(self, mock_bonus_price):
        mock_bonus_price.return_value = 1

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(s.calculation_salary(), 101)
        mock_bonus_price.assert_called()

    # デコレータではなくwithでも記述可能
    def test_calculations_salaly_patch_with(self):
        with mock.patch(
            "salary.ThirdPartyBonusRestAPI.bonus_price"
        ) as mock_bonus_price:
            mock_bonus_price.return_value = 1

            s = salary.Salary(year=2017)
            salary_price = s.calculation_salary()

            self.assertEqual(salary_price, 101)
            mock_bonus_price.assert_called()

    # patcherとして記述可能
    # def test_calculations_salaly_patch_with(self, mock_bonus_price):
    #     patcher = mock.patch("salary.ThirdPartyBonusRestAPI.bonus_price")
    #     mock_bonus_price = patcher.start()
    #     mock_bonus_price.return_value = 1

    #     s = salary.Salary(year=2017)
    #     salary_price = s.calculation_salary()

    #     self.assertEqual(salary_price, 101)
    #     mock_bonus_price.assert_called()

    #     patcher.stop()

    # setUpとtearDownに記述してpather使うことも可能
    def setUp(self):
        self.patcher = mock.patch("salary.ThirdPartyBonusRestAPI.bonus_price")
        self.mock_bonus_price = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_calculations_salaly_with_patcher(self):
        self.mock_bonus_price.return_value = 1

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)
        self.mock_bonus_price.assert_called()

    def test_calculations_salaly_patch_with_side_effect(self):
        # 関数の形で書き換えられる。 この部分はlambdaでもよい
        def f(year):
            return 1

        self.mock_bonus_price.side_effect = f
        self.mock_bonus_price.side_effect = ConnectionRefusedError

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 100)
        self.mock_bonus_price.assert_called()
