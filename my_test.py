my_dict = {"key1" : 2, "key2" : 3, }
my_list = [1,2,3,4]
my_string = "stringus"
my_int = 23232
# [n**2 for n in numbers if n%2==0]
print([n for n in my_dict])
print("".join(str(n for n in my_dict)))
# mylist = ['spam', 'ham', 'eggs']
# intlist = [2,4,8]
# compiled = "".join(str(mylist))
# print(type(compiled))

# print(str(mylist).strip("[]").replace("'", ""))
# test = str(mylist).strip("[]").replace("'", "")
# print(test)
# test2 = "".join(map(str, intlist))
# print(test2)
var1 = "test"
var2 = "test2"
var3 = "test3"
numbers = [1,2,3]
print(*(x for x in my_dict),  sep='\n')
print(str({k:v for (k,v) in my_dict.items()}).strip("{}").replace("'", "").replace(",", '\n'), sep="242424")
print(str({k:v for (k,v) in my_dict.items()}).strip("{}").replace("'", "").replace(",", '\n'), end="")
# print(dict_var)
# print((x for x in numbers), sep='\n')
# print(*var1,*var2,var3, sep = "\n")
# print
if type(my_dict)==dict:
    lista = my_dict.items()
print(list(lista))
for i in lista:
    print(f"{i[0]} {i[1]}")
print(list(my_dict))

def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, number, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    if type(result)==dict:
        lista = my_dict.items()
        print(f"{label}")
        for i in lista:
            print(f"{i[0]} {i[1]}")
            # print(list(my_dict))
    if type(result)==str:
        print(f"{label}")
        print(f"string")
    if type(result)==list:
        print(f"{label}")
        for single_list in result:
            print(str(single_list).strip("()"))
    if type(result)==int:
        print(f"{label}")
        print(f"{result}")
    # your code
testowa_lista_list =[([7, 8, 9], 0), ([7, 8, 9], 0), ([7, 8, 9], 0), ([7, 8, 9], 1), ([7, 8, 9], 2), ([7, 8, 9], 3), ([7, 8, 9], 4), ([7, 8, 9], 5), ([7, 8, 9], 6), ([7, 8, 9], 7)]
label = "Manufacturer | Amount"
print_result(my_int,label)