import random
from yes import *
from ham import *
#Cai dat gia tri
random_numbers = [random.randint(100000, 10000000)]
correct_number = "" 

# Ghi ra dap ane
print(random_numbers)

#Lay do dai cua guessing number
for i in range(0,len(random_numbers)):
    correct_number = correct_number + str(random_numbers[i]) # tao ra mot chuoi string la so hoan chinh cua random number

random_numbers=[]
for i in range(0,len(correct_number)):
    random_numbers.append(correct_number[i])

print(len(random_numbers))

print("This is a guessing numbers game where u can guessing the number we are hiding now let's go shall we? Y/N")
first=input("=> ")
if first in agree_words:
    print("Type Your guessing number length into here \/")
    while True:
        typing=int(input("=> "))
        if int(typing) == int((correct_number)):
            print("Wanna continue? => ")
            typing2=input("=> ")
            if typing2 in agree_words:
                print("Now guessing the letter on the number u dummy...")
                while typing2 in agree_words:
                    random=[]
                    for i in range(0,len(random_number)):
                            random.append("#")
                    typing3=int(input("=> "))
                    if typing3 == 109001:
                        print()
                    elif typing3 in random_numbers:
                        idk=finding_number(int(typing3), random_number)
                        random[idk] = typing3
                    else:
                        print("Try another number I tryly believe it will match some letter")
            else:
                quit()
        elif int(typing) < int((correct_number)):
            print("increase the length of the pre guessing numbers kiddo")
            continue
        elif int(typing) > int((correct_number)):
            print("that kinda long reduce it")
            continue

elif first in not_words:
    quit()