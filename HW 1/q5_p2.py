def isPalindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


def passwordCheck(username, password):
    if len(password) >= 6 and len(password) <= 20:
        containsDigit, containsUppercase, containsSpecial = 0, 0, 0
        for i in range(len(password)):
            if (password[i]).isnumeric():
                containsDigit = 1
            if (password[i]).isupper():
                containsUppercase = 1
            if not password[i].isalnum():
                containsSpecial = 1
        if (containsDigit & containsUppercase & containsSpecial == 1):
            for i in range(len(password) - 2):
                counter = 0
                str = ""
                while (counter < 2):
                    str += password[i]
                    counter += 1
                if password.count(str) > 1:
                    return False
                else:
                    if isPalindrome(password):
                        return False
                    else:
                        unique = {}
                        for i in range(len(password)):
                            if password[i] in unique:
                                unique[password[i]] += 1
                            else:
                                unique[password[i]] = 1
                        if len(unique.keys()) <= int(len(password)/2):
                            return False
                        else:
                            revuname = username[::-1]
                            if revuname in password or username in password:
                                return False
                            else:
                                return True
        else:
            return False
    else:
        return False

#main
username = input("Username: ")

isValid = 0
while isValid == 0:
    password = input("Password: ")
    if passwordCheck(username, password) == True:
        print("That's a strong password.")
        isValid = 1
    else:
        print("Password not strong. Try again.")
