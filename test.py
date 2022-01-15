import string


len_tab = 16
stringa = ''
for _ in range(4): stringa+=('{:<'+str(len_tab)+'}')

print(stringa.format(12, 12, 12, 12))