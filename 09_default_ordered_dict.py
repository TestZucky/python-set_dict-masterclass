user_data = {
    "name": "Alice",
    "age": 23,
    "fav_items": ['toy', 'dog', 'laptop']
}

print(user_data.get('address', 0))

# # default_dict

# from collections import defaultdict

# dd = defaultdict(lambda: 5, user_data)

# print(dd['address'])
# print(dd['number'])

# # ordered dict

# user_data = {
#     "name": "Alice",
#     "age": 23,
#     "fav_items": ['toy', 'dog', 'laptop']
# }

# print(user_data)
