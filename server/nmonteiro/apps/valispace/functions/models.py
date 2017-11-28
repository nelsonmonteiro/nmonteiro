import re
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .exceptions import ParseException


@python_2_unicode_compatible
class Function(models.Model):
    class Meta:
        ordering = ['id']

    syntax = models.CharField(max_length=255)

    def parse(self, functions=None, stack=None):
        """
        :param functions: List of functions. Use the variable instead getting all the time for performance.
        :param stack: List of functions already parsed inside of the context. To prevent self-recursion.
        :return: Parsed function
        """
        # Set initial values for functions and sta

        if not functions:
            functions = Function.objects.all()

        if not stack:
            stack = []

        func = self.syntax
        for f in re.findall("f\d+", func):
            if f in stack:
                raise ParseException('Self-recursion found!')

            stack.append(f)
            try:
                func = func.replace(f, '(%s)' % functions[int(f[1:])-1].parse(functions, stack))
            except IndexError as e:
                raise ParseException("Function '%s' doesn't exist." % f)
            del stack[-1]
        return func

    def __str__(self):
        return self.syntax

