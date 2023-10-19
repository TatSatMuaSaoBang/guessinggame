import random
from yes import *
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
            quit()
        elif int(typing) < int((correct_number)):
            print("increase the length of the pre guessing numbers kiddo")
            continue
        elif int(typing) > int((correct_number)):
            print("that kinda long reduce it")
            continue
            
elif first in not_words:
    quit()