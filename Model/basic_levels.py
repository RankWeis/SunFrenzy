"""
Eventually need to create some sort of level editor.
For simplicity, array string of nxm size can be used.
W = wall
G = ground (could be wall I guess)
B = Block, could be more descriptive later
I = invisible block, somehow need to feed in conditions, but for now can be on all enemies killed
E = Enemy
S = Starting Position
"""
"""
level1 - First level is not side scrolling, to get things up and running. 

For this level, I am assuming we can jump two x blocks, sprint 5.
I don't want to assume we can jump y=2 AND x=2, but that also means 
"""
level1 = [
"WWWWWWWWWWWWWWWWWWWW",
"W                    W",
"W                    W",
"W F   E              W",
"W  BBBBB   II   BB   W",
"W                    W",
"W                  BBW",
"W  S                 W",
"WGGGGGG  GGG     GGW",
"WGGGGGG  GGG     GGW",
"WGGGGGG  GGG     GGW"
]
