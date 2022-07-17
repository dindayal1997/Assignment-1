num1 = list(map(int, input("Enter some space separeted numbers: ").split()))
even_counter = 0
odd_counter = 0

for i in range(len(num1)):
    if num1[i] % 2 == 0:
        even_counter+=1
    else:
        odd_counter+=1

print("Number of even numbers: ", even_counter)
print("Number of odd numbers: ", odd_counter)