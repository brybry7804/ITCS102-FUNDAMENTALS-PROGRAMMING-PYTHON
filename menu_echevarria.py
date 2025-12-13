#def function

full_name = input("\n\t\t\tEnter your full name: ")
print(f"\n\t\tHi,{full_name} Welcome to my Python Interactive Menu Program\n")

def main_menu_program():
    print("\t\t\t\t\t\t-------------------------------------------")
    print("\t\t\t\t\t\t-------------------------------------------")
    print("\t\t\t\t\t\t|         Hi! this is Bry Echevarria      |")
    print("\t\t\t\t\t\t|               from BSIT-1A              |")
    print("\t\t\t\t\t\t-------------------------------------------")
    print("\t\t\t\t\t\t-------------------------------------------")
    print("\t\t\t\t\t\t|      Welcome To My Python Interactive   |")
    print("\t\t\t\t\t\t|               Menu Program              |")
    print("\t\t\t\t\t\t-------------------------------------------")
    print("\t\t\t\t\t\t-------------------------------------------")
    print("\t\t\t\t\t\t|     Python Interactive Menu Program     |")
    print("\t\t\t\t\t\t-------------------------------------------")
    print("\t\t\t\t\t\t|       |1| ===>| Print Statement |       |")
    print("\t\t\t\t\t\t|       |2| ===>|    Variables    |       |")
    print("\t\t\t\t\t\t|       |3| ===>|    Operators    |       |")
    print("\t\t\t\t\t\t|       |4| ===>|    Conditions   |       |")
    print("\t\t\t\t\t\t|       |5| ===>|      Loops      |       |")
    print("\t\t\t\t\t\t|       |6| ===>|      Lists      |       |")
    print("\t\t\t\t\t\t|       |7| ===>|    Functions    |       |")
    print("\t\t\t\t\t\t|       |0| ===>|       Exit      |       |")
    print("\t\t\t\t\t\t-------------------------------------------")

