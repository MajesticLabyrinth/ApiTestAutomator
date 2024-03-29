registry = []

def register(decorated):
    registry.append(decorated)
    return decorated

# The register method is a simple decorator. It appends the positional argument,
# decorated to the registry variable, and then returns the decorated method
# unchanged. Any method that receives the register decorator will have itself
# appended to the registry.

@register
def foo():
    return 3

@register
def bar():
    return 5

if __name__=='__main__':
    foo()
    bar()
    print(registry)
    answers = []
    for func in registry:
        answers.append(func())
    print(answers)