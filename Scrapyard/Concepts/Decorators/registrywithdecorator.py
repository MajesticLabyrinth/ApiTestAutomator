class registry(object):
    def __init__(self):
        self._functions = []

    def register(self, decorated):
        self._functions.append(decorated)
        return decorated

    def run_all(self, *args, **kwargs):
        return_values = []
        for func in self._functions:
            return_values.append(func(*args, **kwargs))
        print(return_values)
        return return_values


#if __name__ == '__main__':
a = registry()
b = registry()

@a.register
def foo(x=3):
    return x
@b.register
def bar(x=5):
    return x
@a.register
@b.register
def baz(x=7):
    return x

a.run_all()
b.run_all()
print('----------')
a.run_all(x=4)