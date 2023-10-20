# Finding number require
def finding_number(Element_to_find, random_number):
    return random_number.index(Element_to_find)
random_number=[2,3,4,5,6]
answear=""
random=[]
for i in range(0,len(random_number)):
    random.append("#")
    answear = answear + str(random_number[i])

def finding_numberhidden(random_number, dauvao):
    random=[]
    for i in range(0,len(random_number)):
        random.append("#")
    if dauvao in random_number:
        idk=finding_number(int(dauvao), random_number)
        random[idk] = dauvao
    return random