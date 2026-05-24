
#this area was use for testing and understandind some elements of main.py


# d = {}
# transactions = [
#     {"category": "Food", "amount": 280},
#     {"category": "Transport", "amount": 350},
#     {"category": "Food", "amount": 60},
# ]

# for row in transactions:
#     print("Current dict:", d)
#     print("Processing:", row["category"], row["amount"])
#     if row["category"] in d:
#         d[row["category"]] += row["amount"]
#     else:
#         d[row["category"]] = row["amount"]
#     print("After:", d)
#     print("---")



d={}
trans = [
    {"description": "Netflix", "amount": 649},
    {"description": "Uber", "amount": 350},
    {"description": "Netflix", "amount": 649},
]

for row in trans:
    if row['description'] in d:
        d[row["description"]]["count"] += 1
    else:
        d[row["description"]] = {"count": 1, "amount": row["amount"]}

print(d)