def sub_menu_print_statements():
    while True:
        print("\t\t\t\t\t\t-------------------------------------------")
        print("\t\t\t\t\t\t|            Print Statements             |")
        print("\t\t\t\t\t\t-------------------------------------------")
        print("\t\t\t\t\t\t|      |1| ===>|    Simple Print   |      |")
        print("\t\t\t\t\t\t|      |2| ===>|   Concatenation   |      |")
        print("\t\t\t\t\t\t|      |3| ===>|   Format String   |      |")
        print("\t\t\t\t\t\t|      |4| ===>| Printing Variable |      |")
        print("\t\t\t\t\t\t|      |5| ===>|   Printing Lists  |      |")
        print("\t\t\t\t\t\t|      |6| ===>| Escape Characters |      |")
        print("\t\t\t\t\t\t|      |7| ===>|     Sep and End   |      |")
        print("\t\t\t\t\t\t|      |0| ===>|        Back       |      |")
        print("\t\t\t\t\t\t-------------------------------------------")

        print_statements = input("\nEnter a number to execute a program: ")
        
        if print_statements == "1":
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |                This a process of Sample Print              |")
            print("\t\t\t\t      --------------------------------------------------------------")

            #Basic Output
            data = input("\nEnter you want to print: ")

            #Result
            print(f"\n{data}")

            #Explanation
            print("\nProcess: Just printing what you want to input.")
            
            done_print = input("\nY or N if you want to continue: ").lower()
            if done_print == "y":
                continue
            else:
                break
                
        elif print_statements == "2":
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |               This a process of Concatenation              |")
            print("\t\t\t\t      --------------------------------------------------------------")

            #Concatenation
            name2 = input("\nEnter your Name: ")
            age1 = int(input("\nEnter your Age: "))
            status = input("\nEnter your status: ")

            #Result
            print("\nMy name is",name2,"and I am",age1,"years old.","and I am",status)

            #Explanation
            print("\nProccess: Using Concatenation to combine strings and variables like 'Name' + 'Age' + 'Status'")
            
            done_concatenation = input("\nY or N if you want to continue: ").lower()
            if done_concatenation == "y":
                continue
            else:
                break
                     
        elif print_statements == "3":
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |             This a process of Formatting Strings           |")
            print("\t\t\t\t      --------------------------------------------------------------")

            #Formatting String
            name3 = input("\nEnter your Name: ")
            age2 = input("\nEnter your Age: ")

            #Result
            print(f"\nMy name is {name3} and I am {age2} years old.")

            #Explanation
            print("\nProcess: Instead of Concatenation 'Name' + 'Age', in front of (f"")")
            print("it uses 'f' or the format string to insert variable into a string.")
            
            done_formatting_string = input("\nY or N if you want to continue: ").lower()
            if done_formatting_string == "y":
                continue
            else:
                break
            
        elif print_statements == "4":
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |             This a process of Printing Variables           |")
            print("\t\t\t\t      --------------------------------------------------------------")

            #Data Types
            print("\nYou will enter different types of Data Types")
            print("\nStrings: Name, Hobby\nInteger: Age, Balance\nFloat: Grades.")

            #Inputs
            name4 = input("\nEnter a Name: ")
            hobby1 = input("\nEnter your hobby: ")
            age3 = int(input("\nEnter your Age: "))
            balance1 = int(input("\nEnter the Amount of money: "))
            grades1 = float(input("\nEnter your current average grade: "))

            #Results
            print("\nName:",name4,"\nHobby:",hobby1,"\nAge:",age3,"years old.","\nBalance:",balance1,"\nGrades:",grades1)

            #Explanation
            print("\nProcess: Data Types define the kind of data a variable can hold, such as strings, integers, and floats.")

            done_datatypes = input("\nY or N if you want to continue: ").lower()
            if done_datatypes == "y":
                continue
            else:
                break
                
        elif print_statements == "5":
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |               This a process of Printing Lists             |")
            print("\t\t\t\t      --------------------------------------------------------------")
            #Lists
            n = int(input("\nHow many numbers? "))
            my_list1 = []
            for i in range(n):
                num = int(input(f"\nEnter number {i+1}: "))
                my_list1.append(num)
                print("\nList elements:", my_list1)
                print("\nProcess: List is for storing data and make it like a list or a group of data.")
            
            done_list = input("\nY or N if you want to continue: ").lower()
            if done_list == "y":
                continue
            else:
                break
                
        elif print_statements == "6":
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |             This a process of Escape Characters            |")
            print("\t\t\t\t      --------------------------------------------------------------")
            
            #This section is for the R Strings or the special characters
            backslash = (r"\ "[:-1])
            print(f"\nNew Line:          {backslash}n")
            print(f"\nTab character:     {backslash}t")
            print(f"\nSpecial Character: {backslash}u03A9")
            print(f"\nProcess: These Escape Characters are use {backslash}n for newline, {backslash}t for tab, and {backslash}{backslash} for a literal backslash.")
            
            done_R_Strings = input("\nY or N if you want to continue: ").lower()
            if done_R_Strings == "y":
                continue
            else:
                break
                
        elif print_statements == "7":
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |                This a process of Sep and End               |")
            print("\t\t\t\t      --------------------------------------------------------------")

            print("Enter 3 words to join with custom separator and ending.")

            #Inputs
            word1 = input("Word 1: ")
            word2 = input("Word 2: ")
            word3 = input("Word 3: ")
            sep = input("Separator (Ex.' ', ',', '-', ':'): ")
            end = input("Ending text (Ex. Go! etc.): ")

            #Results
            print("\nResult:")
            print(word1, word2, word3, sep=sep, end=end + "\n")

            #Explanation
            print ("\nProcess: Sep parameter controls how items are separated within single print() statement.")
            print ("\nThe End parameter (end=' ') identified by whitespace and not a newline.")

            done_parameter = input("\nY or N if you want to continue: ").lower()
            if done_parameter == "y":
                continue
            else:
                break
                
        elif print_statements == "0":
            print("\nBack to Main Menu")
            break
            
        else:
            #Prevents errors
            print("\nInvalid!, Please select a number: ")

