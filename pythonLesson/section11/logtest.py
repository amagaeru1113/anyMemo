import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

h = logging.FileHandler("logtest.log")
logger.addHandler(h)
# ハンドラーに渡したもの（loggerの内容）がファイルに書き込まれる
# https://docs.python.org/ja/3/library/logging.handlers.html


def _do_something():
    logger.info("from logtest")
    logger.debug("from logtest debug")

