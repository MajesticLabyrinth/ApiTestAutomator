# A context manager is an object that wraps an arbitrary block of code.
# Context managers ensure that setup is consistently performed when the
# context manager is entered, and that teardown is consistently performed when the
# context manager is exited.
# This is probably the most common use of context managers - they are a way to
# ensure cleanup.

class ContextManager(object):
    def __init__(self):
        self.entered = False

    def __enter__(self):
        self.entered = True
        return self

    def __exit__(self, exec_type, exec_instance, traceback):
        self.entered = False


