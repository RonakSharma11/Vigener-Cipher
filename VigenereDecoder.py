def vigenere_decrypt(ciphertext, keyword):
    """
    This function takes a Vigenere ciphertext and a keyword as input, and returns the decrypted plaintext.
    """
    plaintext = ""
    keyword = keyword.upper()
    i = 0
    for c in ciphertext:
        if c.isalpha():
            keyword_index = i % len(keyword)
            keyword_char = keyword[keyword_index]
            keyword_char_index = ord(keyword_char) - ord('A')
            if c.islower():
                plaintext += chr((ord(c) - ord('a') - keyword_char_index) % 26 + ord('a'))
            else:
                plaintext += chr((ord(c) - ord('A') - keyword_char_index) % 26 + ord('A'))
            i += 1
        else:
            plaintext += c
    return plaintext


# Take user input for ciphertext and keyword
ciphertext = input("Enter your ciphertext: ")
keyword = input("Enter your keyword: ")

# Decrypt the ciphertext using the Vigenere cipher and print the plaintext
plaintext = vigenere_decrypt(ciphertext, keyword)
print("Decrypted plaintext:", plaintext)
