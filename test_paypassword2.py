#coding:utf-8
import binascii
import base64
import pyDes

class DES:
    #IV必须是 8 字节长度的十六进制数
    iv = 'hellocxp'
    #key加密密钥长度，24字节
    key = 'E10ADC3949BA59ABBE56E057F20F883E'
    def __init__(self, iv, key):
        self.iv = iv
        self.key = key
    def encrypt(self, data):
        k = pyDes.triple_des(self.key, pyDes.ECB, self.iv, pad=None, padmode=pyDes.PAD_PKCS5)
        d = k.encrypt(data)
        d = base64.encodestring(d)
        return d
    def decrypt(self, data):
        k = pyDes.triple_des(self.key, pyDes.ECB, self.iv, pad=None, padmode=pyDes.PAD_PKCS5)
        data = base64.decodestring(data)
        d = k.decrypt(data)
        return d
if __name__ == '__main__':
    data = "123456"
    des = DES('123456','1234567812345678')
    encryptdata = des.encrypt(data.encode('utf-8'))
    print  encryptdata
    decryptdata = des.decrypt(encryptdata)
    print decryptdata