# write a prpgram to find out  the line number where present froem question 6

with open("log.txt") as f:
    lines=f.readlines()

lineno=1
for line in lines:
    if("python" in line):
        print(f"Yes python is present. line no {lineno}")
        break
    lineno +=1
else:
    print("No python is not present.")
       