def sub_menu_variables():
    while True:
        print("\t\t\t\t\t ----------------------------------------------------------")
        print("\t\t\t\t\t |                        Variables                       |")
        print("\t\t\t\t\t ----------------------------------------------------------")
        print("\t\t\t\t\t |   |1| ===>|           String Concatenation         |   |")
        print("\t\t\t\t\t |   |2| ===>|     Simple Arithmetic Calculations     |   |")
        print("\t\t\t\t\t |   |3| ===>|        Function with Variables         |   |")
        print("\t\t\t\t\t |   |4| ===>| Dictionary Manipulation with Variables |   |")
        print("\t\t\t\t\t |   |0| ===>|                Back                    |   |")
        print("\t\t\t\t\t ----------------------------------------------------------")

        variables = input("\nEnter a number to execute a program: ")
        
        if variables == "1":
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |           This a process of String Concatenation           |")
            print("\t\t\t\t      --------------------------------------------------------------")

            #Input of a string concatenation
            first_name = input("Enter your First Name: ")
            middle_name = input("Enter your Middle Name: ")
            last_name = input("Enter your Last Name: ")

            #Concatenation
            full_name = first_name + " " + middle_name + " " + last_name

            #Result
            print("\nFull Name: ", full_name)

            #Explanation
            print("\nProcess: String Concatenation in python allows us to combine two or more strings into one.")
            print("\nExample: first_name + middle_name + last_name")
            
            done_string_concatenation = input("\nY or N if you want to continue: ").lower()
            if done_string_concatenation == "y":
                continue
            else:
                break
                
        elif variables == "2":
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |          This a process of Arithmetic Operations           |")
            print("\t\t\t\t      --------------------------------------------------------------")

            #Addition Assignment Operators
            print("\nSample Addition Assignment Operators '+' add.")
            num1 = int(input("\nEnter a first number: "))
            num2 = int(input("Enter a second number: "))

            #Formula
            result = num1 + num2

            #Result
            print("\nThe sum is: ", result)

            #Explanation
            print("\nProcess: The Python Operators are used to perform operations on values and variables.") 
            print("These are the special symbols that carry out arithmetic, logical, and bitwise computations.")
            print("The value the operator operates on is known as the Operand.")
            
            #Python Operators
            print("\nOther Python Operators:")
            print("\nAssignment Operator:                   =")
            print("\nAddition Assignment Operator:          +")
            print("\nSubtraction Assignment Operator:       -")
            print("\nMultiplication Assignment Operator:    *")
            print("\nDivision Assignment Operator:          /")
            print("\nModulus Assignment Operator:           %")
            print("\nFloor Division Assignment Operator:    //")
            print("\nExponentiation Assignment Operator:    **")
            
            done_operators = input("\nY or N if you want to continue: ").lower()
            if done_operators == "y":
                continue
            else:
                break
                
        elif variables == "3":
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |          This a process of Function and Variables          |")
            print("\t\t\t\t      --------------------------------------------------------------")

            #Function that takes args
            def calculation(length,width):
                return length * width

            #Assignment Operators values to variables
            length = int(input("Enter a length: "))
            width = int(input("Enter a width: "))

            #Call the function and store
            area = calculation(length,width)
            print("\nArea:",area)

            #Explanation
            print("\nProcess: The def keyword is used to define a function. Functions are reusable blocks of code")
            print("that can perform specific tasks.")
            print("\nExample: def function_name(parameter):")
            print("\t\treturn parameter")
            
            done_funcOperators = input("\nY or N if you want to continue: ").lower()
            if done_funcOperators == "y":
                continue
            else:
                break
                
        elif variables == "4":
            #Addition Assignment Operators
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |  This a process of Dictionary Manipulation with Variables  |")
            print("\t\t\t\t      --------------------------------------------------------------")

            #Can make Dictionary
            student = {'name': 'Bry Echevarria', 'age': 21, 'major': 'BS in Information Technology'}

            #Can access this dict and can modify wherever it is.
            original_name = 'name'
            original_age = 'age'
            original_major = 'major'
            print("\nOriginal Dict: ",student)

            #Updating Dictionary
            updated_name = input("\nUpdate your Name: ")
            updated_age = input("\nUpdate your Age: ")
            updated_major = input("\nUpdate your Major: ")
            student[original_name] = updated_name
            student[original_age] = updated_age
            student[original_major] = updated_major
            print("\nEdited Dict: ", student)

            #Explanation
            print("\nProcess: A dictionary in Python is a collection of key-value pairs, where")
            print("each key is unique and maps to a specific value. This data structure is highly")
            print("efficient for data retrieval and manipulation, making it a fundamental tool in Python programming.")
            
            done_dict = input("\nY or N if you want to continue: ").lower()
            if done_dict == "y":
                continue
            else:
                break
                
        elif variables == "0":
            print("\nBack to Main Menu")
            break
        else:
            #Prevent errors
            print("\nInvalid!, Please select a number: ")

