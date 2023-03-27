input = "aabbbbeeeeffggg"
freq = {}
for i in input:
    if i in freq:
        freq[i]+= 1
    else:
        freq = 1
