# Nomor 3
import re

x = open("Indonesia.txt", 'r', encoding='latin1')

text = x.read()
x.close()
y = r'di \w+'
tampilkan = re.findall(y,text)
print(tampilkan)
