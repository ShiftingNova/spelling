def replace(file,spelling):
    content = file.readlines()
    miss = []
    suggestion = []
    print("\n--- OUTPUT ---")
    count = 0
    for line in content:
        for key in spelling:
            if key in line:
                count += 1
                suggestion = line.split(key)
                fill = spelling[key]
                print(suggestion[0], fill, suggestion[1].replace("\n", ""))
                miss.append(key)
def suggest(file,spelling):
    content = file.readlines()
    miss=[]
    suggestion = []
    print("\n--- OUTPUT ---")
    count = 0
    for line in content:
        for key in spelling:
            if key in line:
                count+=1
                suggestion = line.split(key)
                fill = "("+str(count)+")"
                print(suggestion[0],key,fill,suggestion[1].replace("\n",""))
                miss.append(key)
    print("\n--- LEGEND ---")
    e=0
    for i in miss:
        e+=1
        print("(",str(e),")",spelling[i])
file_name = str(input("Enter a file name\n"))
file = open(file_name,'r')
spelling = open('misspellings.txt','r')
count = len(open("misspellings.txt").readlines())
misspellings = {}
pair = []
for i in spelling:
    pair = i.split("->")
    misspellings[pair[0]] = (pair[1]).replace("\n","")
mode = input("Enter spellcheck mode (replace or suggest):\n")
if mode.lower() == "replace":
    replace(file,misspellings)
elif mode.lower() == "suggest":
    suggest(file,misspellings)
else:
    print("bruh",mode,"isn't a mode")
