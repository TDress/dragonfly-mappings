from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text, Function)

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
    keyArgumentString =  ""
    words = str(text).split(" ")
    print words
    print text
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
                '[<n>] page up': Key("pgup:%(n)d"),
                '[<n>] page down': Key("pgdown:%(n)d"),
                '[<n>] code future':  Key("c-i"),
                '[<n>] code past':  Key("c-o"),
                'code help search':  Text(":helpgrep "),
                'code list errors': Text(":clist") +  Key("enter"),
                '(Lance | lance)': Key("escape,a"),
		'(Lance | lance) end': Key("escape,A"),
                'scape': Key("escape"),
		'etch start': Key("escape,I"),
		'[<n>] dub': Key("%(n)d,w"), 
		'[<n>] (Hynde | hind)': Key("%(n)d,b"),
		'[<n>] nib': Key("%(n)d,e"), 
	},
	extras = [
		Dictation("text"),
		IntegerRef("n", 1, 9)
	],
	defaults = {
		"n": 1
	}
)

buffer_rule = MappingRule(
	name = "buffer",
	mapping = {
            'code buffer next':  Key("escape") + Text(":bn") + Key("enter"), 
            'code buffer previous': Key("escape") + Text(":bp") + Key("enter"),
            'code buffer <n>': Key("escape") + Text(":b") + Key("%(n)d,enter"),
            'code save': Key("escape") + Text(":w") +  Key("enter"),
            'code save quit': Key("escape") + Text(":wq") +  Key("enter"),
            'code quit': Key("escape") + Text(":q")+    Key("enter"),
            'code quit bang': Key("escape") + Key("colon,q, exclamation, enter"),
            'code save quit bang': Key("escape") + Key("colon,w,q, exclamation, enter"),
            'code edit':Key("escape") +  Key("colon,e,space")
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
                '[<n>] jump right': Key("rangle:2"),
                '[<n>] jump left': Key("langle:2"),
                '[<n>] shoot': Key("enter:%(n)d"),
		'lop': Key("d"),
                'lop dub [<n>]':  Key("d,%(n)d,w"),
                'lop nib [<n>]': Key("d,%(n)d,e"),
		'lop line': Key("d,d"), 
		'oust': Key("c"), 
                #'oust <text>': Key("c") +  Function(vim_movement), 
                'oust': Key("c"), 
                'paste': Key("p"),
                'paste bump': Key("P"),
                'redo': Key("cs-r"),
   		'sub': Key("s"),
   		'sub line': Key("s-s"),
   		'swap': Key("r"),
   		'swap more': Key("s-r"),
                'top off': Key("cs-p"),
                '[<n>] trim': Key("escape, x:%(n)d"),
                '[<n>] trim back': Key("escape, X:%(n)d"),
                'undo': Key("escape,u"),
                'yank': Key("y"),
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
