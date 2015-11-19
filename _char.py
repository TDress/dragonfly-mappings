from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text)

import lib.combination

grammar = Grammar("characters")

character_rule = MappingRule(
	name = "characters",
	mapping = {
            'bravo [<text>]': Key("b") + Function(lib.combination.executeCombo),
            'Charlie [<text>]':  Key("c") + Function(lib.combination.executeCombo),
            'Delta [<text>]':    Key("d") + Function(lib.combination.executeCombo),
            'Eli [<text>]':  Key("e") + Function(lib.combination.executeCombo),
            'foxtrot [<text>]':  Key("f") + Function(lib.combination.executeCombo),
            'George [<text>]':  Key("g") + Function(lib.combination.executeCombo),
            'Hank [<text>]':  Key("h") + Function(lib.combination.executeCombo),
            'Ike [<text>]':  Key("i") + Function(lib.combination.executeCombo),
            'Jake [<text>]':  Key("j"), + Function(lib.combination.executeCombo) 
            'kilo [<text>]':  Key("k"), + Function(lib.combination.executeCombo) 
            'Lima [<text>]':  Key("l"), + Function(lib.combination.executeCombo) 
            'Mike [<text>]':  Key("m"), + Function(lib.combination.executeCombo) 
            'Noah [<text>]':  Key("n") + Function(lib.combination.executeCombo),
            'Oscar [<text>]':  Key("o") + Function(lib.combination.executeCombo),
            'Papa [<text>]':  Key("p") + Function(lib.combination.executeCombo),
            '(Quintin | Quentin) [<text>]':  Key("q") +  Function(lib.combination.executeCombo),
            'Randy [<text>]':  Key("r") + Function(lib.combination.executeCombo),
            'Simon [<text>]':  Key("s") + Function(lib.combination.executeCombo),
            'tango [<text>]':  Key("t") + Function(lib.combination.executeCombo),
            'Udall [<text>]':  Key("u") + Function(lib.combination.executeCombo),
            'Victor [<text>]':  Key("v") + Function(lib.combination.executeCombo),
            'whiskey [<text>]':  Key("w") + Function(lib.combination.executeCombo),
            'x-ray [<text>]': Key("x") +  Function(lib.combination.executeCombo),
            'Yankee [<text>]':  Key("y") + Function(lib.combination.executeCombo),
            'Zulu [<text>]':  Key("z" + Function(lib.combination.executeCombo),
            # uppercase characters
            'Stout bravo [<text>]': Key("B") + Function(lib.combination.executeCombo),
            'Stout Charlie [<text>]':  Key("C") + Function(lib.combination.executeCombo),
            'Stout Delta [<text>]':    Key("D") + Function(lib.combination.executeCombo),
            'Stout Eli [<text>]':  Key("E") + Function(lib.combination.executeCombo),
            'Stout foxtrot [<text>]':  Key("F") + Function(lib.combination.executeCombo),
            'Stout George [<text>]':  Key("G") + Function(lib.combination.executeCombo),
            'Stout Hank [<text>]':  Key("H") + Function(lib.combination.executeCombo),
            'Stout Ike [<text>]':  Key("I") + Function(lib.combination.executeCombo),
            'Stout Jake [<text>]':  Key("J"), + Function(lib.combination.executeCombo) 
            'Stout kilo [<text>]':  Key("K"), + Function(lib.combination.executeCombo) 
            'Stout Lima [<text>]':  Key("L"), + Function(lib.combination.executeCombo) 
            'Stout Mike [<text>]':  Key("M"), + Function(lib.combination.executeCombo) 
            'Stout Noah [<text>]':  Key("N") + Function(lib.combination.executeCombo),
            'Stout Oscar [<text>]':  Key("O") + Function(lib.combination.executeCombo),
            'Stout Papa [<text>]':  Key("P") + Function(lib.combination.executeCombo),
            'Stout (Quintin | Quentin) [<text>]':  Key("Q") +  Function(lib.combination.executeCombo),
            'Stout Randy [<text>]':  Key("R") + Function(lib.combination.executeCombo),
            'Stout Simon [<text>]':  Key("S") + Function(lib.combination.executeCombo),
            'Stout tango [<text>]':  Key("T") + Function(lib.combination.executeCombo),
            'Stout Udall [<text>]':  Key("U") + Function(lib.combination.executeCombo),
            'Stout Victor [<text>]':  Key("V") + Function(lib.combination.executeCombo),
            'Stout whiskey [<text>]':  Key("W") + Function(lib.combination.executeCombo),
            'Stout x-ray [<text>]': Key("X") +  Function(lib.combination.executeCombo),
            'Stout Yankee [<text>]':  Key("Y") + Function(lib.combination.executeCombo),
            'Stout Zulu [<text>]':  Key("Z") + Function(lib.combination.executeCombo),

            },
        extras = [
            Dictation("text"),
            ],
        defaults = {
            "n":1,
            "text":''
            }
        )


grammar.add_rule(character_rule)
grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
