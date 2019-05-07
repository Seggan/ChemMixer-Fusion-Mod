from json import load,dump
modded_compounds={}
modded_reactions={
    "he+h":{
            "reactants":["helium","hydrogen"],
            "temp max":3500,
            "temp min":3499,
            "results":["lithium"]
            },
    "li+li":{
            "reactants":["lithium"],
            "temp max":3500,
            "temp min":3499,
            "results":["oxygen"]
            },
    "o+h":{
            "reactants":["hydrogen","oxygen"],
            "temp max":3500,
            "temp min":3499,
            "results":["nitrogen"]
            },
    "n+o":{
            "reactants":["oxygen","nitrogen"],
            "temp max":3500,
            "temp min":3499,
            "results":["aluminum"]
            },
    "o+o":{
            "reactants":["oxygen"],
            "temp max":3500,
            "temp min":3499,
            "results":["sulfur"]
            },
    "n+n":{
            "reactants":["nitrogen"],
            "temp max":3500,
            "temp min":3499,
            "results":["chlorine"]
            },
    "s+h":{
            "reactants":["sulfur","hydrogen"],
            "temp max":3500,
            "temp min":3499,
            "results":["chlorine"]
            },
    "h+h":{
            "reactants":["hydrogen"],
            "temp max":3500,
            "temp min":3499,
            "results":["helium"]
            },
    }
with open("reactions.json",'r') as f:
    reactions=load(f)
reactions.update(modded_reactions)
with open("reactions.json",'w') as f:
    dump(reactions,f)
    
