## 1.4.1 conditions in python
"""
    if first_condition:
        statement
    elif second_condition:
        statement
    else:
        statement
"""
door_is_closed = True
door_is_locked = True

if door_is_closed:
    if door_is_locked:
        print("The door is locked")
    print("The door is closed")
print("other code to execute")     

## 1.4.2 loops in python
"""
    while condition:
        statement
        
    for item in iterable:
        statement
        
    for index in range(len(iterable)):
        statement
        
    python supports break and continue
    break: exit the loop
    continue: skip to the next item in the loop
"""

names = ["Alice", "Bob", "Charlie","Mohab","ayman"]
j=0

## print all names that before Mohab
print("-------------- While Loop --------------")
while j < len(names) and names[j] != "Mohab":
    print(names[j])
    j+=1
    
print("-------------- for each element in loop --------------")
for name in names:
    if name == "Mohab":
        break
    print(name)
    
print("-------------- for index in loop --------------")
for j in range(len(names)):
    if names[j] == "Mohab":
        break
    print(names[j])
    
## break and continue
print("-------------- Break Loop When Mohab found (stop the for loop) --------------")
for name in names:
    if name == "Mohab":
        break
    print(name)

print("-------------- Continue Loop When Mohab found (skip to the next item in the loop) --------------")
for name in names:
    if name == "Mohab":
        continue
    print(name)
