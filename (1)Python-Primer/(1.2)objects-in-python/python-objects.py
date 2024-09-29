# python is an object oriented programming language

## 1.2.1 identifier & object & assignment statements 
temp = 98.6
"""
    - temp is a name or identifier 
    - associated with float object with value 98.6 ( float(98.6))
    - identifier works like reference variable(JAVA) or pinter(C++) which focus on memory address
    - identifier can be assigned to a None object that equals to null 
    - python is dynamically typed language which means that the type of an object can be changed during runtime
"""
## alias assignment
original_temp = temp
"""
    now every time the original temp is changed by a class state change the temp will be changed too and vice versa
    if the temp = temp + 1 the original temp will not be changed but the temp will be reassigned to 99.6
    but if the temp changed by some method on the float object the original temp will be changed too
"""
## 1.2.2 creating and using objects
"""
    - creating objects is called instantiation
    - an object is an instance of a class that created when invoked the class constructor
    - Mohab = Person("Mohab", 24, "male")
    - many python built in class support what called a literal form that can be used to create objects 
    - example: 
        - 99.6 = float(99.6) <= 99.6 is an object of float class which is equal to call the float class constructor
    - functions is supported on python as traditional functions or methods 
    - example:
        - data.sort() (data is an object of list class)
        - word.capitalize() (word is an object of string class)
    - some class methods return info about the object without changing it's states and called accessors
    - some class methods change the object states and called mutators
"""
## 1.2.3 python built in classes
"""
    - bool          (immutable)         literal form: True, False
    - int           (immutable)         literal form: 1, 2, 3
    - float         (immutable)         literal form: 1.0, 2.0, 3.0
    - dict          (mutable)           literal form: {"a": 1, "b": 2, "c": 3} " empty dict represented by dict() or {} "
    - set           (mutable)           literal form: {1, 2, 3} " empty set represented by set()  not {} " set accept only immutable objects
    - frozen set    (immutable) 
    
    \\ sequence types (used when order is important)
    - str           (immutable)         literal form: "hello", "world"
    - tuple         (immutable)         literal form: (1, 2, 3) " tuple class is immutable class of list " if want to create a tuple with length 1 use (1,)
    - list          (mutable)           literal form: [1, 2, 3] " list class is a sequence of references to objects "
    
    - immutable means that once an object is created it cannot be changed
    - mutable means that once an object is created it can be changed
    - example:
        - temp = 99.6
        - temp += 1
        - now temp = 100.6 (it changed by creating new float object with value 100.6, not by changing the value of 99.6)
        - so if temp1 = temp2 = 99.6 => now temp1 have reference to 99.6 and temp2 have reference to 99.6 
        - if we make temp2 = temps2 + 1 => now temp2 have reference to 100.6 and temp1 have reference to 99.6 
    - 
"""