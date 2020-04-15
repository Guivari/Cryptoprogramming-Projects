def encode(x):
    plSent = []
    sentence = x.split()
    for word in sentence:
        plSent.append((word[-1]+word[:-1]+'ay').lower())
    return ' '.join(plSent)

