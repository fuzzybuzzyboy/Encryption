import string, random
from unencryption import *
from encryption import *

random_list = [''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(35000, 50000))) for _ in range(1000)]
plaintext = ""
plaintext = f'{random.choice(random_list)}!-#2f1'+plaintext+f'!-#2f1{random.choice(random_list)}'
keyword = random.choice(random_list)
keyword = random.choice(random_list)
print(f'Decrypting with key: {keyword}')
encrypted_text = encrypt(plaintext, keyword)
print("\nEncrypted:", encrypted_text)
decrypted_text = unencryption(encrypted_text, keyword)
print("\nDecrypted:", decrypted_text)