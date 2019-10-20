Python has several built-in functions associated with the string data type. These functions let us easily modify and manipulate strings. We can think of functions as being actions that we perform on elements of our code. Built-in functions are those that are defined in the Python programming language and are readily available for us to use.

The functions str.upper() and str.lower() will return a string with all the letters of an original string converted to upper- or lower-case letters. Because strings are immutable data types, the returned string will be a new string. Any characters in the string that are not letters will not be changed.

Python has some string methods that will evaluate to a Boolean value.
str.isalnum() :	String consists of only alphanumeric characters (no symbols)
str.isalpha()	: String consists of only alphabetic characters (no symbols)
str.isnumeric() : String consists of only numeric characters

Determining String Length
The string method len() returns the number of characters in a string. This method is useful for when you need to enforce minimum or maximum password lengths, for example, or to truncate larger strings to be within certain limits for use as abbreviations.

The str.join() method will concatenate two strings, but in a way that passes one string through another.

The str.split() method returns a list of strings that are separated by whitespace if no other parameter is given.
We can also use str.split() to remove certain parts of an original string.

The str.replace() method can take an original string and return an updated string with some replacement.



Python String capitalize() : Converts first character to Capital Letter
Python String center() :	Pads string with specified character
Python String casefold() :	converts to casefolded strings
Python String count() :	returns occurrences of substring in string
Python String endswith() :	Checks if String Ends with the Specified Suffix
Python String expandtabs() :	Replaces Tab character With Spaces
Python String encode() :	returns encoded string of given string
Python String find() :	Returns the index of first occurrence of substring
Python String format() :	formats string into nicer output
Python String index() : Returns Index of Substring
Python String isalnum() :	Checks Alphanumeric Character
Python String isalpha()	: Checks if All Characters are Alphabets
Python String isdecimal()	: Checks Decimal Characters
Python String isdigit()	: Checks Digit Characters
Python String isidentifier() :	Checks for Valid Identifier
Python String islower()	Checks if all Alphabets in a String are Lowercase
Python String isnumeric()	: Checks Numeric Characters
Python String isprintable()	: Checks Printable Character
Python String isspace()	: Checks Whitespace Characters
Python String istitle()	: Checks for Titlecased String
Python String isupper()	: returns if all characters are uppercase characters
Python String join()	: Returns a Concatenated String
Python String ljust()	: returns left-justified string of given width
Python String rjust()	: returns right-justified string of given width
Python String lower()	: returns lowercased string
Python String upper()	: returns uppercased string
Python String swapcase() :	swap uppercase characters to lowercase; vice versa
Python String lstrip() : Removes Leading Characters
Python String rstrip() : Removes Trailing Characters
Python String strip()	: Removes Both Leading and Trailing Characters
Python String partition() :	Returns a Tuple
Python String maketrans()	: returns a translation table
Python String rpartition()	: Returns a Tuple
Python String translate()	: returns mapped charactered string
Python String replace()	: Replaces Substring Inside
Python String rfind()	: Returns the Highest Index of Substring
Python String rindex()	: Returns Highest Index of Substring
Python String split()	: Splits String from Left
Python String rsplit()	: Splits String From Right
Python String splitlines() :	Splits String at Line Boundaries
Python String startswith() :	Checks if String Starts with the Specified String
Python String title() :	Returns a Title Cased String
Python String zfill() :	Returns a Copy of The String Padded With Zeros
Python String format_map() :	Formats the String Using Dictionary
Python any() :	Checks if any Element of an Iterable is True
Python all() :	returns true when all elements in iterable is true
Python ascii() :	Returns String Containing Printable Representation
Python bool() :	Converts a Value to Boolean
Python bytearray() :	returns array of given byte size
Python bytes() :	returns immutable bytes object
Python compile() :	Returns a Python code object
Python complex() :	Creates a Complex Number
Python enumerate() :	Returns an Enumerate Object
Python filter() :	constructs iterator from elements which are true
Python float() :	returns floating point number from number, string
Python input() :	reads and returns a line of string
Python int() :	returns integer from a number or string
Python iter()	: returns iterator for an object
Python len()	: Returns Length of an Object
Python max()	: returns largest element
Python min()	: returns smallest element
Python map()	: Applies Function and Returns a List
Python ord()	: returns Unicode code point for Unicode character
Python reversed() :	returns reversed iterator of a sequence
Python slice() :	creates a slice object specified by range()
Python sorted() :	returns sorted list from a given iterable
Python sum() :	Add items of an Iterable
Python zip() :	Returns an Iterator of Tuples
