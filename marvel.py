xx = [["Marvel",["Avengers",["Iron Man","Captain America","Thor"]],["X-Men",    ["Wolverine","Cyclops","Storm"]]],["DC Comics",["Justice League",["Superman"    ,"Batman","Wonder Woman"]],["Teen Titans",["Robin","Starfire","Raven", "Cybo    rg", "Beast Boy"]]]]
  2 super = {}
  3
  4 for i in range(len(xx)):
  5     super[xx[i][0]] = {sub[0]:sub[1] for sub in xx[i][1:] }
  6
  7 print(super)

