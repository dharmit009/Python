
dicA = {
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
        0:'zero',

        }

def get_value(oneKey):
    return dicA[oneKey];

for x in sorted(dicA, reverse=True, key=get_value):
    print(dicA[x])
    