def sub_menu_operators():
    while True:
        print("\t\t\t\t\t\t-------------------------------------------")
        print("\t\t\t\t\t\t|               Operators                 |")
        print("\t\t\t\t\t\t-------------------------------------------")
        print("\t\t\t\t\t\t|    |1| ===>|   Logical Operator  |      |")
        print("\t\t\t\t\t\t|    |2| ===>| Comparison Operator |      |")
        print("\t\t\t\t\t\t|    |3| ===>| Assignment Operator |      |")
        print("\t\t\t\t\t\t|    |4| ===>|  Identity Operator  |      |")
        print("\t\t\t\t\t\t|    |0| ===>|        Back         |      |")
        print("\t\t\t\t\t\t-------------------------------------------")

        operators = input("\nEnter a number to execute a program: ")
        
        if operators == "1":
            #Logical Operator
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |         This a process of Addition Logical Operator        |")
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\nLogical Operators: AND, OR, NOT")

            #Get user input simple True/False only
            a = input("\nEnter value for a (True/False): ").strip().title() == "True"
            b = input("Enter value for b (True/False): ").strip().title() == "True"

            print(f"\nYou chose: a = {a}, b = {b}")

            # AND
            print("\nAND")
            print(f"a and b = {a and b}")

            # OR
            print("\nOR")
            print(f"a or b  = {a or b}")

            # NOT
            print("\nNOT")
            print(f"not a   = {not a}")
            print(f"not b   = {not b}")

            #Explanation
            print("\nProcess: Logical operators AND, OR, and NOT let us combine or")
            print("reverse true/false conditions and requires both sides to be")
            print("true, or needs at least one side true, and not simply flips true to false or false to true.")
                
            done_logicals = input("\nY or N if you want to continue: ").lower()
            if done_logicals == "y":
                continue
            else:
                break
                
        elif operators == "2":
            #Comparison Operators
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |       This a process of Addition Comparison Operator       |")
            print("\t\t\t\t      --------------------------------------------------------------")
            print("Comparison Operator")

            #Inputs
            x = float(input("Enter first number for x: "))
            y = float(input("Enter second number for y: "))

            #Results
            print(f"\nx = {x}, y = {y}")

            #Process
            if x > y:
                print("\nx is greater than y.")
            elif x < y:
                print("\nx is less than y.")
            else:
                print("\nx is equal to y.")

            #Explanation
            print("\nThis code lets the user input two numbers")
            print("and instantly compares them showing whether")
            print("the first is greater than, less than, or equal")
            print("to the second using simple if/elif/else logic")
            print("with Comparison Operators (>, <, ==).")
                
            done_comparison = input("\nY or N if you want to continue: ").lower()
            if done_comparison == "y":
                continue
            else:
                break
                
        elif operators == "3":
            #Addition Assignment Operators
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |       This a process of Addition Assignment Operator       |")
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\nSample Addition Assignment Operators '+' add.")

            #Inputs
            num1 = int(input("\nEnter a first number: "))
            num2 = int(input("Enter a second number: "))

            #Formula
            result = num1 + num2

            #Result
            print("\nThe sum is: ", result)

            #Explanation
            print("\nProcess: The Python Operators are used to perform operations on values and variables.") 
            print("These are the special symbols that carry out arithmetic, logical, and bitwise computations.")
            print("The value the operator operates on is known as the Operand.")
            print("\nOther Python Operators:")
            print("\nAssignment Operator:                   =")
            print("\nAddition Assignment Operator:          +")
            print("\nSubtraction Assignment Operator:       -")
            print("\nMultiplication Assignment Operator:    *")
            print("\nDivision Assignment Operator:          /")
            print("\nModulus Assignment Operator:           %")
            print("\nFloor Division Assignment Operator:    //")
            print("\nExponentiation Assignment Operator:    **")
            
            done_assignment = input("\nY or N if you want to continue: ").lower()
            if done_assignment == "y":
                continue
            else:
                break
                
        elif operators == "4":
            #Identity Operator
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |             This a process of Identity Operator            |")
            print("\t\t\t\t      --------------------------------------------------------------")
            print("Identity Operator: is / is not")

            #Variables
            x = [1, 2, 3]
            y = [1, 2, 3]
            z = x  # z points to the SAME object as x

            #Process
            print("\nx =", x)
            print("y =", y)
            print("z = x")

            #Results
            print("\nx is y ?     ", x is y)      # False — same values, different objects
            print("x is z ?     ", x is z)      # True  — same object
            print("x is not y ? ", x is not y)  # True

            print(f"\nx = {x}")
            print(f"y = {y}")
            print(f"\nValues equal? {x == y}")
            print(f"Same object?  {x is y}")
            print(f"Different objects? {x is not y}")

            #Explanation
            print("\nThe is and is not operators check whether two variables refer")
            print("to the exact same object in memory not just equal values. For")
            print("example, x = [1,2,3] and y = [1,2,3] have equal contents")
            print("(x == y is True) but are different objects (x is y is False),")
            print("(x == y is True) but are different objects (x is y is False),")
            print("whereas z = x makes z and x point to the same list (x is z is True).")

            done_identityOp = input("\nY or N if you want to continue: ").lower()
            if done_identityOp == "y":
                continue
            else:
                break
                
        elif operators == "0":
            print("\nBack to Main Menu")
            break
        else:
            #Prevent errors
            print("\nInvalid!, Please select a number: ")

