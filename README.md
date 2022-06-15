# Easy Input
A Simple and Easy to Use Input Parsing Library

# Functions
There are only 5 simple Functions

## - `ask_int`
#### Will Keep asking for input until the input is a valid integer, in that case returns the parsed int

#### Takes in 2 arguments, both of them should be string types
`prompt`: the message to show when asking for input

`message`: The Message to Print out if the validation failed

### Returns
The parsed integer

## - `ask_float`
#### Will Keep asking for input until the input is a valid float, in that case returns the parsed float
Takes in the same arguments as `ask_int`

### Returns
The parsed float

## - `ask_bool`
#### Will Keep asking for input until the input is a valid boolean, in that case returns the parsed boolean
Takes in the same arguments as `ask_int` and `ask_float`

### Returns
The parsed boolean

## - `ask_if_in`
#### Will keep asking for input until the input is found in a given iterable, in that case return the input that was found
The iterable is automatically converted to a set so the lookup time is much faster

The items in the iterable are automatically converted to a string

So `[1, 2.0, print, "hi", True]`

becomes: `["1", "2.0", "print", "hi", "True"]`, so the input can be parsed
<br>
#### Takes in 3 arguments

`prompt`: the message to show when asking for input

`ask_in`: The iterable that will be looked in with given input

`message`: The Message to Print out if the validation failed

### Returns
The input that was found in the iterable


## - `ask_regex`
#### Will Keep asking for input until the input is a matched by a regex pattern, in that case returns the input that matched
#### Takes in 3 arguments

`prompt`: the message to show when asking for input

`pattern`: the regex pattern that matches the input

`message`: The Message to Print out if the validation failed

#### `prompt` and `message` must be of type string, `pattern` can be of type string or re.Pattern

### Returns
The input that matched the regex pattern
