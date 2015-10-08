from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text)

# vocabulary mapping of single command words to key string representations.
#  these are used in combination functions to retrieve key strokes.
# the command words are not necessarily usable in isolation,
# i.e. outside of combinations
keyVocabulary = {
        "paste": "escape,p",
        "indent": "equal,equal",
}

# combination functions for vim  commands
# each function describes combinations for a particular command.

def cleave_combo(text):
    keyArgumentString = ""
    words = str(text).split(" ")
    counter = 0
    for word in words:
        if word in keyVocabulary.keys() and counter == 0: 
            keyArgumentString += keyVocabulary[word]
        elif word in keyVocabulary.keys():
            keyArgumentString += "," + keyVocabulary[word]
        else:
            break
        ++counter
    Key(keyArgumentString).execute()



grammar = Grammar("vim")


#Navigation keys are preceded by the escape key.  for use of
#these keys in other contexts, we can create augmented commands.
#E.g. for a variable in PHP, our command will be Buck plus
#some formatted text. For inserting the  symbol alone,
#using press + <key> will suffice.

navigation_rule = MappingRule(
	name = "navigation",
	mapping = {
   		'(Buck | buck)': Key("dollar"),
	  	'zilch': Key("0"),
		'(Lance | lance)': Key("escape,a"),
		'(Lance | lance) end': Key("escape,A"),
                'scape': Key("escape"),
		'etch start': Key("escape,I"),
		'[<n>] dub': Key("w:%(n)d"), 
		'[<n>] (Hynde | hind)': Key("b:%(n)d"),
		'[<n>] nib': Key("e:%(n)d"), 
	},
	extras = [
		Dictation("text"),
		IntegerRef("n", 1, 20)
	],
	defaults = {
		"n": 1
	}
)

buffer_rule = MappingRule(
	name = "buffer",
	mapping = {
            'vim buffer next':  Key("escape") + Text(":bn") + Key("enter"), 
            'vim buffer previous': Key("escape") + Text(":bp") + Key("enter"),
            'vim buffer <n>': Key("escape") + Text(":b") + Key("%(n)d,enter"),
            'vim save': Key("escape") + Text(":w") +  Key("enter"),
            'vim save quit': Key("escape") + Text(":wq") +  Key("enter"),
            'vim quit': Key("escape") + Text(":q")+    Key("enter"),
            'vim quit bang': Key("escape") + Key("colon,q, exclamation, enter"),
            'vim save quit bang': Key("escape") + Key("colon,w,q, exclamation, enter"),
	},
	extras = [
		Dictation("text"),
		IntegerRef("n", 1, 20)
	],
	defaults = {
		"n": 1
	}
)

manipulation_rule = MappingRule(
	name = "manipulation",
	mapping = {
		'cull': Key("v"), 
		'cull block': Key("c-v"), 
		'(cleave | Cleve) up': Key("escape,O") + Function(cleave_combo),
                '(Cleve | cleave)': Key("escape,o") + Function(cleave_combo),
                '[<n>] shoot': Key("enter:%(n)d"),
		'lop': Key("d"),
                'lop dub [<n>]':  Key("d,%(n)d,w"),
                'lop nib [<n>]': Key("d,%(n)d,e"),
		'lop line': Key("d,d"), 
		'oust': Key("c"), 
                #'oust <text>': Key("c") +  Function(vim_movement), 
                'oust': Key("c"), 
                'paste': Key("p"),
                'paste front': Key("P"),
		'cleave up': Key("escape,O"),
   		'sub': Key("s"),
   		'sub line': Key("s-s"),
   		'swap': Key("r"),
   		'swap more': Key("s-r"),
                '[<n>] trim': Key("escape, x:%(n)d"),
                '[<n>] trim back': Key("escape, X:%(n)d")
	},
	extras = [
		Dictation("text"),
                IntegerRef("n", 1, 20)
	],
        defaults = {
                "n":  1
        }
)
 
grammar.add_rule(navigation_rule)
grammar.add_rule(manipulation_rule)
grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
