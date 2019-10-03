# take some text and compare it to english letter freq
import operator

englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_freq_analysis(line):
    result_dict = dict()
    total_num_letters = 0
    for ltr in line:
        ltr = ltr.upper()
        if ltr not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            pass
        elif ltr in result_dict:
            total_num_letters += 1
            result_dict[ltr] = result_dict[ltr] + 1
        else:
            total_num_letters += 1
            result_dict[ltr] = 1

    for item in result_dict:
        result_dict[item] = result_dict[item]/total_num_letters * 100
    return result_dict

test = "hello hello, one two three four, this is a test, testing"
result = get_freq_analysis(test)
sorted_x = sorted(result.items(), key=operator.itemgetter(1))
sorted_x.reverse()
print(sorted_x)
    
