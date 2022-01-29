def AccessLevel(rights, minPermission):
    output = ""
    for val in rights:
        if val >= minPermission:
            output += "A"
        else:
            output += "D"
    print(output)


rights = []
rights = [int(num) for num in input("Enter the rights list: ").split(",") if num != "" and num != " "]
minPermission = int(input("Enter the min permission : "))

AccessLevel(rights, minPermission)
