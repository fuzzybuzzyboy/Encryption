def encrypt(plaintext, keyword):
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