def sub_menu_conditions():
    while True:
        print("\t\t\t\t      --------------------------------------------------------------")
        print("\t\t\t\t      |                          Conditions                        |")
        print("\t\t\t\t      --------------------------------------------------------------")
        print("\t\t\t\t      |   |1| ===>|         Simple If-Else Statement           |   |")
        print("\t\t\t\t      |   |2| ===>|         Nested If-Else Statement           |   |")
        print("\t\t\t\t      |   |3| ===>|          If-Elif-Else Statement            |   |")
        print("\t\t\t\t      |   |4| ===>| Multiple Conditions with Logical Operators |   |")
        print("\t\t\t\t      |   |0| ===>|                  Back                      |   |")
        print("\t\t\t\t      --------------------------------------------------------------")

        conditions = input("\nEnter a number to execute a program: ")
        
        if conditions =="1":
            #If Else Statement
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |             This a process of If-Else Statement            |")
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\nIn If-Else shows if the number is Even or Odd.")

            #Inputs
            num = int(input("\nEnter a number: \n"))

            #Process
            if num % 2 == 0:
                print(num, "is Even.")
            else:
                print(num, "is Odd.")
            
            #Explanation
            print("\nThe if-else statement runs one block of code when a condition")
            print("is True, and another when it's False enabling decisions in your")
            print("program. In this example, it chooses between printing 'is Even'")
            print("or 'is Odd' based on whether num % 2 == 0 is true.")

            done_ifEl = input("\nY or N if you want to continue: ").lower()
            if done_ifEl == "y":
                continue
            else:
                break   
                
        elif conditions == "2":
            #Nested If-else Statement
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |         This a process of Nested If-Else Statement         |")
            print("\t\t\t\t      --------------------------------------------------------------")

            #Input
            num = float(input("Enter a number: "))

            #Process
            if num > 0:
                print(num, "is Positive.")
            else:
                if num < 0:
                    print(num, "is Negative.")
                else:
                    print(num, "is Zero.")

            #Explanation
            print("\nProcess: This is a nested if-else statement is the first if checks")
            print("if the number is positive then if not, it goes into the else block,")
            print("where another if-else checks for negative or zero showing how")
            print("decisions can be layered step by step.")
                
            done_nestedIf = input("\nY or N if you want to continue: ").lower()
            if done_nestedIf == "y":
                continue
            else:
                break  

        elif conditions == "3":
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |          This a process of If-Elif-Else Statement          |")
            print("\t\t\t\t      --------------------------------------------------------------")

            #Input
            score = float(input("\nEnter your score (0-100): "))

            #Process
            if score >= 90:
                grade = 'A'
            elif score >= 80:
                grade = 'B'
            elif score >= 75:
                grade = 'C'
            elif score >= 70:
                grade = 'D'
            else:
                grade = 'F'
            
            #Result
            print("\nYour grade is:", grade)

            #Explanation
            print("\nThis code uses an if-elif-else chain to assign a letter grade")
            print("based on a numeric score: it checks conditions in order and stops")
            print("at the first true one, ensuring a clear, efficient grading decision.")

            done_elif = input("\nY or N if you want to continue: ").lower()
            if done_elif == "y":
                continue
            else:
                break
                
        elif conditions == "4":
            #Multiple conditions with Logical Operators
            print("\t\t\t\t      -----------------------------------------------------------------")
            print("\t\t\t\t      | This a process of Multiple Conditions with Logical Operators  |")
            print("\t\t\t\t      -----------------------------------------------------------------")

            #Inputs
            num = int(input("\nEnter a number: "))
            
            #Process
            if num % 2 == 0 and num % 3 == 0:
                print(num, "\nis divisible by both 2 and 3.")
            elif num % 2 == 0:
                print(num, "\nis divisible by 2 but not by 3.")
            elif num % 3 == 0:
                print(num, "\nis divisible by 3 but not by 2.")
            else:
                print(num, "\nis neither divisible by 2 nor by 3.")

            #Explanation
            print("\nThis uses if-elif-else with and to check divisibility first")
            print("whether the number is divisible by both 2 and 3, then by 2 only, 3 only, or neither.")

            done_ifEl = input("\nY or N if you want to continue: ").lower()
            if done_ifEl == "y":
                continue
            else:
                break

        elif conditions == "0":
            print("\nBack to Main Menu")
            break
        else:
            #Prevent errors
            print("\nInvalid!, Please select a number: ")
            
            
