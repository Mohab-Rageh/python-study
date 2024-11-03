## 1.5 Functions

"""
    def function_name(parameters):
        function body
        return ##the end of the function
"""

names = ["Mohab", "Ali", "Ahmed","Ali", "Mohab","Ali"]

def count_target_on_list(data,target):
    count = 0
    for name in data:
        if name == target:
            count += 1
    return count

print("Mohab:", count_target_on_list(names, "Mohab"))
print("Ali:", count_target_on_list(names, "Ali"))

## 1.5.1 information passing
"""
    - the identifiers used to describe the functions are called formal parameters
    - the identifiers used to invoke the functions are called actual parameters
    - parameters passed to functions are assigned to the formal parameters
    
    def count_target_on_list(data,target):
        count = 0
        for name in data:
            if name == target:
                count += 1
        return count
    
    count_target_on_list(names, "Mohab") ==> data = names, target = "Mohab"

    - default parameters can be used to assign default values and the function is called polymorphic function
    
    def foo(a=1, b=2, c=3):
        print(a, b, c)
        
    can be called like this:
    foo()
    foo(10)
    foo(10,20)
    foo(10,20,30)
    
    passing the default parameters to the function is called keyword arguments

    foo(b=8) ==> a = 1, b = 8, c = 3 
    
    another example: python built in range function
    range(10) ==> 0,1,2,3,4,5,6,7,8,9
    range(2,5) ==> 2,3,4
    range(2,10,2) ==> 2,4,6,8
"""

names = ["Mohab"]
name="Ahmed"

def add_item_and_reset_the_item(data, item):
    ## this will modify the original list since we use the mutate state
    data.append(item)
    ## this will reassign the insider data not the original list 
    data=["NewName"]
    ## this will reassign the insider item not the original item
    item="NewItem"
    
    return data, item

internalDataOfTheFunction = add_item_and_reset_the_item(names,name) ## ==> data = names, item = name
## the append will edit the original list 
## the data = [] will reassign the data with new object without edit the original list
## the item = "" will reassign the item with new object without edit the original item


print(internalDataOfTheFunction,names,name)
## we expect to see ["NewName"] and "NewItem" as the internal data of the function
## and ["Mohab","Ahmed"] for the names and "Ahmed" for the name
