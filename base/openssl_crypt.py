import os
import logging


class CryptFile():

    def __init__(self, pri_key, pub_key):
        self.has_env = self.check_openssl()
        self.pri_key = pri_key
        self.pub_key = pub_key
        self.suffix = '.encode'

    def check_openssl(self):
        result = os.popen('openssl version').read()
        if 'SSL' not in result.upper():
            logging.warning('环境缺少openssl')
            return False
        return True


class EncryptFile(CryptFile):

    def __init__(self, pub_key):
        super().__init__(pri_key='', pub_key=pub_key)

    def encrypt(self, file: str, debug=False):
        # openssl rsautl -encrypt -inkey pub.key -pubin -in data.zip -out back.zip
        if not self.has_env:
            logging.warning('环境缺少openssl')
            return ''
        encode_file = file + self.suffix
        if not os.path.exists(file):
            logging.warning('加密文件不存在')
            return ''
        if not debug:
            os.system('openssl rsautl -encrypt -inkey {} -pubin -in {} -out {}'.format(
                self.pub_key, file, encode_file))
            os.system('rm -f {}'.format(file))
        else:
            print('openssl rsautl -encrypt -inkey {} -pubin -in {} -out {}'.format(
                self.pub_key, file, encode_file))
        return encode_file


class DecryptFile(CryptFile):

    def __init__(self, pri_key):
        super().__init__(pri_key=pri_key, pub_key='')

    def decrypt(self, encode_file: str, debug=False):
        # openssl rsautl -decrypt -inkey pri.key -in back.zip -out data.zip
        if not self.has_env:
            logging.warning('环境缺少openssl')
            return ''
        if not os.path.exists(encode_file):
            logging.warning('解密文件不存在')
            return ''
        if encode_file.endswith(self.suffix):
            file = encode_file[:-len(self.suffix)]
        else:
            file = encode_file
        if not debug:
            os.system(
                'openssl rsautl -decrypt -inkey {} -in {} -out {}'.format(self.pri_key, encode_file, file))
            os.system('rm -f {}'.format(encode_file))
        else:
            print(
                'openssl rsautl -decrypt -inkey {} -in {} -out {}'.format(self.pri_key, encode_file, file))
        return file