def sub_menu_loops():
    while True:
        print("\t\t\t\t\t\t-------------------------------------------")
        print("\t\t\t\t\t\t|                 LOOPS                   |")
        print("\t\t\t\t\t\t-------------------------------------------")
        print("\t\t\t\t\t\t|    |1| ===>|      Simple Loop      |    |")
        print("\t\t\t\t\t\t|    |2| ===>|      Nested Loop      |    |")
        print("\t\t\t\t\t\t|    |3| ===>|    Reversing String   |    |")
        print("\t\t\t\t\t\t|    |4| ===>|  Multiplication Table |    |")
        print("\t\t\t\t\t\t|    |0| ===>|         Back          |    |")
        print("\t\t\t\t\t\t-------------------------------------------")

        loops = input("\nEnter a number to execute a program: ")
        
        if loops == "1":
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |              This a process of Looping Numbers             |")
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\nThis is a simple For Loop")

            #Inputs
            start = int(input("\nStart from: "))
            end = int(input("End at: "))
            step = int(input("Step by: "))

            print("\nCounting:")

            #Process
            for a in range(start, end, step):
                print(a)

            #Explanation
            print("\nProcess: A for loop runs code repeatedly for each value")
            print("in a sequence like counting from start to end,")
            print("excluding end, stepping by a fixed amount.")
                
            done_loop = input("\nY or N if you want to continue: ").lower()
            if done_loop == "y":
                continue
            else:
                break    

        elif loops == "2":
            #Creating Patterns using Nested Loops
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |              This a process of Nested Looping              |")
            print("\t\t\t\t      --------------------------------------------------------------")

            #Input
            rows = int(input("\nEnter number of rows: "))

            #Process
            for i in range(1, rows + 1):# i starts at 1, not undefined!
                for j in range(1, i + 1):# print numbers 1 to i
                    print(j, end=" ")
                print()# move to next line

            #Explanation
            print("\nProcess: This code uses nested for loops to print a number triangle")
            print("then the outer loop controls the row number (i), and the inner")
            print("loop prints numbers from 1 to i on each line creating a step by step increasing pattern.")
                    
            done_NesLoop = input("\nY or N if you want to continue: ").lower()
            if done_NesLoop == "y":
                continue
            else:
                break

        elif loops == "3":
            #String in reverse using for loop
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |             This a process of Reversing String             |")
            print("\t\t\t\t      --------------------------------------------------------------")

            #Input
            string = input("\nEnter a word: ")

            #Process
            reversed_string = ""
            for char in string[::-1]:  # [::-1] slices the string in reverse
                reversed_string += char

            #Result
            print("\nReversed: ", reversed_string)

            #Explanation
            print("\nProcess: This code reverses a user-entered string by looping through")
            print("its characters backward using [::-1] and building a new string")
            print("step by step demonstrating how a for loop can process each character in sequence.")
            
            done_reverse = input("\nY or N if you want to continue: ").lower()
            if done_reverse == "y":
                continue
            else:
                break
                
        elif loops == "4":
            #Creating Multiplication Table using Nested Loops
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |            This a process of Looping a Pattern             |")
            print("\t\t\t\t      --------------------------------------------------------------")

            #Input
            n = int(input("\nEnter a number to generate its multiplication table (1-10): "))

            #Result
            print(f"\nMultiplication Table for {n}:\n")
            for i in range(1, 11):
                print(f"{n} x {i} = {n * i}")
            print("")

            #Explanation
            print("\nProcess: This code uses a single for loop not a nested loop to generate a")
            print("multiplication table for one number. It runs 10 times (for i = 1 to 10), printing")
            print("each product n x i. A nested loop would be needed for a full grid (1-10 x 1-10).")
                
            done_multi = input("\nY or N if you want to continue: ").lower()
            if done_multi == "y":
                continue
            else:
                break

        elif loops == "0":
            print("\nBack to Main Menu")
            break
        else:
            #Prevents errors
            print("\nInvalid!, Please select a number: ") 


