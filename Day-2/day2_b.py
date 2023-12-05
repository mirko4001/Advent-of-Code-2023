f = open("Day-2/day2.txt")
inputData = [x.replace("\n", "").split(": ") for x in f.readlines()]
f.close()

result = 0

for i in inputData:
    gameId = i[0][5:]
    i.pop(0)
    tmpString = " ".join(map(str, i))
    tmpSubsets = tmpString.split("; ")
    subsetsRaw = []
    subsetsSorted = []
    for j in tmpSubsets:
        subsetsRaw.append(j.split(", "))

    for j in subsetsRaw:
        tmp = [0,0,0]
        for k in j:
            if "red" in k:
                k = k.replace(" red","")
                tmp[0] += int(k)
            elif "green" in k:
                k = k.replace(" green","")
                tmp[1] += int(k)
            else:
                k = k.replace(" blue","")
                tmp[2] += int(k)
        subsetsSorted.append(tmp)
    
    red = []
    green = []
    blue = []
    for x in subsetsSorted:
        red.append(x[0])
        green.append(x[1])
        blue.append(x[2])

    product = max(red)*max(green)*max(blue)
    result += product

print(result)