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
    for i in range(0,len(dauvao)):
        if dauvao[i] in random_number:
            idk=finding_number(dauvao[i], random_number)
            if dauvao[i] in random:
                random
            else:
                random[idk] = dauvao[i]
    return random