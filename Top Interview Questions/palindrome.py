def isPalindrome(s):
    if s == "":
        return True
    elif len(s) == 1:
        return True
    else:
        start, end  = 0, len(s) - 1

        while start < end:
            char1 = s[start].lower()
            char2 = s[end].lower()
            isValidChar1 = isValid(char1)
            isValidChar2 = isValid(char2)

            if isValidChar1 and isValidChar2:
                if char1 != char2:
                    return False
                else:
                    start += 1
                    end -= 1
    return True

def isValid(char):
    return char.isalpha()


assert True == isPalindrome("aa")
