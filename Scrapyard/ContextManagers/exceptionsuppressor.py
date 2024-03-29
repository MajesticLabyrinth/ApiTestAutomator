class SuppressExceptions(object):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_instance, traceback):
        if exc_instance:
            print('Suppressing exception: %s.' % exc_instance)
        return True


with SuppressExceptions():
    print(5 + 5)
    print('Done!')

with SuppressExceptions():
    print(5 / 0)
    print('Done again!')


# The first and most obvious thing to note is that the traceback is gone. The exception was
# handled (suppressed) by the __exit__ method, so program execution continues with no
# exception raised.
# The second thing to note is that no value was ever returned. Whereas the expression 5+5
# when entered into the interpreter, gave a value of 10, the exception-raising 5/0 simply never
# shows a value. The exception was raised in the process of computing a value, which triggered
# the running of __exit__. A value is never actually returned. It is also worth noting that if any
# code was present after 5/0, would never run.