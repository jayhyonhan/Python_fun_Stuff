def Decode(passwd, shift):
    result = ""
    for i in passwd:
        if 65 <= ord(i) <= 90:
            if (ord(i) + shift) > 90:
                result += chr(ord(i) + shift - 26)
            elif 65 > (ord(i) + shift):
                result += chr(ord(i) + shift + 26)
            elif 65 <= ord(i) + shift <= 90:
                result += chr(ord(i) + shift)
        elif 97 <= ord(i) <= 122:
            if (ord(i) + shift) > 122:
                result += chr(ord(i) + shift - 26)
            elif 97 > (ord(i) + shift):
                result += chr(ord(i) + shift + 26)
            elif 97 <= ord(i) + shift <= 122:
                result += chr(ord(i) + shift)
        elif i == " ":
            result += " "
    return result


n = input("Input : ")
for s in range(26):
    e = Decode(n, s)
    print(s, "encoded : " + e)

b = int(input("index: "))
c = input("answer: ")

print(Decode(c, b * -1))