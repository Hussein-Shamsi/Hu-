
import itertools
import string

english_words = {"BAD", "DOG", "CAT", "GOOD", "WORD", "HAT", "BAT"}

def is_english_word(word):
    return word.upper() in english_words

def decrypt_with_mapping(cipher_text, mapping):
    return ''.join(mapping[char] for char in cipher_text)

cipher_text = "ZQM"
cipher_text = ''.join([c for c in cipher_text if c.isalpha()])
used_letters = sorted(set(cipher_text))

attempts = 0

for perm in itertools.permutations(string.ascii_uppercase, len(used_letters)):
    mapping = dict(zip(used_letters, perm))
    decrypted = decrypt_with_mapping(cipher_text, mapping)
    attempts += 1

    if is_english_word(decrypted):
        print(f"Possible English word found: {decrypted}")
        print(f"Attempt number: {attempts}")
        break

print(f"Total attempts: {attempts}")
