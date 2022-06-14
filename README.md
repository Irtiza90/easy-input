# Easy Input
A Simple and Easy to Use Input Parsing Library

# Functions
There are only 4 simple Functions

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

## - `ask_regex`
#### Will Keep asking for input until the input is a matched by a regex pattern, in that case returns the input that matched
#### Takes in 3 arguments

`prompt`: the message to show when asking for input

`pattern`: the regex pattern that matches the input

`message`: The Message to Print out if the validation failed

#### `prompt` and `message` must be of type string, `pattern` can be of type string or re.Pattern

### Returns
The input that matched the regex pattern
