import random


def main():

    print("============================================================INDIAN PASSWORD GENERATOR======================================================================")
    print("==============================================================BY    SOHAM     SAHA=========================================================================")


    numPasswords = int(input("How many passwords do you want to generate? "))

    print("Generating " +str(numPasswords)+" passwords")

    passwordLengths = []

    print("Minimum length of password should be 8")

    for i in range(numPasswords):
        length = int(input("Enter the length of Password #" + str(i+1) + " "))
        new_length = length_checker(length)
        passwordLengths.append(new_length)


    Password = generatePassword(passwordLengths)

    for i in range(numPasswords):
        print ("Password #"+str(i+1)+" = " + Password[i])

def length_checker(length):

    if length<8:
        length = 8

    return length


def generatePassword(pwlength):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    passwords = []

    for i in pwlength:

        password = ""
        for j in range(i):
            next_letter_index = random.randrange(len(alphabet))
            password = password + alphabet[next_letter_index]

        #print("PW:",password)

        for j in range(i//4):
            password = replaceWithNumber(password)
            for k in range(j//3):
                password = replaceWithSpecialChar(password)
            password = replaceWithUppercaseLetter(password)




        passwords.append(password)


    return passwords


def replaceWithNumber(pword):
    for i in range(random.randrange(1,8)):
        replace_index = random.randrange(len(pword)//2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]
        #print("RWN:",pword)
        return pword


def replaceWithUppercaseLetter(pword):
    for i in range(random.randrange(1,8)):
        replace_index = random.randrange(len(pword)//2,len(pword))
        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]
        #print("RWUC:",pword)
        return pword


def replaceWithSpecialChar(pword):
    sp_char = ["@","!","#","$","%","^","&","*","_","-",".","?","=",":",";","/","(",")"]

    for i in range(random.randrange(1,8)):
        replace_index = random.randrange(len(pword)//2)
        pword = pword[0:replace_index] + str(random.choice(sp_char)) + pword[replace_index+1:]

        return pword


if __name__ == "__main__":
    main()