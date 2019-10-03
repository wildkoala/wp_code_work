

#WORKING

# INPUT: a key, and then a message, both of which must be strings.
# OUTPUT: a list of strings, which are hex encoded bytes.

# I should modify this so that it handles cases where the input is not a string, but a list of hex values.
# Solution was to make a bunch of different xor options, but this is kind of hacky.
def xor_with_key(key, msg):
    i = 0
    key_len = len(key)
    result_list = []
    for msg_ltr in msg:
        key_ltr = key[i%key_len]
        i += 1
        result_byte = ord(key_ltr) ^ ord(msg_ltr)
        result_list.append(hex(result_byte))
    return(result_list)

# INPUT: a key, and then a list of ints in any form.
# OUTPUT: a list of strings, which are hex encoded bytes.

def xor_hexlist_with_key(hexlist,key):
    i = 0
    key_len = len(key)
    result_list = []
    for hex_val in hexlist:
        key_ltr = key[i%key_len]
        i += 1
        result_byte = ord(key_ltr) ^ hex_val
        result_list.append(hex(result_byte))
    return(result_list)

def xor_string_of_hex_with_key(key, hexstr): #no 0x before hand, just a bunch of two hex character bytes, all together.
    hex_list = [hexstr[i:i+2] for i in range(0, len(hexstr), 2)] #convert it to list, and use prewritten function.
    index = 0
    for item in hex_list:
            hex_list[index] = int(item, 16)
            index += 1
    return xor_hexlist_with_key(key, hex_list)


def xor_bytes_file_with_key(bytes_file, key):
    i = 0
    key_len = len(key)
    b = open(bytes_file, "rb")
    vals = b.read()
    result_list = []
    for val in vals:
        key_ltr = key[i%key_len]
        i += 1
        result_byte = ord(key_ltr) ^ val
        result_list.append(result_byte)
    #print(result_list)
    final = hexlist_to_hexstr(result_list)
    return(final)
    

#WORKING

# INPUT: a list of strings representing hex encoded bytes
# OUTPUT: one long hex encoded string
# EXTRA INFO: every two hex characters is a byte, or one ascii character, after being decrypted

def hexlist_to_hexstr(hex_list):
    index = 0
    for item in hex_list:
        hex_list[index] = item.replace("0x", "")        
        if len(hex_list[index]) == 1:
            hex_list[index] = hex_list[index].zfill(2)
        index += 1        
    return "".join(hex_list)
    
#Working Test
#hex_list = xor_with_key("ICE", "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal")
#final = hexlist_to_hexstr(hex_list)


# WORKING

# encrypted_msg must be a string, with two hex characters representing one ascii chr
# it is NOT preceeded by 0x
# ex. "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
# when that's XOR'ed with "ICE", you get back the original text-
# Burning 'em, if you ain't quick and nimble
# I go crazy when I hear a cymbal

def decrypt_xored_words(encrypted_msg, key):
    result = xor_string_of_hex_with_key(key, encrypted_msg)
    #must now convert results into a string
    ltr_list = []
    for num in result:
        ltr_list.append(chr(int(num,16)))
    return "".join(ltr_list)

# Working test
# x=decrypt_xor("ICE", "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f")

# I can make the function below better by adding in some common file signatures and
# checking to see if the bytes satify those conditions.
# maybe then I can just save it as that file type and the original file
# will be reconstructed?

def decrypt_xored_txtfile(encrypted_file_path, key):
    f = open(encrypted_file_path, "r")
    line = f.readline()
    f.close()
    result = xor_string_of_hex_with_key(key, line)
    #give back the bytes, without converting them to characters.
    ltr_list = []
    for num in result:
        ltr_list.append(hex(int(num,16)))
    f = open("DECRYPTED.txt", "w")
    f_str = "".join(ltr_list)
    f.write(f_str.encode())
    f.close()
    #print("DECRYPTED file has been created!")

'''
x = decrypt_xored_txtfile("encrypted.txt","A")
hex_string = hexlist_to_hexstr(x)
f = open("DECRYPTED_FILE.txt", "wb")
print("DECRYPTED_FILE.txt has been writen!")
f.write(hex_string.encode())
f.close()
'''

def decrypt_xored_imgfile(encrypted_file_path, key):
    f = open(encrypted_file_path, "rb")
    data = f.read()
    f.close()
    result = xor_string_of_hex_with_key(key, line)
    #give back the bytes, without converting them to characters.
    ltr_list = []
    for num in result:
        ltr_list.append(hex(int(num,16)))
    f = open("DECRYPTED_FILE", "wb")
    f_str = "".join(ltr_list)
    f.write(f_str.encode())
    f.close()
    #print("DECRYPTED file has been created!")

