from pprint import pprint
xx = [["Marvel",["Avengers",["Iron Man","Captain America","Thor"]],["X-Men",    ["Wolverine","Cyclops","Storm"]]],["DC Comics",["Justice League",["Superman"    ,"Batman","Wonder Woman"]],["Teen Titans",["Robin","Starfire","Raven", "Cybo    rg", "Beast Boy"]]]]
super = {}
for i in range(len(xx)):
    super[xx[i][0]] = {sub[0]:sub[1] for sub in xx[i][1:] }
pprint(super)

