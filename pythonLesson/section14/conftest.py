import os
import pytest

# pytest実行時に読み込まれる


def pytest_addoption(parser):
    parser.addoption("--os-name", default="linux", help="os name")


# 独自のfixture
@pytest.fixture
def csv_file(tmpdir):
    with open(os.path.join(tmpdir, "test.csv"), "w") as c:  # yieldの前後に処理を付随できる
        print("before")
        yield c
        print("after")

