import csv

totalVotes = {
    "julenissen": 0,
    "alvekongen": 0,
    "sneglulf": 0
}

actions = dict()
with open("slemmehandlinger.txt", "r") as f:
    reader = csv.reader(f, delimiter=":")
    actions = {rows[0]:rows[1] for rows in reader}

votes = dict()
with open("stemmer.txt", "r") as f:
    reader = csv.reader(f, delimiter=":")
    for row in reader:
        weight = 1.0
        for action in row[0].split(","):
            if action not in actions.keys():
                continue
            if float(actions[action]) < weight:
                weight = float(actions[action])
        current = totalVotes.get(row[1]) 
        totalVotes.update({row[1]: current + 1.0 *weight})


ans = round(totalVotes.get("julenissen") - totalVotes.get("alvekongen"))
print(ans)