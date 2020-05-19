# import random
# def secret_key(num):
#     seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     sa = []
#     for i in range(num):
#         sa.append(random.choice(seed))
#     salt = ''.join(sa)
#     print(salt)
import os

def get_secret_key(num=1):
    result = os.urandom(num)
    print(result)
    return result

# get_secret_key(32)

