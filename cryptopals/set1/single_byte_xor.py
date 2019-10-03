import binascii

def single_byte_xor_check():
    hex_str = input("Please enter your hexstring:\n")

    # break into bytes
    byte_str = binascii.unhexlify(hex_str)

    #print(nums) # prints as a byte string
    possible_strings = []

    # for every value in range 1 to 255, xor every byte, join them all
    for num in range(1,256):
        result = ''
        for byte in byte_str:
            result_byte = num ^ byte
            result += chr(result_byte)
        if result.isprintable():
            possible_strings.append(result)
    return possible_strings
        
englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getItemAtIndexZero(x):
    return x[0]

def getLetterCount(message):
    # Returns a dictionary with keys of single letters and values of the
    # count of how many times they appear in the message parameter.
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1
    return letterCount

def getFrequencyOrder(message):
    # Returns a string of the alphabet letters arranged in order of most
    # frequently occurring in the message parameter.
    # first, get a dictionary of each letter and its frequency count
    letterToFreq = getLetterCount(message)
    freqToLetter = {}
    for letter in LETTERS:
        if letterToFreq[letter] not in freqToLetter:
            freqToLetter[letterToFreq[letter]] = [letter]
        else:
            freqToLetter[letterToFreq[letter]].append(letter)

# third, put each list of letters in reverse "ETAOIN" order, and then
# convert it to a string

    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])

# fourth, convert the freqToLetter dictionary to a list of tuple
# pairs (key, value), then sort them

    freqPairs = list(freqToLetter.items())
    freqPairs.sort(key=getItemAtIndexZero, reverse=True)
    
# fifth, now that the letters are ordered by frequency, extract all
# the letters for the final string
    freqOrder = []
    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])
        return ''.join(freqOrder)

def englishFreqMatchScore(message):
# Return the number of matches that the string in the message
# parameter has when its letter frequency is compared to English
# letter frequency. A "match" is how many of its six most frequent
# and six least frequent letters is among the six most frequent and
# six least frequent letters for English.
    freqOrder = getFrequencyOrder(message)
    matchScore = 0
# Find how many matches for the six most common letters there are.
    for commonLetter in ETAOIN[:6]:
        if commonLetter in freqOrder[:6]:
            matchScore += 1
# Find how many matches for the six least common letters there are.
    for uncommonLetter in ETAOIN[-6:]:
        if uncommonLetter in freqOrder[-6:]:
            matchScore += 1
    return matchScore


# xor with all single bytes up to 255. Get possible results
possibly_xored_strings = single_byte_xor_check()

# go through the results, and get a frequency analysis of letters
index = 0
for string in possibly_xored_strings:
    
    index += 1
    string_score = englishFreqMatchScore(string)
    
    # see which ones most closely match English
    if string_score > 0:
        print(str(index) + ": " + string)


