# Step 1: array of dresses and print each item
# make the array of just the items
# Defined a list of dresses so I can show them to Amy
# dresses = [
#     "LBD", 6,
#     "Fluro green mini",
#     "Gold sparkly long",
#     "Animal print long sleeves",
#     "Maxi twitter blue"
# ]

# for item in dresses:
#    print item

# Step 2: Sizes
# dresses = [
#     # Talk about arrays of array
#     ["LBD", 6],
#     ["Floral green mini", 8],
#     ["Mini super green dress", 10]
# ]
# Do not print anything here.
# Explain: so let's assume we know nothing about this array in arrays
# then we would define dresses = ["lbd", 6, "a", 8]
# From the structure above is quite hard to associate that 6
# is the size of LBD. So we need to group them together, hence the use
# or inner arrays.

# Step 3: Make a nice method to get dresses by size and style
# What size r u and which dress you fancy.
dresses = [
    # List of dress designer and size
    ["Little Back dress", 6],
    ["Fluro green mini", 8],
    ["Fluro green mini", 6],
    ["Gold sparkling", 10],
    ["Animal print long sleeves", 10]
]

# Oke so you want me to get the dresses that suite you
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



