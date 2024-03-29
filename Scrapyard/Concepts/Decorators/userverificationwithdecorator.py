# A common use case for this pattern (that is, performing some kind of sanity check before
# running the decorated method) is user verification. Consider a method that is expected to
# take a user as its first argument as shown below -

import functools

class User(object):
    """A representation of a user in our application."""

    def __init__(self, username, email):
        self.username = username
        self.email = email


class AnonymousUser(User):
    """An anonymous user; a stand-in for an actual user that nonetheless is not an actual user."""
    def __init__(self):
        self.username = None
        self.email = None

    def __nonzero__(self):
        return False


# A decorator is a powerful tool here for isolating the boilerplate code of user verification.
# A @requires_user decorator can easily verify that you got a User object

def requires_user(func):
    @functools.wraps(func)
    def inner(user, *args, **kwargs):
        """Verify that the user is truthy; if so, run the decorated method, and if not, raise ValueError."""
        # Ensure that user is truthy, and of the correct type.
        # The "truthy" check will fail on anonymous users, since the
        # AnonymousUser subclass has a '__nonzero__' method that
        # returns False.
        if user and isinstance(user, User):
            return func(user, *args, **kwargs)
        else:
            raise ValueError('A valid user is required to run this.')
        return inner;

    # This decorator applies a common, boilerplate need - the verification  that a user is logged
    # in to the application. When you implement this as a decorator, it is reusable and more
    # easily maintainable, and its application to functions i clear and explicit.

    # Note that this decorator will only correctly wrap a function or static method, and will fail
    # if wrapping a bound method to a class.