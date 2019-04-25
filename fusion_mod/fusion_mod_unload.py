from json import load,dump
def dict_reduce(parent_dict, child_dict):
    for key in child_dict.keys():
        del parent_dict[key]
    return parent_dict
modded_compounds={}
modded_reactions={
    "h+h":{
            "reactants":["hydrogen"],
            "temp max":3500,
            "temp min":3499,
            "results":["helium"]
            },
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
            }
    }
with open("reactions.json",'r') as f:
    reactions=load(f)
reactions=dict_reduce(reactions,modded_reactions)
with open("reactions.json",'w') as f:
    dump(reactions,f)
    
