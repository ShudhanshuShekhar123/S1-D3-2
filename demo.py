rows = 5  # You can change this to control the number of rows in the pattern

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

numbers = [12, 75, 150, 180, 145, 525, 50]


for num in numbers:
  
    if num % 5 == 0:
     
        if num > 150:
            
            continue
        elif num > 500:
          
            break
    
        print(num)


s1 = "Ault"
s2 = "Kelly"

midpoint = len(s1) // 2

s3 = s1[:midpoint] + s2 + s1[midpoint:]
print(s3)





str1 = "PyNaTive"


lowercase_chars = ''.join([char for char in str1 if char.islower()])
uppercase_chars = ''.join([char for char in str1 if char.isupper()])

arranged_str = lowercase_chars + uppercase_chars


print(arranged_str)



list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]


result = []


min_length = min(len(list1), len(list2))


for i in range(min_length):
    result.append(list1[i] + list2[i])


if len(list1) > min_length:
    result.extend(list1[min_length:])
elif len(list2) > min_length:
    result.extend(list2[min_length:])


print(result)




list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]


for i in range(len(list1)):
 
    print(list1[i], list2[-(i + 1)])



employees = ['Kelly', 'Emma']


defaults = {"designation": 'Developer', "salary": 8000}


employee_info = {employee: defaults.copy() for employee in employees}


print(employee_info)



tuple1 = (11, [22, 33], 44, 55)


tuple_list = list(tuple1)


tuple_list[1][0] = 222


modified_tuple = tuple(tuple_list)


print("tuple1:", modified_tuple)
