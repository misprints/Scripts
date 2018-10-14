#!/usr/bin/python3
from time import sleep


def apr(string):  #Extraction Factors For Common Decryption.
    num = len(string)
    reminder = []
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            reminder.append(i)
    if not reminder:
        reminder = apr(string + ' ')
    return reminder


def encrypt():
    pwd = ''
    orgn = input('[*] Input the Orignal Strings : ')
    slic = input('[*] The Groups Number(2 By Default) : ')
    slic = int(slic) if slic else 2
    for i in range(slic):
        pwd += orgn[i::slic]  #Divide Into Groups.
    sleep(0.5)
    return '\n[+] Encryption:\n\n"' + pwd + '"'


def decryption(cmd):
    pwd = input('[*] Input the Encrypted Strings : ')
    slic = range(2, len(pwd)) if cmd == '3' else apr(
        pwd)  #Choose The Way To Decrypt.
    orgs = {}  #Use A Dictionary To Save The Results.
    for i in slic:
        org = decrypt(pwd, i)  #Use The Core Function Here.
        orgs[i] = org
    sleep(0.5)
    print('\n[+] "Groups : Decryptions" :"')
    for i, j in orgs.items():
        print(i, ": " + j)


def decrypt(pwd, slic):  #The Core Function.
    quotient, reminder = divmod(len(pwd), slic)
    if reminder:
        quotient += 1  #If There Is A Reminder, It Means We Need One More Iteration.
        h = quotient * reminder
        ind = (h + i * (quotient) - 1 for i in range(1, slic - reminder + 1)
               )  #Find The Places To Insert Spaces.
        for i in ind:
            pwd = pwd[:i] + ' ' + pwd[i:]  #Insert A Space.
    result = ''
    for i in range(quotient):
        result += pwd[i::quotient]
    return result.rstrip(
    )  #At Last The Spaces Will Be At The End Of The String. Use str.rstrip() To Delete It.


def main():
    cmd = ''
    while cmd != '4':
        try:
            cmd = input(
                "[*] Common:\n1. Encryption\n2. Common Decryption\n3. Brute Force(If Common Decryption Doesn't Work)\n4. Quit\n: "
            )
            if cmd == '1':
                print(encrypt())
            if cmd in '23':
                decryption(cmd)
        except Exception as e:
            print('[-] Wrong Input!\n' + str(e))
        finally:
            print('\n' + '=' * 20)
    print('=' * 10 + "Thanks For Playing" + '=' * 10)


if __name__ == '__main__':
    main()
