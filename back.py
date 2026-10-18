# def calculate(statement):       # "3+5*(7-6)"         split
#     numbrs=["0","1","2","3","4","5","6","7","8","9"]
#     second_operations = ["+","-"]
#     thirsth_operations= ["+","-"]
#     for symb in statement:
# import re
second_operations = ["*","/"]
thirsth_operations= ["+","-"]
# print("3+5*(7-6)".split(thirsth_operations))
def split_double_list_once(object:list):                    #[list_return, is_not_nested_list_in_return_list]распаковка вложенных листов с глубиной 1
    if not isinstance(object, list):
        raise TypeError("Argument must be list")
    print("once spliter is start working", object)
    ret=[]
    result=[]
    result_eficience=True
    for i in object:
        print("     once deep check element in list start ", i)
        if isinstance(i, list)==True:
            print("     isinstance(i, list)==True ", i)
            for a in i:
                result.append(a)
        else:
            print("     isinstance(i, list)==False ", i)
            result.append(i)
    for i in result:
        if isinstance(i,list):
            result_eficience=False
    ret=[result, result_eficience]
    print("     ",ret)
    return ret

def spliter_nested_lists(object:list):
    print("spliter_nested_lists start working")
    in_objlist_is_nested_list=True
    while in_objlist_is_nested_list==True:
        print("step_spliter")
        bufer=split_double_list_once(object)
        if bufer[1] == True:
            in_objlist_is_nested_list=False
            print("end")
    print(bufer)
    return bufer

def split_for_masive(insert_str: list,spliter: list):
    if not isinstance(insert_str, list) or not isinstance(spliter, list):
        raise TypeError("Arguments must be lists")      
    
    insert_str=spliter_nested_lists(insert_str)[0]
                
    for a in insert_str:
        proxod=[]
        for i in spliter:
            proxod.append(a.split(i))
            for z in proxod:
                if i in proxod:
                    split_for_masive(proxod, spliter)
    proxod=spliter_nested_lists(proxod)[0]
    return proxod

if __name__ == "__main__":
    print(split_for_masive(["3+5*(7-6)"],thirsth_operations))

