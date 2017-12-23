# base36
*base36* is a python class to be used for a base-36 number system. The characters
used are 0-9 followed by A-Z.

*base62* is identical to the base-36 number system except with more characters. The characters
used are 0-9 followed by uppercase A-Z and then lowercase a-z

## operators
the base36 and base62 classes are compatible with the following operators:
- `init`: Initialization  
- `str`: Convert to string for output
- `add`: Addition using (+)
- `sub`: Subtraction using (-)
- `mul`: Multiplication using (\*)
- `div`: Division using (/)
- `mod`: Modulus using (%)
- `len`: Returns number of characters in the number when using len()
- `getitem`: Returns character at given array index (ex: base36[index] )
- `lt`: Less than (<)
- `le`: Less than or equal to (<=)
- `eq`: Equal to (==)
- `ne`: Not equal (!=)
- `ge`: Greater than or equa to (>=)
- `gt`: Greater than (>)
