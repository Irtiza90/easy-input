import re


def ask_int(prompt: str, message=...) -> int:
    while True:
        try:
            inp = int(input(prompt))
        except TypeError:
            print("Expected a number" if not message else message)
        else:
            return inp


def ask_float(prompt: str, message=...) -> float:
    while True:
        try:
            inp = float(input(prompt))
        except TypeError:
            print("Expected a floating point number" if not message else message)
        else:
            return inp


def ask_bool(prompt: str, message=...) -> bool:
    bools = {
        "true": True,
        "True": True,
        "false": False,
        "False": False,
    }

    while True:
        inp: bool | None = bools.get( input(prompt) )

        if inp is not None:
            return inp
        
        print("Expected boolean" if not message else message)


def ask_regex(prompt: str, pattern: str | re.Pattern, message=...) -> str:
    while True:
        inp = input(prompt)

        if re.match(pattern=pattern, string=inp):
            return inp

        print("Expected boolean" if not message else message)

