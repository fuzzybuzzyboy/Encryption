def unencryption(encrypted_text, keyword, *ignore):
    actual_decrypted_text, decrypted_text, keyword_index = "", "", 0
    for char in encrypted_text:
        if char.isalpha():
            shift = ord(keyword[keyword_index % len(keyword)].upper()) - ord('A')
            if char.islower(): decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else: decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            keyword_index += 1
        else: decrypted_char = char
        decrypted_text += decrypted_char   
    ignore, actual_decrypted_text, ignore = decrypted_text.split('!-#2f1')
    return actual_decrypted_text