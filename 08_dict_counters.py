from collections import Counter

names = ["ram", "shyam", "john", "reena", "raja", "ram", "reena"]

names_lookup_dict = Counter(names)

print(names_lookup_dict.most_common)