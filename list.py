fruits = ["apple", "cherry", "banana", "orange", "mango"]
fruits.append("tomato")
fruits.remove("apple")
fruits.sort()
fruits.remove(fruits[1])

for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)