def sub_menu_lists():
    while True:
        print("\t\t\t\t\t\t-------------------------------------------")
        print("\t\t\t\t\t\t|                  LISTS                  |")
        print("\t\t\t\t\t\t-------------------------------------------")
        print("\t\t\t\t\t\t|     |1| ===>|   Simple Lists   |        |")
        print("\t\t\t\t\t\t|     |2| ===>|  Appending Lists |        |")
        print("\t\t\t\t\t\t|     |3| ===>|  Checking Lists  |        |")
        print("\t\t\t\t\t\t|     |4| ===>|  Combining Lists |        |")
        print("\t\t\t\t\t\t|     |0| ===>|      Back        |        |")
        print("\t\t\t\t\t\t-------------------------------------------")

        lists = input("\nEnter a number to execute a program: ")
        
        if lists == "1":
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |         This a process of Creating a Simple Lists          |")
            print("\t\t\t\t      --------------------------------------------------------------")

            #Lists and Accessing it
            print("Enter 5 item to create a list: ")

            #Inputs
            my_list = [
                input("1st item: "),
                input("2nd item: "),
                input("3rd item: "),
                input("4th item: "),
                input("5th item: ")
            ]

            #Results
            print("\nYour list:", my_list)
            print("\nFirst element:", my_list[0])
            print("Last element: ", my_list[-1])

            #Explanation
            print("\nProcess: A list is created in Python by enclosing comma separated items")
            print("in square brackets, like my_list = [Hi, Hello, World] it can hold any")
            print("data type and is ordered, mutable, and indexed starting at 0.")

            done_list = input("\nY or N if you want to continue: ").lower()
            if done_list == "y":
                continue
            else:
                break
            
        elif lists == "2":
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |             This a process of Appending Lists              |")
            print("\t\t\t\t      --------------------------------------------------------------")

            #Appending List
            my_list = [1, 2, 3]
            print("\nStarting list: ", my_list)
            
            #Inputs
            item = input("\nEnter an item to add: ")
            my_list.append(item)

            #Result
            print("\nUpdated list: ", my_list)

            #Explanation
            print("\nProcess: This code starts with a list [1, 2, 3], lets the user input")
            print("any item (as text), and uses .append() to add it to the end showing how")
            print("lists can be dynamically extended.")
        
            done_append = input("\nY or N if you want to continue: ").lower()
            if done_append == "y":
                continue
            else:
                break 
         
        elif lists == "3":
            #Rechecking if I added a new word in a List
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |             This a process of Checking a Lists             |")
            print("\t\t\t\t      --------------------------------------------------------------")

            my_list = [1, 2, 3, 4, 5]
            print("\nCurrent list:", my_list)

            #Inputs
            item = input("\nEnter an item to add: ").strip()

            #Process
            if item.lstrip('-').isdigit():
                item = int(item)
            
            #Adding in a list
            my_list.append(item)

            #Results
            print("\nUpdated list:", my_list)

            #Rechecking the item in lists
            print("\nRechecking if the item is in the list...")

            #Results
            if item in my_list:
                print(f"\nYes! '{item}' is in the list.")
            else:
                print(f"\nNo! '{item}' is NOT in the list.")

            #Explanation
            print("\nProcess: Re-checking a list means using the 'in' operator")
            print("(Ex. item in my_list) to verify if a value exists in the list")
            print("useful after adding, removing, or modifying items to confirm the change took effect.")
                
            done_check = input("\nY or N if you want to continue: ").lower()
            if done_check == "y":
                continue
            else:
                break    
        
        elif lists == "4":
            #Combining it to two list by using zip
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |            This a process of Combining a Lists             |")
            print("\t\t\t\t      --------------------------------------------------------------")

            #Inputs
            list1 = input("\nEnter items for first list: ").split()
            list2 = input("Enter items for second list: ").split()

            #Process
            combined = list(zip(list1, list2))

            #Results
            print("\nCombined list pairs:", combined)

            #Explanation
            print("\nProcess: Combining lists with zip() pairs up elements")
            print("from two or more lists by position creating a list of")
            print("tuples like [(a1, b1), (a2, b2)] ideal for linking")
            print("matching data (Ex. names and scores).")
            
            done_combine = input("\nY or N if you want to continue: ").lower()
            if done_combine == "y":
                continue
            else:
                break

        elif lists == "0":
            print("\nBack to Main Menu")
            break
        else:
            #Prevents errors
            print("\nInvalid!, Please select a number: ")

