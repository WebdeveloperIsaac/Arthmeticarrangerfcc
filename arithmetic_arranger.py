import re


def arithmetic_arranger(problems, solve=False):#optional parameter solve default agi false irutte
    # First Constraint that is the length of the problems must be less than or equal to 5 amele 
    if (len(problems) > 5):
        return "Error: Too many problems."
    #empty strings intialize madbeku for first of the problem and then the second 
    #lines and sumx and string for the resultant of the solution
    first = ""
    second = ""
    lines = ""
    sumx = ""
    string = ""
    for problem in problems:
        #with this i will check the problem for spaces or other stuffs
        if (re.search("[^\s0-9.+-]", problem)):
            #multiplication illa division constraint removed
          if (re.search("[/]", problem) or re.search("[*]", problem)):
            return "Error: Operator must be '+' or '-'."
          return "Error: Numbers must only contain digits."
#problem loop madudmele split madbeku after which we identify other props
        firstNumber = problem.split(" ")[0]#problem du first number 
        operator = problem.split(" ")[1]#next number admele operator
        secondNumber = problem.split(" ")[2]#next second number like 32 + 5 Done
#constraint first number or second number should not be more than 5
        if (len(firstNumber) >= 5 or len(secondNumber) >= 5):
            return "Error: Numbers cannot be more than four digits."
#sum is an empty string to contain the results in the string format
        sum = ""
        if (operator == "+"):
            sum = str(int(firstNumber) + int(secondNumber))
        elif (operator == "-"):
            sum = str(int(firstNumber) - int(secondNumber))
#ille max of first atva second number ge add 2 for the adjustment needed 
        length = max(len(firstNumber), len(secondNumber)) + 2#block numbers du
#that length ge space bittu pakkakhe barsade rjust nothing more
        top = str(firstNumber).rjust(length)
        bottom = operator + str(secondNumber).rjust(length - 1)
#line is an empty string to contain the lines ---- not underscore _ half an hour wated with that
        line = ""
        res = str(sum).rjust(length)
        for s in range(length):
            line += "-"
#problem End check madakke
        if problem != problems[-1]:
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            sumx += res + '    '
        else:
            first += top
            second += bottom
            lines += line
            sumx += res
#if solve is true then return the the formatted string run agutte amele remember \n not /n
    if solve:
        string = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
        string = first + "\n" + second + "\n" + lines
    return string