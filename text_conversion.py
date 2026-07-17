def caesar(text, shift, encrypt=True):   # function to conver text

    # Validators to checks the perameters
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift

    # ----- Main Logic ------
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):   # call caesar function to encrypt plane text
    return caesar(text, shift)
    
def decrypt(text, shift):   # call caesar function to decrypt cipher text 
    return caesar(text, shift, encrypt=False)

# Demo Execution
encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf."
decrypted_text = decrypt(encrypted_text, 13)
print(encrypted_text)
print(decrypted_text)
