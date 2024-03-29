class HandleValueError(object):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_instance, traceback):
        # Return True if there is no exception.
        if not exc_type:
            return True

        # If this is a ValueError, note that it is being handled and return True.
        if issubclass(exc_type, ValueError):
            print('Handling ValueError: %s' % exc_instance)
            return True
        # Propagate anything else
        return False


with HandleValueError():
    raise ValueError('Wrong value.')

print('Moving to type error.')

with HandleValueError():
    raise TypeError('Wrong type.')


# This context manager ensures that all value errors are suppressed.
# If the error is of type error, it does not get suppressed, instead it gets
# highlighted with the stack trace.