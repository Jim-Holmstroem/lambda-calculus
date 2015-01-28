from __future__ import division, print_function

import operator
import string

from pyparsing import (
    Literal,
    OneOrMore,
    Forward,
    Group,
    Word,
    alphas,
)


def parse_abstraction(abstraction):
    class Abstraction(object):
        def __init__(self, argument, body):
            self.argument = argument
            self.body = body

        def __repr__(self):
            return r"(\{}.{})".format(self.argument, self.body)

        def __str__(self):
            return self.__repr__()


    return Abstraction(abstraction[0], abstraction[1:])


def parser():
    variable = reduce(
        operator.or_,
        map(
            Literal,
            string.ascii_letters
        )
    )
    application = Forward()
    abstraction = (
        Literal('\\').suppress() + variable + Literal('.').suppress() + application
    ).setParseAction(parse_abstraction)
    group = Group(
        Literal('(').suppress() + application + Literal(')').suppress()
    )
    application << OneOrMore(group | abstraction | variable).setParseAction(list)

    return application


tests = [
    "(ab)c",
    "a(bc)",
    "\\a.a",
    "\\b.\\a.ab",
    "abcdef",
    "ab(cd)ef",
]

map(
    lambda test: print(parser().parseString(test)),
    tests
)
