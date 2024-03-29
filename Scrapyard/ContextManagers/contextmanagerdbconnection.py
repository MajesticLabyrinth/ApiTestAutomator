import psycopg2

class DBConnection(object):
    def __init__(self, dbname=None, user=None, password=None, host='localhost'):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password

    def __enter__(self):
        self.connection = psycopg2.connect(dbname=self.dbname,
                                           host = self.host,
                                           user = self.user,
                                           password=self.password)
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_instance, traceback):
        self.connection.close()




# The xontext manager creates a psycopg2 connection object and returns a cursor,
# which the developer can use to interact with the database. What is important
# here, though, is that the connection is guaranteed to be closed when the
# context manager exits.
# This is important because, as mentioned, lingering database connections not only
# consume memory, but they also open files or ports on both the application
# machine and database machine. Additionally, some databases also have maximum
# connection allowances.
# Note also that, unlike the previous example, this context manager does not simply
# return itself at the end of the __enter__ method. Instead, it returns a database cursor.
# This is fine, and a useful paradigm. However, it is still the context manager's
# __exit__ method that runs.
# most frameworks that work with databases handle opening and closing your database
# connections for you, but this principle remains: if you are opening a resource and must
# ensure that it is being properly closed, a context manager is an excellent tool.