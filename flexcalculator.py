list_array = []

inputedNumber = input("Enter the Number: ")

while inputedNumber != "done":
    inputedNumber = input("Enter the Number: ")
    list_array.append(inputedNumber)
    
print(list_array[:-1])