def sub_menu_function():
    while True:
        print("\t\t\t\t\t\t-------------------------------------------")
        print("\t\t\t\t\t\t|                Functions                |")
        print("\t\t\t\t\t\t-------------------------------------------")
        print("\t\t\t\t\t\t|     |1| ===>|   Simple Function  |      |")
        print("\t\t\t\t\t\t|     |2| ===>|      Factorial     |      |")
        print("\t\t\t\t\t\t|     |3| ===>|  Reverse a String  |      |")
        print("\t\t\t\t\t\t|     |4| ===>| Compute an Average |      |")
        print("\t\t\t\t\t\t|     |5| ===>| Calculate the Area |      |")
        print("\t\t\t\t\t\t|     |0| ===>|        Back        |      |")
        print("\t\t\t\t\t\t-------------------------------------------")
        
        functions = input("\nEnter a number to execute a program: ")
        
        if functions == "1":
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |          This a process of Using a Simple Function         |")
            print("\t\t\t\t      --------------------------------------------------------------")

            #Function
            def simple_func(a, b, c, sep, end):
                print(a, b, c, sep=sep, end=end + "\n")

            #Inputs
            a = input("\nWord 1: ")
            b = input("Word 2: ")
            c = input("Word 3: ")
            d = input("Separator: ")
            e = input("Ending: ")

            #Use the function
            print("\nOutput: ")
            simple_func(a, b, c, d, e)
            
            done_func = input("\nY or N if you want to continue: ").lower()
            if done_func == "y":
                continue
            else:
                break
        
        if functions == "2":
            #Creating a function to see if the factiorial number is there
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |       This a process of Using a Factorial in Function      |")
            print("\t\t\t\t      --------------------------------------------------------------")

            def factorial(n):
                if n == 0 or n == 1:
                    return 1
                else:
                    return n * factorial(n - 1)

            # Get input
            num = int(input("\nEnter a non-negative integer: "))

            # Validate & compute
            if num < 0:
                print("\nFactorial is not defined for negative numbers.")
            else:
                result = factorial(num)
                print(f"{num} = {result}")
            
            #Explanation
            print("\nProcess: This code defines a recursive factorial() function")
            print("that computes 'n!' by multiplying 'n' with the factorial of 'n-1'")
            print("until it reaches the base case 0! = 1, then lets the user input a")
            print("number to calculate and display its factorial.")
            
            done_func_fac = input("\nY or N if you want to continue: ").lower()
            if done_func_fac == "y":
                continue
            else:
                break

        elif functions == "3":
            #Creating a function to use for reversing a string
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |        This a process of Function to Reverse a String      |")
            print("\t\t\t\t      --------------------------------------------------------------")
            def reverse_string(s):
                return s[::-1]  # Correct slicing: [start:stop:step]
            
            #Input
            text = input("\nEnter a word or phrase: ")

            #Process
            reversed_text = reverse_string(text)

            #Result
            print("\nReversed:", reversed_text)

            #Explanation
            print("\nProcess: This function uses slicing (s[::-1]) to reverse a")
            print("string in one line simple, fast, and beginner-friendly. In contrast,")
            print("the earlier loop based version builds the reversed string step-by-step")
            print("with a for loop, which is more explicit and educational but longer and slower. ")
            
            done_func_revrs = input("\nY or N if you want to continue: ").lower()
            if done_func_revrs == "y":
                continue
            else:
                break

        elif functions == "4":
            #Creating a function to find the average in a list
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |           This a process of Computing an Average           |")
            print("\t\t\t\t      --------------------------------------------------------------")

            #Process
            def average(listahan):
                total = 0
                count = 0
                for num in listahan:
                    total += num
                    count += 1
                return total / count

            #Input
            numbers = input("\nEnter numbers separated by spaces: ").split()
            numbers = [int(x) for x in numbers]

            #Result
            print("\nAverage:", average(numbers))

            #Explanation
            print("\nProcess: This code calculates the average of a list by manually")
            print("summing the numbers and counting them using a 'for' loop to show")
            print("how averaging works step by step.")
                        
            done_compute = input("\nY or N if you want to continue: ").lower()
            if done_compute == "y":
                continue
            else:
                break

        elif functions == "5":
            #Creating a function to calculate the result of the area
            print("\t\t\t\t      --------------------------------------------------------------")
            print("\t\t\t\t      |            This a process of Calculating an Area           |")
            print("\t\t\t\t      --------------------------------------------------------------")
            
            #Process
            def triangle_area(base, height):
                return 0.5 * base * height

            #Inputs
            base = float(input("\nEnter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))

            #Process
            area = triangle_area(base, height)

            #Result
            print(f"\nThe area of the triangle is: {area}")

            #Explanation
            print("\nProcess: This code defines a function triangle_area()")
            print("that calculates the area using the formula 1/2 x base x height,")
            print("then prompts the user to input the base and height making it")
            print("interactive and reusable for any triangle.")
            
            done_calc = input("\nY or N if you want to continue: ").lower()
            if done_calc == "y":
                continue
            else:
                break

        elif functions == "0":
            print("\nBack to Main Menu")
            break
        else:
            #Prevents errors
            print("\nInvalid!, Please select a number: ")

while True:
    main_menu_program()
    select_num = int(input("\nEnter a number to execute a program: "))
    if select_num == 0:
        print("Thankyou for using my Python Interactive Menu Program!")
        break
    elif select_num == 1:
        sub_menu_print_statements()
    elif select_num == 2:
        sub_menu_variables()
    elif select_num == 3:
        sub_menu_operators()
    elif select_num == 4:
        sub_menu_conditions()
    elif select_num == 5:
        sub_menu_loops()
    elif select_num == 6:
        sub_menu_lists()
    elif select_num == 7:
        sub_menu_function()
    else:
        print("\nInvalid!, Please select a number: ")

