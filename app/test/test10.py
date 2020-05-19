from contextlib import contextmanager
#
#
# class MyResource:
#     # def __enter__(self):
#     #     print('connect to resource')
#     #     return self
#     #
#     # def __exit__(self, exc_type, exc_val, exc_tb):
#     #     print('close resource connection')
#
#     def query(self):
#         print('query data')
#
# # with MyResource() as r:
# #     r.query()
# #把不具备上文协议的对象变成具有上下文协议的对象
# @contextmanager
# def make_resource():
#     print('connect to resource')
#     yield MyResource()
#     print('close resource connection ')
#
#
# with make_resource() as r:
#     r.query()

#打印书名号

# @contextmanager
# def make_book():
#     print('《',end='')
#     yield
#     print('》',end='')
#
# with make_book():
#     print('西游记',end='')



# class A:
#     #用于对象的创建
#     def __new__(cls):
#         return object.__new__(cls)
#     def __init__(self):
#         pass
# a = A()
# print(a)
# from enum import Enum
#
# class VIP(Enum):
#     red = 1
#     green = 2
#     black = 3
#
#
# a = VIP(1)
#
# print(a)
import json
r = {
    'name':'ken',
    'age':19,
    'gender':'女'
}
t = json.dumps(r).encode('utf-8')
print(t)
# from itsdangerous import JSONWebSignatureSerializer as Serializer
#
#
# def generate_token(expiration=600):
#     secret_key = "\xa7\x85[\xe7\x98\xcc\x86V\xcb\xd0\x000\xe8\x12%\xa1>n@\xe4\xb9b\x1e\x9e\x0fF\x05'\xd2pP\x89"
#     s = Serializer(secret_key,expiration)
#     print(s.dumps({'name': "ALEX"}).decode('utf-8'))
# generate_token()