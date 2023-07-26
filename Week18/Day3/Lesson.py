# my_name="Jack"
# hello="Hello World"
# my_age= 27
# my_list=[my_name, my_age, hello]

# print(my_list[0])

# my_list.append(True)

# print(my_list)

# my_list.insert(1, 20)

# print(my_list)

# my_list.pop(0) is by index

#my_list.remove("Hello world") is by value

# my_list.index(True)

# my_copy_list=my_list.copy()

# my_list.clear

# my_list.count("True")
# my_list.extend(my_copy_list) will change my_list, while my_list+my_copy_list will not

# numbers=[1, 0, 5, 10, -2]

# my_sorted_numbers= sorted(numbers) will create a sorted shallow copy
# numbers.sort() will change numbers


# print(numbers)

# letters=["a", "e", "b"]
# letters.sort(reverse=True)
# print(letters)

# print(len(numbers))
# unique for number list: sum(numbers), max(numbers), min(numbers)

# # lists are sequences and are mutable

# part=numbers[2:5]
# print(numbers)

# my_fixed_numbers= ('1', 5, 'hello', True)

# print(type(my_fixed_numbers))

# tuples (and strings) are immutable, you can't change what is in their index

# list1 = [5, 10, 15, 20, 25, 50, 20]

# if (20 in list1)==True:
#     i= list1.index(20)
#     list1[i]=200
#     print(list1)

# my_tuple= (5, 6, 7)

# a, b, c=my_tuple
# #this is called unpacking. it also works with string, but the number of arguments needs to be the same!

# my_set= set()

# my_set.add('pop')
# my_set.add('bob')
# my_set.add('pop')
# my_set.add('rob')
# my_set.add('gob')
# my_set.add('nob')
# print(my_set)

# # see how every print, the indexes change! this means that while sets are mutable, they are not iterable
# my_set.remove('rob')

# Care!! we can change lists that are inside tuples! if an element in an immutable data type is mutable, then we can change it.