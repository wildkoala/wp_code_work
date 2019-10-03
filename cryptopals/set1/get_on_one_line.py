

f = open("xored_then_base64.txt", "r")
lines = f.readlines()
final = ''
for l in lines:
    final += l.strip()
print(final)
