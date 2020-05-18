count = 0
with open(file) as  f:
    for line in f:
        for word in line.split('with_my_delimiter'):
            if word == 'my_word':
                count = count + 1