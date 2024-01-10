import random

charTable = (
"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
"Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", ".", ",", "!", "?")
encodedString = ""
decodedString = ""
keyString = ""
quitFlag = False


def enSubstitute(O0O000OOOOO0OOO0O):
    O0O000OOOOO0OOO0O = O0O000OOOOO0OOO0O.replace(" ", "@")
    O0O000OOOOO0OOO0O = O0O000OOOOO0OOO0O.replace(".", "%")
    O0O000OOOOO0OOO0O = O0O000OOOOO0OOO0O.replace(",", "#")
    return O0O000OOOOO0OOO0O


def deSubstitute(O00O00OO00O000000):
    O00O00OO00O000000 = O00O00OO00O000000.replace("@", " ")
    O00O00OO00O000000 = O00O00OO00O000000.replace("%", ".")
    O00O00OO00O000000 = O00O00OO00O000000.replace("#", ",")
    return O00O00OO00O000000


print("-- TKK 1.2 branch A --")

while not quitFlag:
    inputMode = input("\n[E]ncrypt, [D]ecrypt?, [G]enerate Keys, [H]elp, or [Q]uit -> ").upper()

    if inputMode == "Q":
        quitFlag = True
    elif inputMode == "E":
        print("[E]ncrypt mode active.")
        inputString = input("Input clear message -> ").upper()
        inputKeyOption = input("[G]enerate a random key, or [P]rovide one? -> ").upper()

        if inputKeyOption == "G":
            for char in inputString:
                randChar = charTable[random.randrange(len(charTable))]
                keyString += randChar
        elif inputKeyOption == "P":
            keyString = input("          Input key -> ").upper()
        else:
            print("Error: Invalid response.")

        posi = 0
        inputStringLen = len(inputString)
        keyStringLen = len(keyString)

        if keyStringLen >= inputStringLen:
            for char in inputString:
                try:
                    charCode = charTable.index(char)
                except:
                    print("Error: The clear message contains an unrecognized character.")
                    charCode = 0

                try:
                    keyStringCode = charTable.index(keyString[posi])
                except:
                    print("Error: The key contains an invalid character.")
                    keyStringCode = 0

                resultCharCode = charCode + keyStringCode

                if resultCharCode > 27:
                    resultCharCode -= len(charTable)

                encodedString += charTable[resultCharCode]
                posi += 1

            encodedString = enSubstitute(encodedString)
            keyString = enSubstitute(keyString)

            print("Encrypted message: " + encodedString)

            if inputKeyOption == "G":
                print("              Key: " + keyString)
        else:
            print("Error: The key is too short.")
    elif inputMode == "D":
        print("[D]ecrypt mode active.")
        inputString = input("Input encrypted message -> ").upper()
        inputString = deSubstitute(inputString)
        keyString = input("              Input key -> ").upper()
        keyString = deSubstitute(keyString)

        posi = 0
        inputStringLen = len(inputString)
        keyStringLen = len(keyString)

        if keyStringLen >= inputStringLen:
            for char in inputString:
                try:
                    charCode = charTable.index(char)
                except:
                    print("Error: The encrypted message contains an unrecognized character.")
                    charCode = 0

                try:
                    keyStringCode = charTable.index(keyString[posi])
                except:
                    print("Error: The key contains an invalid character.")
                    keyStringCode = 0

                resultCharCode = int(charCode) - int(keyStringCode)

                if resultCharCode < 0:
                    resultCharCode += len(charTable)

                decodedString += charTable[resultCharCode]
                posi += 1

            print("Decoded message: " + decodedString)
        else:
            print("Error: The key is too short.")
    elif inputMode == "H":
        print("[H]elp mode active.")
        print("This software will encrypt or decrypt a text message.")
        print("This software utilizes an encryption technique that, if used properly, cannot be cracked.")
        print("   Use Guide:")
        print(" - The message and the key may only contain letters, numbers, spaces, periods, exclamation marks, and question marks.")
        print(" - The key must be at least as long as the message.")
        print(" - If you don't have a key, the program will generate a random key.")
        print(" - The message will be converted to upper case.")
        print(" - Never transmit keys by the same method as the encrypted message.")
        print(" - Destroy key promptly after decoding.")
        print(" - Never re-use a key.")
    elif inputMode == "G":
        print("[G]enerate Keys mode active.")
        numKeysInput = int(input("Number of keys to create? -> "))
        keysLenInput = int(input("      Length of each key? -> "))
        posi = 1
        genKey = ""

        while posi <= numKeysInput:
            charIndex = 0

            while charIndex <= keysLenInput:
                randChar = charTable[random.randrange(len(charTable))]
                genKey += randChar
                charIndex += 1

            print(str(posi) + ": " + enSubstitute(str(genKey)))
            posi += 1
            genKey = ""
    else:
        print("Unrecognized command.")

    encodedString = ""
    decodedString = ""
    keyString = ""

print("\n-- Program terminated --")
