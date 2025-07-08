# Dictionary Comprehensions 
# create a new dictiary from an existing one or any iterable object

# new_dict = {key: value for item in iterable if condition}
# iterable can be a list, tuple, set, or any iterable object

import random

squares = {x: x**2 for x in range(1, 6)}
print(squares)

names = ["Arun", "Radha", "Rajani"]

scores = ({x : random.randint(1, 100) for x in names})
print(scores)

result = {key: ("Pass" if value >= 50 else "Fail") for key, value in scores.items()}
print(result)


# pandas
import pandas as pd
data = {
    "Name": ["Arun", "Radha", "Rajani"],
    "Score": [random.randint(1, 100) for _ in range(3)]
}
df = pd.DataFrame(data)

l = {row["Name"]: row["Score"] for index, row in df.iterrows()}
print(l)