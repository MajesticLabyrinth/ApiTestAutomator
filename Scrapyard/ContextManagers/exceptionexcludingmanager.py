class ValueErrorSubclass(ValueError):
    pass


class HandleValueError(object):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_instance, traceback):
        # Return True if there is no exception.
        if not exc_type:
            return True

        # If this is a ValueError (but not a ValueError subclass),
        # note that it is being handled and return True.
        if exc_type == ValueError:
            print('Handling ValueError: %s' % exc_instance)
            return True

        # Propagate everything else
        return False


with HandleValueError():
    raise ValueErrorSubclass('foo bar bar')


# Here we are catching only a given class of exception, but explicitly not its subclass.from
# This cannot be achieved with the traditional except block, but a context manager is
# able to address such an edge case as shown above.
# We are checking the type using -- rather than the more traditional 'issubclass' check that
# the previous example used. This means that although it will handle 'ValueError' as before,
# it will not handle a 'ValueError' subclass such as the 'ValueErrorSubClass' defined previously.