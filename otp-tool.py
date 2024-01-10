import random #line:1
charTable =("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"," ",".",",","!","?")#line:2
encodedString =""#line:3
decodedString =""#line:4
keyString =""#line:5
quitFlag =False #line:6
def enSubstitute (O0O000OOOOO0OOO0O ):#line:8
    O0O000OOOOO0OOO0O =O0O000OOOOO0OOO0O .replace (" ","@")#line:9
    O0O000OOOOO0OOO0O =O0O000OOOOO0OOO0O .replace (".","%")#line:10
    O0O000OOOOO0OOO0O =O0O000OOOOO0OOO0O .replace (",","#")#line:11
    return O0O000OOOOO0OOO0O #line:12
def deSubstitute (O00O00OO00O000000 ):#line:14
    O00O00OO00O000000 =O00O00OO00O000000 .replace ("@"," ")#line:15
    O00O00OO00O000000 =O00O00OO00O000000 .replace ("%",".")#line:16
    O00O00OO00O000000 =O00O00OO00O000000 .replace ("#",",")#line:17
    return O00O00OO00O000000 #line:18
print ("-- TKK 1.2 branch A --")#line:20
while (quitFlag ==False ):#line:22
    inputMode =input ("\n[E]ncrypt, [D]ecrypt?, [G]enerate Keys, [H]elp, or [Q]uit -> ").upper ()#line:24
    if inputMode =="Q":#line:26
        quitFlag =True #line:27
    elif inputMode =="E":#line:29
        print ("[E]ncrypt mode active.")#line:30
        inputString =input ("Input clear message -> ").upper ()#line:31
        inputKeyOption =input ("[G]enerate a random key, or [P]rovide one? -> ").upper ()#line:32
        if inputKeyOption =="G":#line:33
            for char in inputString :#line:34
                randChar =charTable [random .randrange (len (charTable ))]#line:35
                keyString =keyString +randChar #line:36
        elif inputKeyOption =="P":#line:37
            keyString =input ("          Input key -> ").upper ()#line:38
        else :#line:39
            print ("Error: Invalid response.")#line:40
        posi =0 #line:41
        inputStringLen =len (inputString )#line:42
        keyStringLen =len (keyString )#line:43
        if keyStringLen >=inputStringLen :#line:44
            for char in inputString :#line:45
                try :#line:46
                    charCode =charTable .index (char )#line:47
                except :#line:48
                    print ("Error: The clear message contains an unrecognized character.")#line:49
                    charCode =0 #line:50
                try :#line:51
                    keyStringCode =charTable .index (keyString [posi ])#line:52
                except :#line:53
                    print ("Error: The key contains an invalid character.")#line:54
                    keyStringCode =0 #line:55
                resultCharCode =charCode +keyStringCode #line:56
                if (resultCharCode >27 ):#line:57
                    resultCharCode =resultCharCode -len (charTable )#line:58
                encodedString =encodedString +charTable [resultCharCode ]#line:59
                posi =posi +1 #line:60
            encodedString =enSubstitute (encodedString )#line:61
            keyString =enSubstitute (keyString )#line:62
            print ("Encrypted message: "+encodedString )#line:63
            if inputKeyOption =="G":#line:64
                print ("              Key: "+keyString )#line:65
        else :#line:66
            print ("Error: The key is too short.")#line:67
    elif inputMode =="D":#line:69
        print ("[D]ecrypt mode active.")#line:70
        inputString =input ("Input encrypted message -> ").upper ()#line:71
        inputString =deSubstitute (inputString )#line:72
        keyString =input ("              Input key -> ").upper ()#line:73
        keyString =deSubstitute (keyString )#line:74
        posi =0 #line:75
        inputStringLen =len (inputString )#line:76
        keyStringLen =len (keyString )#line:77
        if keyStringLen >=inputStringLen :#line:78
            for char in inputString :#line:79
                try :#line:80
                    charCode =charTable .index (char )#line:81
                except :#line:82
                    print ("Error: The encrypted message contains an unrecognized character.")#line:83
                    charCode =0 #line:84
                try :#line:85
                    keyStringCode =charTable .index (keyString [posi ])#line:86
                except :#line:87
                    print ("Error: The key contains an invalid character.")#line:88
                    keyStringCode =0 #line:89
                resultCharCode =int (charCode )-int (keyStringCode )#line:90
                if (resultCharCode <0 ):#line:91
                    resultCharCode =resultCharCode +len (charTable )#line:92
                decodedString =decodedString +charTable [resultCharCode ]#line:93
                posi =posi +1 #line:94
            print ("Decoded message: "+decodedString )#line:95
        else :#line:96
            print ("Error: The key is too short.")#line:97
    elif inputMode =="H":#line:99
        print ("[H]elp mode active.")#line:100
        print ("This software will encrypt or decrypt a text message.\nThis software utilizes an encryption technique that, if used properly, cannot be cracked.\n   Use Guide:\n - The message and the key may only contain letters, numbers, spaces, periods, exclaimation marks, and question marks.\n - The key must be at least as long as the message.\n - If you don't have a key, the program will generate a random key.\n - The message will be converted to upper case.\n - Never transmit keys by the same method as the encrypted message.\n - Destroy key promptly after decoding.\n - Never re-use a key.")#line:101
    elif inputMode =="G":#line:103
        print ("[G]enerate Keys mode active.")#line:104
        numKeysInput =int (input ("Number of keys to create? -> "))#line:105
        keysLenInput =int (input ("      Length of each key? -> "))#line:106
        posi =1 #line:107
        genKey =""#line:108
        while (posi <=numKeysInput ):#line:109
            charIndex =0 #line:110
            while (charIndex <=keysLenInput ):#line:111
                randChar =charTable [random .randrange (len (charTable ))]#line:112
                genKey =genKey +randChar #line:113
                charIndex =charIndex +1 #line:114
            print (str (posi )+": "+enSubstitute (str (genKey )))#line:115
            posi =posi +1 #line:116
            genKey =""#line:117
    else :#line:119
        print ("Unrecognized command.")#line:120
    encodedString =""#line:122
    decodedString =""#line:123
    keyString =""#line:124
print ("\n-- Program terminated --")#line:126
