# this can encrypt anything with a key! #wait, text too. ANY FILE.

import argparse

def xor_bytes_with_key(b_file, key):
    
    #open file
    bytez = open(b_file, 'rb')
    bytez_read = bytez.read()
    bytez.close()

    #encrypt by xor'ing
    i = 0
    key_len = len(key)
    result_list =[]
    for b in bytez_read: #individual bytes are ints
        #print(b)
        key_ltr = key[i%key_len]
        i += 1
        result_byte = ord(key_ltr) ^ b
        result_list.append(result_byte)

    
    #write these to a file
    f = open('XORRED', 'wb')
    f.write(bytes(result_list))
    f.close()
    print("The input file has been xorred and the XORRED file has been created!", end="")
    

'''
EXECUTION:

# Convert picture to bytes and save to generic file
# if you just change the extension to whatever filetype the image is
# then you will get back the original picture, but I'm going to end up
# trying to write a function to predict this, checking the beginning against
# common file signatures

pic_to_bytes("Ring Weekend.jpg")

# xor the bytes with a given string, make a file out of it.
xor_bytes_with_key(b, key)

# take that encrypted file, xor every byte with the same key, make file out of it

# Convert bytes back to image
bytes_to_pic("ENCODED_IMG")

'''

# =====================================================
# Handle Arguments
# =====================================================

parser = argparse.ArgumentParser()
parser.add_argument("file", help="the file to be xorred")
parser.add_argument("key", help="the string that will be used to xor")
args = parser.parse_args()

print(args)

xor_bytes_with_key(args.file, args.key)
