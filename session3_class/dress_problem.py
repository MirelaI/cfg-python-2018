dresses = [
    ["LBD", 6],
    ["Fluro green mini", 8],
    ["Gold sparkly", 6],
    ["Animal print long sleeves", 10],
    ["Maxi twitter blue", 8]
]

def get_dress(style, size):
    matches = []
    for dress in dresses:
        if dress[0] == style and dress[1] == size:
            matches.append(dress)

    return matches

amy_matches = get_dress("Hot PINK Number", 8)
if len(amy_matches) > 0:
    print amy_matches
else:
    print "Sorrryy NO dress for you :(."
