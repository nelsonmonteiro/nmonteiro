import re
from .models import Function
from .exceptions import ParseException


def parse_function(func):
    functions = Function.objects.all()
    stack = []

    for f in re.findall("f\d+", func):
        stack.append(f)
        try:
            func = func.replace(f, '(%s)' % functions[int(f[1:]) - 1].parse(functions, stack))
        except IndexError as e:
            raise ParseException("Function '%s' doesn't exist." % f)
        del stack[-1]
    return func

