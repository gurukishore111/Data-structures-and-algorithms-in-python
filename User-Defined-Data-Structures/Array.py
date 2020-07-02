import array as arr

a = arr.array("i", [1, 2, 3, 4, 5])

while True:
    print("1.Print Array")
    print("2.Add Elements")
    print("3.Delete Elements")
    print("4.Exit")
    choice = int(input("Enter the option"))
    if choice == 1:
        print("The array elements are")
        for numbers in a:
            print(numbers)
    elif choice == 2:
        val = int(input(print("Enter the integer")))
        if isinstance(val, int):
            a.append(val)
    elif choice == 3:
        value = int(input("Enter the index of element want to delete"))
        a1 = a.pop(value)
        print("Deleted element:", a1)
    elif choice == 4:
        break
    else:
        print("Enter the valid option")
