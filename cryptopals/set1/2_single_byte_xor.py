import binascii

# the ord(' ') is the thing you're most likely to see in the string, a partial key.
# this one is looking for which string has the most spaces in it.
# WORKING
def decode_xor(hex_str):
    nums = binascii.unhexlify(hex_str)
    key = max(nums, key=nums.count) ^ ord(' ')
    result = ''.join(chr(num ^ key) for num in nums)
    print(result)

#open file
f = open("detect_single_byte_xor.txt", "r")
#f = open("test.txt", "r")
#for every line in the file
line_num = 1
lines = f.readlines()
for line in lines:
    print("================================================")
    print("LINE NUM: " + str(line_num))
    line_num += 1
    clean_line = line.strip()
    # xor with all single bytes up to 255. Get result with the most spaces
    decode_xor(clean_line)

#decode_xor("7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f")
# FOUND IT!
# Line 171: Now that the party is jumpin
