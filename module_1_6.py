my_dict = {"My name": "Viktor", "Year of berth": 1971, "My phone": +79788734461}
print(my_dict)
print(my_dict["My name"])
print(my_dict.get("age", "This key not in use"))
my_dict["Status"] = "Student"
my_dict.update({"course": 1, "Level": "kettle"})
print(my_dict)
a = my_dict.pop("My phone")
print(a)
print(my_dict)
my_set = {1, 2, 2, 1, 3, 'apple', "apple", True, (9,8,7,7)}
print(my_set)
my_set.add(2024)
my_set.add("home")
my_set.remove("apple")
print(my_set)



