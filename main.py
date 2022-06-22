import re
from typing import Iterable


# TODO: ASK input is in iterable

def ask_int(prompt: str, message: str = None) -> int:
    """
    Asks an integer

    :param prompt: the prompt to show when asking input
    :param message: the message that will be printed if input is invalid
    :returns: int
    """
    while True:
        try:
            inp = int(input(prompt))
        except ValueError:
            print("Expected a number" if not message else message)
        else:
            return inp


def ask_float(prompt: str, message: str = None) -> float:
    """
    Asks an Float

    :param prompt: the prompt to show when asking input
    :param message: the message that will be printed if input is invalid
    :returns: float
    """
    while True:
        try:
            inp = float(input(prompt))
        except ValueError:
            print("Expected a floating point number" if not message else message)
        else:
            return inp


def ask_bool(prompt: str, message: str = None) -> bool:
    """
    Asks an Boolean

    :param prompt: the prompt to show when asking input
    :param message: the message that will be printed if input is invalid
    :returns: bool
    """

    bools = {
        "true": True,
        "True": True,
        "false": False,
        "False": False,
    }

    while True:
        inp: bool | None = bools.get(input(prompt))

        if inp is not None:
            return inp
        
        print("Expected boolean" if not message else message)


def ask_if_in(prompt: str, ask_in: Iterable, message: str = None, *, auto_convert: bool = True) -> str:
    """
    Will Keep asking for input until it is found in the iterable
    
    The items in the iterable are automatically converted to a string\n
    So [1, 2.0, print, "hi", True]\n
    becomes: ["1", "2.0", "print", "hi", "True"], so the input can be parsed

    :param prompt: the prompt to show when asking input
    :param ask_in: checks if the input given is in the iterable
    :param message: the message that will be printed if input is invalid
    :param auto_convert: keyword only argument if it's False will not convert ask_in to a set
    :returns: the input string that was found in the iterable
    """
    if auto_convert is True and isinstance(ask_in, str) is False:
        ask_in = {f"{item}" for item in ask_in}
    

    while True:
        inp = input(prompt)

        if inp in ask_in:
            return inp

        print("Invalid Input" if not message else message)


def ask_regex(prompt: str, pattern: str | re.Pattern, message: str = None) -> str:
    """
    Will Keep asking for input until it matches regex

    :param prompt: the prompt to show when asking input
    :param pattern: The regex pattern that will be matched
    :param message: the message that will be printed if input is invalid
    :returns: the input string that matched the regex pattern
    """
    while True:
        inp = input(prompt)

        if re.match(pattern=pattern, string=inp):
            return inp

        print("Invalid Input" if not message else message)

