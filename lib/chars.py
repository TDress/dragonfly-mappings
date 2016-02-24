# character mappings

from dragonfly import (Key, Text)

import lib.format

charMapping = {
        'alpha':"a",
        'bravo':"b",
        'charlie': "c",
        'delta':   "d",
        'eli': "e",
        'foxtrot': "f",
        'george': "g",
        'hank': "h",
        'ike': "i",
        'jake': "j", 
        'kilo': "k", 
        'key low': "k",
        'lima': "l", 
        'mike': "m", 
        'noah': "n",
        'oscar': "o",
        'paris': "p",
        'quentin': "q",
        'quintin': "q",
        'randy': "r",
        'simon': "s",
        'tango': "t",
        'udall': "u",
        'victor': "v",
        'whiskey': "w",
        'x-ray':"x",
        'yankee': "y",
        'zulu': "z",
        # uppercase characters
        'stout alpha': 'A',
        'stout bravo':"B",
        'stout charlie': "C",
        'stout delta':   "D",
        'stout eli': "E",
        'stout foxtrot': "F",
        'stout george': "G",
        'stout hank': "H",
        'stout ike': "I",
        'stout jake': "J", 
        'stout kilo': "K", 
        'stout lima': "L", 
        'stout mike': "M", 
        'stout noah': "N",
        'stout oscar': "O",
        'stout paris': "P",
        'stout quentin': "Q",
        'stout quintin': "Q",
        'stout randy': "R",
        'stout simon': "S",
        'stout tango': "T",
        'stout udall': "U",
        'stout victor': "V",
        'stout whiskey': "W",
        'stout x-ray':"X",
        'stout yankee': "Y",
        'stout zulu': "Z"

    }

def bashFlagText(text): 
    newText = lib.format.strip_dragon_info(text).lower()
    if newText in charMapping.keys(): 
        Key(charMapping[newText]).execute()
    else:
        Text("%(text)s").execute({"text": newText})
