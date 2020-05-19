from werkzeug.local import LocalStack


s = LocalStack()

s.push(2)
print(s.top)
print(s.top)
print(s.pop())
print(s.pop)
