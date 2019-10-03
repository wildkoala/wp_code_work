import hashlib

# right now this only cracks MD5. I want to extend functionailty to attack more.
# the hashes im using might not come in a format that I can check properly.


# crack md5 hashes, as long as they are in the same format that python puts out...
# encrypted_word variable is a string.
def md5_dict_attack(encrypted_word, dictionary_file):
    encrypted_word = encrypted_word.strip()
    dictionary = open(dictionary_file, 'r')
    for word in dictionary:
        word = word.strip()
        potential_pass = hashlib.md5(word.encode())
        potential_pass = potential_pass.digest()
        if str(potential_pass) == encrypted_word:
            print("[+] Password: " + word + " MD5 hash: "+ encrypted_word)
            return
    print("[-] Password not in dictionary for MD5 hash " + encrypted_word)


# Run the dictionary attack on every word in the encrypted file
def crack(encrypted_pw_file, dictionary_file):
    try:
        
        encrypted_pws = open(encrypted_pw_file, 'r')
        for encrypted_byte_str in encrypted_pws:
            md5_dict_attack(encrypted_byte_str, dictionary_file)
            
    except FileNotFoundError:
        print("Could not open that file")
            

    
    

# Get the file to crack and the dictionary you want to use.
encrypted_pws_file = input("Please provide the encrypted password file\n")

#parse out the quotes in file name
encrypted_pws_file = encrypted_pws_file[1:len(encrypted_pws_file)-1]
dictionary_file = input("Please provide the dictionary file you wish to use.\n")
dictionary_file = dictionary_file[1:len(dictionary_file)-1]

#crack all the passwords
crack(encrypted_pws_file, dictionary_file)

