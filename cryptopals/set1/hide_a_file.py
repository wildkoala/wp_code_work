from cycling_xor import hexlist_to_hexstr, xor_hexlist_with_key, decrypt_xored_file

# I am trying to encrypt things with the new xor encryption I've devised. I wonder if I can hide a picture from ring weekend?
# I need to pick a key for it.
# I guess this wont be susceptible to freq analysis attacks, bc it's not english, just bytes for a photo... hmm.



# INPUT: Takes path to file, and a key as arguments. They must both be strings.
# OUTPUT: creates a text file with a a single line of encoded bytes.

# Currently this isn't encrypting, just writing the bytes to a new text file.
def encrypt_file(path_to_file, key):
    
    # open the file and read it as binary data
    hex_list = []
    with open(path_to_file, 'rb') as f:
        contents = f.read()
        for byte in contents:
            hex_list.append(hex(byte))
        f.close()

    # get the bytes into a two hex character format and write it to a text file.
    result = hexlist_to_hexstr(hex_list)
    f = open("hexstring.txt","wb")
    f.write(result.encode())
    f.close()
    print("hexstring.txt has been created!")

    # encrypt
    f = open("hexstring.txt","rb")
    lines = f.readlines()
    f.close()
    for line in lines: # and there should just be one
        
        # split into list of strings that are correct hex values
        byte_list = [line[i:i+2] for i in range(0, len(line), 2)]
        # change them into ints to be xor'ed
        index = 0
        for item in byte_list:
            byte_list[index] = int(item, 16)
            index += 1
        #print(byte_list)
        enc = xor_hexlist_with_key(key, byte_list)
        string_version = hexlist_to_hexstr(enc)
        #print(string_version)

    #write encrpyted bytes to a new file
    f = open("encrypted.txt","wb") #changed to 2 for testing
    f.write(string_version.encode())
    f.close()
    print("encrypted.txt has been created!")

encrypt_file("Ring Weekend.jpg", "A")
decrypt_xored_file("encrypted.txt","A")
