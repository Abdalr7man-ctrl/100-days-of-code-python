from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True :
    direction=input("Type 'encode' to encrypt type 'decode' to decrypt:\n").lower()
    if direction=="encode" or direction=="decode":
        break
    else : 
        print("valid input Try again")

text=input("Type your message:\n").lower()

while True :
    shift=input("Type the shift number:\n")
    if  shift.isdigit():
        shift=int(shift)
        break
    else :
        print("Valid shift input :( use number")


def encrypt(text,shift,direction):
    encode_decode=""
    if direction=="decode":
        shift*=-1
    for i in text:
        if i in alphabet:
            if alphabet.index(i)+shift > 25 :
                encode_decode+=alphabet[(alphabet.index(i)+shift)%len(alphabet)]
            elif alphabet.index(i)+shift < 0 :
                encode_decode+=alphabet[(alphabet.index(i)+shift)%len(alphabet)]
            else :
                encode_decode+=alphabet[alphabet.index(i)+shift]
        else :
            encode_decode+=i
    return f"Here is the {direction}d result: {encode_decode}"


print(encrypt(text,shift,direction))

