
from flask import Flask,current_app,Request,request


app = Flask(__name__)
#应用上下文 对象 Flask
#请求上下文 请求 Request
#Flask AppContext
#Request RequestContext
#app_context()返回一个应用上下文，使用with就可以我们不需要手动的推入栈
ctx = app.app_context()
ctx.push()
a = current_app

b = current_app.config['DEBUG']
ctx.pop()

# with app.app_context():
#     a = current_app
#     b = current_app.config['DEBUG']
#
# with open('fielname') as f:
#     f.read()
import re

str1 = '(百度)www.baidu.com'
r = re.match('\(百度\)(.*)',str1)
print(r.group(1))
