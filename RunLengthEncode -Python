#Python code

def RunLengthEncode(string):
    string += " "
    new_string = ""
    count = 0
    i, j = 0, 0
    while j <= len(string) - 1:
        if string[i] == string[j]:
            count += 1
            j += 1
        else:
            if count > 4:
                new_string += '/0' + str(count) + string[i]
            else:
                new_string += count * string[i]
            count = 0
            i = j

    return new_string


print(RunLengthEncode(input("Enter the string to be encoded : ")))
