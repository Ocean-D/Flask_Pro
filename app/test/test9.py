from app.forms.auth import LoginForm


class A():
    def __call__(self, *args, **kwargs):
        form = LoginForm()
        if form.validate():
            pass
        pass

    def __str__(self):
        print('This is Start')
        return  "hello"



a = A()
c = str(a)
print(c)
