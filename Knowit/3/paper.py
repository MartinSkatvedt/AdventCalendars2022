import csv

total = 0
with open("pakker.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        width = int(row[0]) 
        height = int(row[1])
        length = int(row[2])

        # a=bredde b=høyde c=lengde
        h_1 = width * 2 + height * 2
        w_1 = height + length
        # acb
        h_2 = width * 2 + length * 2
        w_2 = length + height
        # bac
        h_3 = height * 2 + width * 2
        w_3 = width + length
        # bca
        h_4 = height * 2 + length * 2
        w_4 = length + width
        # cab
        h_5 = length * 2 + width * 2
        w_5 = width + height
        # cba
        h_6 = length * 2 + height * 2
        w_6 = height + width

        areas = [
            (h_1 , w_1),
            (h_2 , w_2),
            (h_3 , w_3),
            (h_4 , w_4),
            (h_5 , w_5),
            (h_6 , w_6),
        ]

        smallest = float("Inf")
        for pair in areas:
            if pair[0] <= 110 and pair[1] < smallest:
                smallest = pair[1]
            if pair[1] <= 110 and pair[0] < smallest:
                smallest = pair[0] 

        total += smallest


print(total)
