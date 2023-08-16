# child_one = {'name':'ali',
#              'birth_city':'Mecca',
#              'birthdat e':'1-1-2021'}

# x=child_one['name']
# print(x)

# a  = 1, 2, 3, 4, 5, 6,  7, 9, 10
# b = a[0::2]
# print(b)

# first , second = True,False

# result = first and second

# print(result)


# price = 2 

# txt = " the price is {} rs"

# print(txt.format(price))


# name = "hamad"
# age = 23
# msg = 'My name is {1} and Im {0} of age'.format(age,name)
# print(msg)


# a  = dict()

# for i in range(4):
#     for j in range (2):
#         a[i] = j
        
# print(a)


# a = (10 , 'alpha' , [1,2])

# b = [2][0]
# print(b)


# def fun (lst):
#     length = len(lst)-1;

sum = 0
number =5


from typing import List
def perfect_Number_check(num: int) -> bool:
    # write your code here ^_^
    div = 0
    for i in range(1,num ):
        if num % i == 0:
            div += i
    return div == num

print(perfect_Number_check(14))

        