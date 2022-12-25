initalString = [
 [0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0],
 [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0],
 [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0]
]

groups = [[ 1,  3,  5,  7,  9, 11, 13, 15],
    [ 2,  3,  6,  7, 10, 11, 14, 15],
    [ 4,  5,  6,  7, 12, 13, 14, 15],
    [ 8,  9, 10, 11, 12, 13, 14, 15],
]


def calculateBlockValue(parityBitIndex: int, block: list[bool]):

    blockIndecies = []
    blockIndecies = groups[parityBitIndex -1] 

    total = 0
    for index in blockIndecies:
        total += block[index]
    
    return total % 2 == 0

totalString = ""
for block in initalString:
    errors = []
    for i in range(1, 5):
        if not calculateBlockValue(i, block):
            errors.append(i)
    for bit in block:
        print(bit, end="")
    print("")

100000101100110101111000101110111 