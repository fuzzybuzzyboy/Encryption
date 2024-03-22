import random, string
random_list, split_key = [''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(35000, 50000))) for _ in range(1000)], ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(5, 10)))
def encrypt_vigenere(plaintext, keyword):
    encrypted_text, keyword_index = "", 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(keyword[keyword_index % len(keyword)].upper()) - ord('A')
            if char.islower(): encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else: encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            keyword_index += 1
        else: encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

def decrypt_vigenere(encrypted_text, keyword):
    actual_decrypted_text, decrypted_text, decrypted_text1, keyword_index = "", "", "", 0
    for char in encrypted_text:
        if char.isalpha():
            shift = ord(keyword[keyword_index % len(keyword)].upper()) - ord('A')
            if char.islower(): decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else: decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            keyword_index += 1
        else: decrypted_char = char
        decrypted_text += decrypted_char
    decrypted_text, actual_decrypted_text, decrypted_text1 = decrypted_text.split(split_key)
    return actual_decrypted_text

plaintext="" # change this to your liking.
plaintext = f"{random.choice(random_list)}{split_key}"+plaintext+f'{split_key}{random.choice(random_list)}'
keyword = random.choice(random_list)
encrypted_text = encrypt_vigenere(plaintext, keyword)
decrypted_text = decrypt_vigenere(encrypted_text, keyword)
print(f'Decrypting with key: {keyword}')
print("\nEncrypted:", encrypted_text)
print("\nDecrypted:", decrypted_text)
#exec(decrypted_text) #
