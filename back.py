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
    ret=[]
    result=[]
    result_eficience=True
    for i in object:
        if isinstance(i, list)==True:
            for a in i:
                result.append(a)
        else:
            result.append(i)
    insert_str=result
    for i in insert_str:
        if isinstance(i,list):
            result_eficience=False
    ret=[result, result_eficience]
    return ret
def split_for_masive(insert_str: list,spliter: list):      
    in_objlist_is_nested_list="dontknow"
    # for a in insert_str:
    while in_objlist_is_nested_list==True or in_objlist_is_nested_list=='dontknow':
        bufer=split_double_list_once(insert_str)
        insert_str=bufer[0]
        if bufer[1] == False:
            in_objlist_is_nested_list=False
                
    for a in insert_str:
        proxod=[]
        for i in spliter:
            proxod.append(a.split(i))
            for z in proxod:
                if i in proxod:
                    split_for_masive(proxod, spliter)
    return proxod

split_for_masive("3+5*(7-6)",thirsth_operations)
if __name__ == "__main__":
    split_for_masive("3+5*(7-6)",thirsth_operations)
