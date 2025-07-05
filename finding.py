import pandas as pd

question = input("what is your question about someone ?").lower().split()

dataset = pd.read_csv("amin.csv")

found = False

for _, row in dataset.iterrows():
    if row["name"].lower() in question:
        if "do" in question:
            print(f"{row['name']} works as {row['job']}")
            found = True
            break
        elif "old" in question:
            print(f"{row['name']} is {row['age']} old")
            found = True
            break
        else:
            print(f"{row['name']} is from {row['city']}")
            found = True
            break
if not found:
    print("sorry we dont have info on that person Right now.")
