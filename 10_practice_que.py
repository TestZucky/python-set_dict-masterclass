# # Given a string count how many times each word appears

# text = "apple banana apple orange banana apple"

# words = text.split()
# res = {}

# for word in words:

#     old_freq = res.get(word, 0)

#     res[word] = old_freq + 1

# print(res)

# # swap keys and values

# data  = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
# }

# # swapped = {value: key for key, value in data.items()}

# swapped = {}

# for key, value in data.items():
#     swapped[value] = key

# print(swapped)

# # merge 2 dictionaries into one. If a key exist in both add there vlaues

# dict1 = {'apple': 3, 'banana': 5}
# dict2 = {'orange': 4, 'banana': 2}

# # res = {'apple': 3, 'banana': 7, 'orange': 4}

# res = dict1.copy() # {'apple': 3, 'banana': 5, 'orange': 4 }

# for key, value in dict2.items():

#     res[key] = res.get(key, 0) + value

# print(res)


    # Given a list of words, group them into a dictionary where the key is the first letter

words = ['apple', 'banana', 'cherry', 'appricot', 'berry']

res = {}

for word in words:
    lst = res.get(word[0], [])
    lst.append(word)

    res[word[0]] = lst

print(res)

'''
{
    'a' : ['apple', 'apricot'],
    'b' : ['berry', 'banana'],
    'c' : ['cherry']
}
'''
