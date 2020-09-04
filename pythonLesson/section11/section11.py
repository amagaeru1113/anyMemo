#  -------------------------------------------------------------------------
# 118.config parser

# import configparser

# config.iniの作成
# config = configparser.ConfigParser()
# config["DEFAULT"] = {"debug": True}

# config["web_server"] = {"host": "127.0.0.1", "port": 80}

# config["db_server"] = {"host": "127.0.0.1", "port": 3306}

# with open("config.ini", "w") as config_file:
#     config.write(config_file)

# config.iniの読み込み
# config = configparser.ConfigParser()
# config.read("config.ini")
# print(config["web_server"]["port"])


#  -------------------------------------------------------------------------
# 119.yaml
# pip instal pyyaml

# import yaml

# with open("config.yml", "w") as yaml_file:
#     yaml.dump(
#         {
#             "web_server": {"host": "127.0.0.1", "port": 80},
#             "db_server": {"h0st": "127.0.0.1", "port": 3306},
#         },
#         yaml_file,
#         default_flow_style=False,
#     )


# with open("config.yml", "r") as yaml_file:
#     data = yaml.load(yaml_file)
#     print(data["web_server"]["port"])


#  -------------------------------------------------------------------------
# 120.ロギング
# import logging

# logging.basicConfig(
#     filename="test.log", level=logging.INFO
# )  # infoまでやる 対外はアプリの運用ではinfo以上

# # logging.critical("critical")
# # logging.error("error")
# # logging.warning("warning")
# # logging.info("info")
# # logging.debug("debug")

# # logging.info("info %s" % "test")
# logging.info("info %s", "test")
# # INFO:root:info test

#  -------------------------------------------------------------------------
# 121.ロギング フォーマッタ


# import logging

# # formater = "%(levelname)s:%(message)s"
# # formater = "%(asctime)s:%(message)s"  # log出力のフォーマット
# # logging.basicConfig(level=logging.INFO, format=formater)


# # logging.info("info %s" % "test")
# logging.info("info %s", "test")
# # INFO:root:info test

#  -------------------------------------------------------------------------
# 122.ロギング ロガー


# import logging

# logging.basicConfig(level=logging.INFO)

# logging.info("info")

# logger = logging.getLogger(__name__)  # loggingのbasciを受け継いで、ログレベルを変えられる
# logger.setLevel(logging.DEBUG)
# logger.debug("debug")


# import logtest

# logtest._do_something()

# """
# mainでloglevelを設定して、以降其のloggerを使う
# loggerをトップで読み込んで、logger側で詳細なカスタマイズを行う
# """

#  -------------------------------------------------------------------------
# 123.ロギング ハンドラー
# import logging
# import logtest

# logging.basicConfig(level=logging.INFO)

# logger = logging.getLogger(__name__)  # loggingのbasciを受け継いで、ログレベルを変えられる
# logger.info("from main")

# logtest._do_something()

#  -------------------------------------------------------------------------
# 124.ロギング フィルタ
# import logging
# import logtest

# logging.basicConfig(level=logging.INFO)


# class NoPassFilter(logging.Filter):
#     def filter(self, record):
#         log_message = record.getMessage()
#         return "password" not in log_message


# logger = logging.getLogger(__name__)
# logger.addFilter(NoPassFilter())  # messageのフィルタ
# logger.info("from main")
# logger.info('from main password = "test"')

#  -------------------------------------------------------------------------
# 125.ロギング コンフィグ
# import logging.config

# logging.config.fileConfig("logging.ini")  # loggin.iniを予め作成してそれを使う
# # dictConfigでも設定できる
# logger = logging.getLogger("simpleExample")

# logger.debug("debug message")
# logger.info("info message")
# logger.warning("warn message")
# logger.error("error message")
# logger.critical("critical message")


#  -------------------------------------------------------------------------
# 126.ロギング ロギングの書き方

# import logging


# logger = logging.getLogger(__name__)

# logger.error("Api call is failed")

# logger.error({"action": "create", "status": "fail", "message": "Api call is failed"})

# 運用してトラブルが起きたときにも情報収集ができるように

#  -------------------------------------------------------------------------
# 127.Email送信

# from email import message
# import smtplib

# smtp_host = "smtp.live.com"
# smtp_port = 587
# from_email = "xxxxx"
# to_email = "xxxxx"
# username = "xxxxx"
# password = "yyyyyyy"

# msg = message.EmailMessage()
# msg.set_content("Test email")
# msg["Subhect"] = "Test email sub"
# msg["From"] = from_email
# msg["To"] = to_email

# server = smtplib.SMTP(smtp_host, smtp_port)
# server.ehlo()  # smtpを使いますよ
# server.starttls()  # secureにして
# server.ehlo()
# server.login(username, password)
# server.send_message(msg)
# server.quit()
# gmailとかだと違う

#  -------------------------------------------------------------------------
# 128.添付ファイルEmail送信

# from email import message
# from email.mime import multipart
# from email.mime import text
# import smtplib

# smtp_host = "smtp.live.com"
# smtp_port = 587
# from_email = "xxxxx"
# to_email = "xxxxx"
# username = "xxxxx"
# password = "yyyyyyy"

# # msg = message.EmailMessage()
# msg = multipart.MIMEMultipart()
# # msg.set_content("Test email")
# msg["Subhect"] = "Test email sub"
# msg["From"] = from_email
# msg["To"] = to_email
# msg.attach(text.MIMEText("Text email", "plain"))

# with open("section11.py", "r") as f:
#     attachment = text.MIMENonMultipart(f.read(), "plain")
#     attachment.add_header("Content-Disposition", "attachment", filename="section11.py")
#     msg.attach(attachment)

# server = smtplib.SMTP(smtp_host, smtp_port)
# server.ehlo()  # smtpを使いますよ
# server.starttls()  # secureにして
# server.ehlo()
# server.login(username, password)
# server.send_message(msg)
# server.quit()


#  -------------------------------------------------------------------------
# 129.SMTPハンドラーでログをEmail送信

# import logging
# import logging.handlers

# smtp_host = "smtp.live.com"
# smtp_port = 587
# from_email = "xxxxx"
# to_email = "xxxxx"
# username = "xxxxx"
# password = "yyyyyyy"

# logger = logging.getLogger("email")
# logger.setLevel(logging.CRITICAL)

# logger.addHandler(
#     logging.handlers.SMTPHandler(
#         (smtp_port, smtp_host),
#         from_email,
#         to_email,
#         subject="Admin test log",
#         credentials=(username, password),
#         secure=(None, None, None),
#         timeout=20,
#     )
# )

# logger.info("test")
# logger.critical("ciritcal")


#  -------------------------------------------------------------------------
# 130.virtualenv

# virtualenvでpythonバージョンの異なる仮想環境の作成・切替が可能
# 個人的にはpyenv + ライブラリ管理poetryを使用
# 最近はDockerの練習でDocker + poetryを使用


#  -------------------------------------------------------------------------
# 131.optparse

# from optparse import OptionParser


# def main():
#     usage = "usage: %prog [options] arg1 arg2"
#     parser = OptionParser(usage=usage)
#     parser.add_option(
#         "-f", "--file", action="store", type="string", dest="filename", help="File name"
#     )
#     options, args = parser.parse_args()
#     print(options)
#     print(args)
#     print(options.filename)


# if __name__ == "__main__":
#     main()

# optparseでoptions操作でよしなに渡しやすくできる -> configを作るまでもないが、ハードコードしたくない
