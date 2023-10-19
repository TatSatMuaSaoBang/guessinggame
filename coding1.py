a = "QTM@quantrimang.com"
b = ""
for i in range(len(a)):
    if a[i] == "@":
        break
    b = b + a[i]
a = a.replace(b, "")
print("a:", a)
print("b:", b)