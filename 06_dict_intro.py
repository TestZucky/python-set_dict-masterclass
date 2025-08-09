# # dict

# user_data = {
#     "name": "Alice",
#     "age": 23,
#     "fav_items": ['toy', 'dog', 'laptop']
# }

# print(user_data)
# print(type(user_data))

# # add or access elements

# user_data = {
#     "name": "Alice",
#     "age": 23,
#     "fav_items": ['toy', 'dog', 'laptop']
# }

# user_data["city"] = "Raipur"
# print(user_data)

# print(user_data['age'])

# delete the elements

user_data = {
    "name": "Alice",
    "age": 23,
    "fav_items": ['toy', 'dog', 'laptop'],
    "city" : "Raipur",
}

# age = user_data.pop("age")
# del user_data['age']
age = user_data.popitem()
print(user_data)

