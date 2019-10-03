
# WORKING

# INPUT: Two integers
# OUTPUT: Hamming Distance between the two
# finds how many different bits there are between two integers.

def int_hamming_dist(x,y):
    result = 0
    xor_result = str(bin(x ^ y))[2:]
    for num in xor_result:
        if num == "1":
            result += 1
        else:
            pass
    #print(result) # uncomment to see value.
    return result

            
# WORKING

# INPUT: Two strings
# OUTPUT: Hamming Distance between the two
# finds how many different bits there are between two strings.
# it calls int_hamming_dist, so you need that function.

def str_hamming_dist(s1,s2):
    if len(s1) != len(s2):
        print("Lengths not equal")
        return
    else:
        i = 0
        ham_dist = 0
        for ltr in s1:
            val_1 = ord(ltr)
            val_2 = ord(s2[i])
            ham_dist += int_hamming_dist(val_1, val_2)
            i += 1
        #print(ham_dist) # uncomment to see value.
        return ham_dist



#str_hamming_dist("this is a test", "wokka wokka!!!")
















