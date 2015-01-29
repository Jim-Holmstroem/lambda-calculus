from __future__ import division, print_function

import operator
import string

from pyparsing import (
    Literal,
    OneOrMore,
    Forward,
    Group,
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

    return Abstraction(abstraction[0], abstraction[1])


def parse_application(applicants):
    #print("{")
    #map(
    #    lambda app:
    #        print("    {} @{}".format(app, type(app))),
    #    applicants.asList()
    #)
    #print("}")

    class Application(object):
        def __init__(self, applicants):
            self.applicants = applicants

        def __repr__(self):
            return "{}".format(
                ' '.join(map(str, self.applicants))
            )

        def __str__(self):
            return self.__repr__()

    return Application(list(applicants))


def parse_variable(variable):
    class Symbol(object):
        def __init__(self, variable):
            self.variable = variable

        def __repr__(self):
            return "{}".format(self.variable)

        def __str__(self):
            return self.__repr__()

    return Symbol(variable[0])


def parse_group(group):  # FIXME consider renaming parser_*
    class Group(object):
        def __init__(self, group):
            self.group = group

        def __repr__(self):
            return "({})".format(self.group)

        def __str__(self):
            return self.__repr__()

    return Group(group[0][0])


def parser():
    variable = reduce(
        operator.or_,
        map(
            Literal,
            string.ascii_letters
        )
    ).setParseAction(parse_variable)

    application = Forward()
    abstraction = (
        Literal('\\').suppress() + variable
        + Literal('.').suppress() + application
    ).setParseAction(parse_abstraction)
    group = Group(
        Literal('(').suppress() + application + Literal(')').suppress()
    ).setParseAction(parse_group)
    application << (
        OneOrMore(group | abstraction | variable)
    ).setParseAction(parse_application)

    return application


tests = [
    "ab",
    "(ab)c",
    "a(bc)",
    "\\a.a",
    "\\b.\\a.ab",
    "abcdef",
    "ab(cd)ef",
    "\\b.(\\x.x)b",
    "\\f.\\x.f(f(x))",
    "\\c.\\n.(c (\\f.\\x.x) (c (\\f.\\x.f(x)) (c (\\f.\\x.f(f(x))) n)))",
]

map(
    lambda test: print(
        "{}: {}".format(
            test,
            parser().parseString(test)[0]
        )
    ),
    tests
)
