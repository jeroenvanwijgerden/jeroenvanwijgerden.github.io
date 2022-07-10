class X:

    def __init__(self, y):
        self.y = y

    def foo(self):
        return self.y

x = X(5)

def call(thunk):
    return thunk()

print(call(x.foo))