# Finding number require
def finding_number(Element_to_find, random_number):
    return random_number.index(Element_to_find)
def finding_thatonenumber(list, dauvao):
    numberlist=[]
    for i in range(0,len(list)):
        if dauvao == list[i]:
            numberlist.append(i)
    return numberlist

def finding_numberhidden(random_number, dauvao):
    random = ["#"] * len(random_number)  # Sử dụng list comprehension để tạo danh sách "#" ban đầu
    for i in range(len(dauvao)):
        if dauvao[i] in random_number:
            idk = finding_number(dauvao[i], random_number)
            if dauvao[i] in random:
                a = finding_thatonenumber(random, dauvao[i])
                if a:  # Kiểm tra nếu danh sách chỉ số không rỗng
                    b = a[0] + 1  # Lấy chỉ số tiếp theo
                    random[b] = dauvao[i]
            else:
                random[idk] = dauvao[i]
    return random
