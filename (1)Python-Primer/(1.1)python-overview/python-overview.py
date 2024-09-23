#1.1.1 python interpreter
## python is an interpreted language: commands are executed through a piece of software called the Python interpreter
## to run python file use command: python [filename.py]
## to run python file in interactive mode use command: python -i [filename.py]

#1.1.2 preview of a python program
## python's syntax depends heavily on whitespace individual statements are started by new line and are separated by semicolons  
## commands can be extended to another line  with conclusion of the line with a back slash (\) or if an opened delimiter 
## is not closed with a closing delimiter 
""" 
example: 
    total_sum = 1 + 2 + 3 + 4 + 5 + \
            6 + 7 + 8 + 9 + 10
            
    total_sum = (1 + 2 + 3 + 4 + 5 +
            6 + 7 + 8 + 9 + 10)
"""
## code example:
print("Welcome to GPA calculator")
print("Please enter your grades one per line")
print("Enter a blank line to end input")
points ={
    "A+":4.0,
    "A":4.0,
    "A-":3.67,
    "B+":3.33,
    "B":3.0,
    "B-":2.67,
    "C+":2.33,
    "C":2.0,
    "C-":1.67,
    "D+":1.33,
    "D":1.0,
    "F":0.0
}
num_courses = 0
total_points = 0
done = False

while not done:
        grade = input().upper()
       
        if grade == "":
            done = True
        elif grade not in points:
            print("Invalid grade `{0}` ".format(grade))
        else: 
            num_courses += 1
            total_points += points[grade]
            
if num_courses != 0:
    print("Your GPA is {0:.3}".format(total_points/num_courses))
        