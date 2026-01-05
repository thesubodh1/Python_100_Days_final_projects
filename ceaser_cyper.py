alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def ceaser_cyper(text,shift,encode_or_decide):
    new_text = ""
    new_shift = shift
    if encode_or_decide == "decode":
        new_shift = shift * (-1)
    for letter in text:
        if letter not in alphabet:
            new_text += letter
        else:
            index = alphabet.index(letter)
            new_index = index + new_shift
            final_index = new_index % len(alphabet)
            new_text += alphabet[final_index]
    return (new_text)

is_on = True
while is_on:
    user_choice = input("Type 'encode' to encrypt, 'decode' to decrypt: ")
    user_message = input("Type your message: ").upper()
    shift = int(input("Type the shift number: "))
    print(ceaser_cyper(text=user_message,encode_or_decide=user_choice,shift=shift))
    again = input("Type 'yes' to go again else 'no'").lower()
    if again == "yes":
        is_on = True
    else:
        is_on = False




