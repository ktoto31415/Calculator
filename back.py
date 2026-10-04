# def calculate(statement):       # "3+5*(7-6)"         split
#     numbrs=["0","1","2","3","4","5","6","7","8","9"]
#     second_operations = ["+","-"]
#     thirsth_operations= ["+","-"]
#     for symb in statement:
# import re
second_operations = ["*","/"]
thirsth_operations= ["+","-"]
# print("3+5*(7-6)".split(thirsth_operations))

 
def split_for_masive(our_object: list,spliter: list):      #поиск и устранение листов в листах с глубиной 1
    def split_double_list_once(list):
        result=[]
        result_eficience=True
        for i in our_object:
            if isinstance(i, list)==True:
                result.append(i)
        our_object=result
        for i in our_object:
            if isinstance(i,list):
                result_eficience=False
        return result_eficience
    
    obj_is_double_list="dontknow"
    # for a in our_object:
    while obj_is_double_list==True or obj_is_double_list=='dontknow':
        if split_double_list_once() == False:
            obj_is_double_list=False
                
    for a in our_object:
        proxod=[]
        for i in spliter:
            proxod.append(a.split(i))
            for z in proxod:
                if i in spliter:
                    split_for_masive(proxod, spliter)
            print(our_object.split(i))

split_for_masive("3+5*(7-6)",thirsth_operations)
