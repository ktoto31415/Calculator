# def calculate(statement):       # "3+5*(7-6)"         split
#     numbrs=["0","1","2","3","4","5","6","7","8","9"]
#     second_operations = ["+","-"]
#     thirsth_operations= ["+","-"]
#     for symb in statement:
import re
second_operations = ["*","/"]
thirsth_operations= ["+","-"]
# print("3+5*(7-6)".split(thirsth_operations))
def split_for_masive(our_object: list,spliter: list):
    for a in our_object:
        for i in spliter:
            proxod.append(a.split(i))
            for z in proxod:
                if i in spliter:
                    split_for_masive(proxod.split(i))
            print(our_object.split(i))

split_for_masive("3+5*(7-6)",thirsth_operations)
