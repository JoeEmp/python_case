import logging

DOMAIN = 'localhost'
PORT = 4723
COMMAND_EXECUTOR_URL = "http://%s:%d/wd/hub" % (DOMAIN, PORT)
is_debug = False
implicitly_wait_sec = 100

# where apk no find file path or url
apk_install_path = '/Users/joe/Documents/CodeManager/git_repo/github/learn_case/frame/bddwithAppium/ee.dustland.android.dustlandsudoku.apk'

log_conf = {
    "format": "%(asctime)s %(levelname)s \"%(pathname)s\", line %(lineno)d, %(message)s",
    "level": logging.INFO,
}

logging.basicConfig(**log_conf)
