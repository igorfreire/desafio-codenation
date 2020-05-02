message='iq tmhq mximke nqqz etmyqxqee mnagf efqmxuzs sdqmf upqme. efqhq vane'
alphabet='abcdefghijklmnopqrstuvwxyz'
key=12
decrypt=''

for i in message:
    pos=alphabet.find(i)
    newpos=(pos-key)%26
    decrypt+=alphabet[newpos]
print(decrypt)
