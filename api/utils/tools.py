import string, secrets
from passlib.context import CryptContext


class Hashing(object):
    """密码工具类"""

    def __init__(self, schemes: str = 'bcrypt'):
        self.crypt = CryptContext(schemes=[schemes], deprecated="auto")

    def hash(self, raw_pwd: str) -> str:
        """
        密码加密
        :param raw_pwd: 用户输入的原始密码
        :return: 密码的哈希值
        """
        return self.crypt.hash(raw_pwd)

    def verify(self, raw_pwd: str, hashed_pwd: str) -> bool:
        """
        验证密码是否正确
        :param raw_pwd: 用户输入的原始密码
        :param hashed_pwd: 密码的哈希值
        :return: bool
        """
        return self.crypt.verify(raw_pwd, hashed_pwd)


def genint(length: int = 4) -> str:
    """
    生成指定长度的纯数字字符串
    @param length: 字符长度
    return
    """
    characters = string.digits
    ret = "".join(secrets.choice(characters) for i in range(length))
    return ret

def genkey(length: int=64) -> str:
    """
    生成指定长度的随机字符串
    :param length: 生成的字符串的长度
    :return: 字符串
    """
    characters = string.ascii_letters        # 26个小写字母和26个大写字母
    characters = characters + string.digits  # 10个数字
    characters = characters + '!@$%^&*./-'  # 特殊符号
    return "".join(secrets.choice(characters) for i in range(length))


if __name__ == '__main__':
    hashing = Hashing()
    # 对原始密码进行哈希加密
    password_hash1 = hashing.hash("123456")
    print(password_hash1)
    password_hash2 = hashing.hash("123456")
    print(password_hash2)

    # 判断原始密码是否和密码哈希值是否匹配
    ret = hashing.verify("123455", password_hash1)
    print(ret)
    ret = hashing.verify("123456", password_hash2)
    print(ret)

    # 生成指定长度的随机字符串秘钥
    print(genkey())