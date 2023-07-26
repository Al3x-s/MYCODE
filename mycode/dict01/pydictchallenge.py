comics= {
    'Marvel': {
        'Avengers': ['Iron Man', 'Captain America', 'Thor'],
        'X-Men': ['Wolverine', 'Cyclops', 'Storm']
    },
    'DC Comics': {
        'Justice League': ['Superman', 'Batman', 'Wonder Woman'],
        'Teen Titans': ['Robin', 'Starfire', 'Raven', 'Cyborg', 'Beast Boy']
    }
}

comics["prime"] = {'The Boys': ["Homelander", "A-Train"]}
x = []
bonus = {}



for keys,value in comics.items():
    x.append(keys)
for i in range(len(x)):
    bonus[str(i)] = comics[x[i]]
for keys,value in bonus.items():
    print(keys,value)


while True:
    intchoice = input("pick a number from the above value")
    if intchoice.isnumeric() and int(intchoice) <= (len(x)-1):
        intchoice = str(intchoice)
        print(f'you chose number {intchoice} that gives you {bonus[intchoice]}')
        break
    else:
        print("Thats not valid input")
while True:
    choice = input(f'Fom the following keys choose one {x}')
    if choice in x:
        print(comics[choice])
        break
    else:
        print("not in list")

