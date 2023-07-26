xx = [
  [
    "Marvel",
    [
      "Avengers",
      [
        "Iron Man",
        "Captain America",
        "Thor"
      ]
    ],
    [
      "X-Men",
      [
        "Wolverine",
        "Cyclops",
        "Storm"
      ]
    ]
  ],
  [
    "DC Comics",
    [
      "Justice League",
      [
        "Superman",
        "Batman",
        "Wonder Woman"
      ]
    ],
    [
      "Teen Titans",
      [
        "Robin",
        "Starfire",
        "Raven",
        "Cyborg",
        "Beast Boy"
      ]
    ]
  ]
  ]
cap = xx[0][1][1][1]
wol = xx[0][2][1][0]
print(f'my favorite avenger is {cap}')
print(f'my favorite x-man is {wol}')
teen = xx[1][2][1]
print(f'Here is a list of my favorite teen titans {teen[-3:]}')
