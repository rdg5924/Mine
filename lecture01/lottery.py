import random
numbers = []
rand_number = random.randint(1, 45)
numbers.append(rand_number)
while(len(numbers) != 6) :
    for i in numbers :
        if i == rand_number :
            break
    else :
        numbers.append(rand_number)
    rand_number = random.randint(1, 45)

print(sorted(numbers))
