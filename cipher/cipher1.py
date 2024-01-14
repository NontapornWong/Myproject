alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z']

def cesar_code(start_text, num_shift, cipher_direction):
    end_text =""
    if cipher_direction == "decode":
        num_shift *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + num_shift
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {direction}d result is: {end_text}")


from art import logo
print(logo)   

let_continue = True
while let_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift%26
    cesar_code(start_text=text, num_shift=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        let_continue = False
        print("Goodbye")