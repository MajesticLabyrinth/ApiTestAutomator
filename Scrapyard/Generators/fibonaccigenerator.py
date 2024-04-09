def simplefibonaccigenerator():
    yield 1
    yield 1
    yield 2
    yield 3
    yield 5
    yield 8

# This generator represents the beginning of the Fibonacci sequence (that is, the sequence
# in which each integer is the sum of the previous two). you can iterate generators, as you
# can see by using a simple for...in loop in the Python interactive terminal.

# output of this particular generator is probably better represented as a plain Python list. However,
# consider a generator which, instead of returning six Fibonacci numbers, returns an infinite
# series of them, as shown in the function below -

def genericfibonacci():
    numbers = []
    while True:
        if len(numbers) < 2:
            numbers.append(1)
        else:
            numbers.append(sum(numbers))
            numbers.pop(0)
        yield numbers[-1]

# This generator will yield an infinite sequence of Fibonacci numbers. Using the simple For...in
# from the interactive terminal shown previously would simply print numbers, which very
# quickly become humorously long (that is, to the screen into perpetuity).

# unlike the previous 'simplefibonaccigenerator' function, this one is not better represented
# as a simple Python list. In fact, not only would it be unwise to try to represent this as a
# simple Python list, it would be impossible. Python list cannot store infinite sequences of values.

# The 'next' function
# you can ask a generator for a value without using a for...in loop. Sometimes you may want to just
# get a single value or a fixed number of values. Python provides the built-in next function, which can
# ask a generator (actually, any object with a __next__ method) for its next value.

gen = genericfibonacci()
print('Next (gen) = %' % next(gen))