#frequency analysis

#This will both encode and decode message. Returns encrypted messages. 
def Encrypt(message,key):
    return [(int(message[i]) ^ key[i%len(key)]) for i in range(0,len(message))]

def Crypto(message,keyLength):
    maxSize = 0 
    for i in range(0,len(message)):
        if int(message[i]) > maxSize:
            maxSize = int(message[i])
    key = [0] * keyLength
    nData = [[0 for x in range(maxSize+1)] for y in range(keyLength)] 
    for i in range(0,len(message)):
        j = i % keyLength
        nData[j][int(message[i])] += 1
        if nData[j][int(message[i])] > nData[j][key[j]]:
            key[j] = int(message[i])
    spaceAscii =32
    for i in range(0,keyLength):
        key[i] = key[i] ^ spaceAscii
    return key

message = open("p059_cipher.txt","r").read().split(",")
keyLength = 3
key = Crypto(message,keyLength)
decryptedMessage = Encrypt(message,key)
secrete = ""
for i in decryptedMessage:
    secrete += str(chr(i))
print("Decrypted message: ",secrete)
print("Sum is: ",sum(decryptedMessage))
