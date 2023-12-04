file = open("day1.txt")
inputData = [x.replace("\n", "") for x in file.readlines()]
file.close()

result = 0

for i in inputData:
    tmp = ""
    for j in i:
        if j.isdigit():
            tmp += j
            for k in i[::-1]:
                if k.isdigit():
                    tmp += k
                    result += int(tmp)
                    break
            break
        
print(result)