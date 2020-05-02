#alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabets = "abcdefghijklmnopqrstuvwxyz"
input_str = "iq tmhq mximke nqqz etmyqxqee mnagf efqmxuzs sdqmf upqme. efqhq vane"
shift = 12

no_of_itr = len(input_str)
output_str = ""

for i in range(no_of_itr):
    current = input_str[i]
    loc = alphabets.find(current)
    if loc < 0:
        output_str += input_str[i]
    else:
        newLoc = (loc + shift)%26
        output_str += alphabets[newLoc]

print (output_str)
