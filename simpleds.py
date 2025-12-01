my_list = [10, 20, 30, 40]
my_list.append(50)
print("List:", my_list)
print("List Slice:", my_list[1:4])

my_tuple = (1, 2, 3, 4)
print("Tuple:", my_tuple)
print("Tuple Element:", my_tuple[2])

my_dict = {"name": "Alice", "age": 25}
my_dict["city"] = "New York"
print("Dictionary:", my_dict)
print("Dictionary Keys:", list(my_dict.keys()))

my_set = {1, 2, 3, 4}
my_set.add(5)
print("Set:", my_set)

my_string = "Hello Python"
print("Upper:", my_string.upper())
print("Slice:", my_string[0:5])
print("Formatted:", f"Message: {my_string}")

squared_list = [x*x for x in range(1, 6)]
print("List Comprehension:", squared_list)

squared_dict = {x: x*x for x in range(1, 6)}
print("Dict Comprehension:", squared_dict)

squared_set = {x*x for x in range(1, 6)}
print("Set Comprehension:", squared_set)
