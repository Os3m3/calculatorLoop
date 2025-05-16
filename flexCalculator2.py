listStore = []

enteredNumber = (input("Enter the Number: "))
status = True

while status == True:
    enteredNumber = (input("Enter the Number: "))
    listStore.append(enteredNumber)

    if enteredNumber == "done":
        status = False

else:
    print(listStore)