   ## 1.3.1 expression & operator precedence
"""
    the order of evaluation is from left to right 
    example: 3 - 8 + 5 = 0 ==> ( 3 - 8 )  + 5 
    
    here is the precedence of the operator
    1-  member access ==> expr.member
    2-  call ==> expr(), expr[]
    3-  exponentiation ==> **
    4-  unary plus and minus ==> +expr, -expr
    5-  multiplication, division, and remainder ==> *expr, /expr, %expr
    6-  addition and subtraction ==> +expr, -expr
    7-  left and right bitwise-shifting ==> <<, >>
    8-  bitwise-and ==> &
    9-  bitwise-xor ==> ^
    10- bitwise-or ==> |
    11- comparisons , containment ==> ==, !=, >, <, >=, <=,is, is not, in, not in
    12- logical-not ==> not expr
    13- logical-and ==> and 
    14- logical-or ==> or
    15- conditional expression ==> expr if expr else expr
    16- assignment ==>  = ,  += ,  -= ,  *= ,  /= ,  %= ,  &= ,  |= ,  ^= ,  <<= ,  >>= 
"""

"""
    chained assignment supported in python
    example: 
        x = y = z = 0 ==> x = 0, y = 0 and z = 0
        1 <= x+y <= 10 ==> ( 1 <= x + y ) and ( x + y <= 10 )
"""