# # dict views

# user_data = {
#     "name": "Alice",
#     "age": 23,
#     "fav_items": ['toy', 'dog', 'laptop']
# }

# # print(user_data.keys())
# # print(user_data.values())
# # print(user_data.items())

# for key, value in user_data.items():
#     print(f"Key is --> {key}, Value is --> {value}")

# dict comprehension

squares = {x: x**2 for x in range(5)}

print(squares)

'''
{
    0 : 0,
    1 : 1,
    2 : 4
    ...
}
'''