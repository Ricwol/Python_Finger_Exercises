# Finger exercise, p.143
# Remedy the problem described in the previous paragraph.
# Hint: a simple way to do this is to create a new book by appending something
# to the original book.

import string

# Amend all printable ascii characters at the end of the book
new_book = (lambda book: book + string.printable)

# Use lambda expression to create a code generator based on first appearence
# Mapping individual, unique letters of plaintext to index number
gen_code_keys = (lambda book, plain_text:
                 {c: str(book.find(c)) for c in plain_text})

# Slicing operator at the end to remove the first '*' at the beginning
encoder = (lambda code_keys, plain_text:
           "".join(["*" + code_keys[c] for c in plain_text])[1:])


# Encrypt plain_text by giving the encoder a book for indexing
encrypt = (lambda book, plain_text:
           encoder(gen_code_keys(book, plain_text), plain_text))


# Finger exercise, p.143
# Using encoder and encrypt as models, implement the functions decoder and
# decrypt. Use them to decrypt the message which was encrypted using the
# opening of Don Quixote.

Don_Quixote = "In a village of La Mancha, the name of which I have no " \
    "desire to call to mind, there lived not long since one of those " \
    "gentlemen that keep a lance in the lance-rack, an old buckler, a lean " \
    "hack, and a greyhound for coursing."


# Decode this cipher
cipher = "22*13*33*137*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*137*" \
         "59*11*23*11*1*57*6*173*7*11"

# Decode key generator as described on p.142
gen_decode_keys = (lambda book, cipher:
                   {c: book[int(c)] for c in cipher.split("*")})


# Implement decoder by looping through all numbers in cipher
decoder = (lambda decode_keys, cipher:
           "".join((decode_keys[c] for c in cipher.split("*"))))


# Decrypting the cipher analog to encrypt function
decrypt = (lambda book, cipher:
           decoder(gen_decode_keys(book, cipher), cipher))

# Decrypt cipher using Don Quixote as book cipher
plain_text = decrypt(Don_Quixote, cipher)

# Cipher reads 'comprehension is incromprehensible' in plain text
print(plain_text)

# Plain text contains letters not existing in book
plain_text = "no joke, Abraham Boston had sex. No one saw it Q!"
# Create new book to account for non-existing characters
new_book = new_book(Don_Quixote)
cipher = encrypt(new_book, plain_text)
print(cipher)
print(decrypt(new_book, cipher))
