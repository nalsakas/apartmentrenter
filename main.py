import math

# Blocks of apartments
# Some apartments have targets in bloks, some don't
blocks = [
    {
        "gym": False,
        "school": True,
        "store": False,
    },
    {
        "gym": True,
        "school": False,
        "store": False,
    },
    {
        "gym": True,
        "school": True,
        "store": False,
    },
    {
        "gym": False,
        "school": True,
        "store": False,
    },
    {
        "gym": False,
        "school": True,
        "store": True,
    },
]

# Targets
reqs = ["gym", "school", "store"]

# Calculate distance of each reqs for all blocks
# i = current block
res = [None] * len(blocks)
for i in range(len(blocks)):

    # Calculate nearest reqs array for each block
    lengths = [math.inf] * len(reqs)

    # search reqs[j] in all blocks for blocks[i]
    # j = current reqs
    for j in range(len(reqs)):

        # loop over blocks to calculate distance for current j and i.
        k = 0
        while k < len(blocks):
            if blocks[k].get(reqs[j]):     # can't put a function into an [index]. So use get()
                if abs(i -k) < lengths[j]:
                    lengths[j] = abs(i - k)
            k += 1
    # save result in res[i]
    res[i] = lengths

# select max distance for any reqs member for all blocks
# convert list[list[int]] --> list[int]
# selected member chooses max walk distance for any given block
res = list(map(lambda x: max(x), res))

# Minimum of the walk distance? Which block? How long?
smallest = [math.inf, math.inf]
for i in range(len(res)):
    if res[i] < smallest[0]: # min walk distance?
        smallest[0] = res[i]
        smallest[1] = i      # which block?  

print(f"Block {smallest[1]}, max walk distance {smallest[0]}")