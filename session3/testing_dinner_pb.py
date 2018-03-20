dresses = [
    # List of dress designer and size
    ["Little Back dress", 6],
    ["Fluro green mini", 8],
    ["Fluro green mini", 6],
    ["Gold sparkling", 10],
    ["Animal print long sleeves", 10]
]

# oke so you want me to get the dresses that suite you
# by style and size
def get_dress(style, size):
    # so for start I am gonna assume that there is not
    # match for you
    matches = []
    # So now I am gonna go through all my dresses and save
    # the ones that suite you
    for dress in dresses:
        if dress[0] == style and dress[1] == size:
            matches.append(dress)

    # And now I need to get that dresses to you
    # so I am gonna return the matches list
    return matches

amys_matches = get_dress("Little Back dress", 6)

if len(amys_matches) > 0:
    print amys_matches
else:
    print "Sorry Amy no dress for you :("
