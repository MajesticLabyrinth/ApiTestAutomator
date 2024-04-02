import subprocess

class ShellException(Exception):
    def __init__(self, code, stdout='', stderr=' '):
        self.code = code
        self.stdout = stdout
        self.stderr = stderr

    def __str__(self):
        return 'exit code %d - %s' % (self.code, self.stderr)


def run_command(command):
    # Run the command and wait for it to complete.
    proc = subprocess.Popen(command.split(' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.wait()

    # Get the stdout and stderr from the shell.
    stdout, stderr = proc.communicate()

    # Sanity check : If the shell returned a non-zero exit status, raise an exception.
    if proc.returncode > 0:
        raise ShellException(proc.returncode, stdout, stderr)

    # Return stdout.
    return stdout


run_command('rm bogusfile')