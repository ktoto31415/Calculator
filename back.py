# def calculate(statement):       # "3+5*(7-6)"         split
#     numbrs=["0","1","2","3","4","5","6","7","8","9"]
#     second_operations = ["+","-"]
#     thirsth_operations= ["+","-"]
#     for symb in statement:
import re
second_operations = ["*","/"]
thirsth_operations= ["+","-"]
print("3+5*(7-6)".split(thirsth_operations))