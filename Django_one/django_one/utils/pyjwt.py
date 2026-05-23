import sys
import os

# 添加根目录到 sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import jwt
import time
# from django.conf import settings
from django_one.settings import JWT_ALGORITHM,JWT_SECRET,JWT_TOKEN_EXPIRE_TIME
# 'exp': 'token过期时间戳'
def encode_jwt(payload):
   token = jwt.encode({'exp':int(JWT_TOKEN_EXPIRE_TIME+time.time()),**payload}, JWT_SECRET, algorithm=JWT_ALGORITHM)
   return token

def decode_jwt(token):
    payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    return payload

if __name__ == '__main__':
    payload = {
        "email":"123@qq.com",
        "pwd":"123456",
        "sercet":"1234"
    }
    token = encode_jwt(payload)
    print(token)
    print(decode_jwt(token))

