import re

def arithmetic_arranger(problems, solve = False):

    if (len(problems) > 5):
        return 'Error: Too many problems.'

    first = ''
    second = ''
    lines = ''
    sumx = ''
    string = ''
    for problem in problems:
        if (re.search('[^\s0-9,+-]', problem)):
            if(re.search(['/'], problem) or re.search('[*]', problem)):
                return 'Error: Operator must be "+" or "-".'
            return 'Error: numbers must only contain digits.'
        firstNumber = problem.split()[0]
        operator = problem.split()[1]
        secondNumber = problem.split()[2]

        if len(firstNumber) >= 5 or len(secondNumber) >= 5:
            return 'Error: Numbers cannot be bigger than 4 digits'

        sum = ''
        if(operator == '+'):
            sum = str(int(firstNumber) + int(secondNumber))
        elif(operator=='-'):
            sum = str(int(firstNumber) - int(secondNumber))
        length = max(len(firstNumber),len(secondNumber)) + 2
        top = str(firstNumber).rjust(length)
        bottom = operator + str(secondNumber).rjust(length-1)
        line = ''
        res = str(sum).rjust(length)
        for s in range(length):
            line = line + '-'
        if problem != problems[-1]:
            first = first + top + '    '
            second = second + bottom + '    '
            lines = lines + line + '    '
            sumx = sumx + res + '    '
        else:
            first = first + top
            second = second + bottom
            lines = lines + line
            sumx = sumx + res

    if solve:
        string = first + '\n' + second + '\n' + lines + '\n' + sumx
    else:
        string = first + '\n' + second + '\n' + lines
    return string

print(arithmetic_arranger(["32 + 698", "3801 - 9999", "45 + 43", "123 + 49"], True))
