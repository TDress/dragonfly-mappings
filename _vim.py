from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text)



grammar = Grammar("vim")


navigation_rule = MappingRule(
	name = "navigation",
	mapping = {
   		'(Buck | buck)': Key("dollar"),
	   	'zilch': Key("0"),
		'(cleave | Cleve)': Key("escape,o"),
		'cleave up': Key("O"),
		'(Lance | lance)': Key("a"),
		'(Lance | lance) end': Key("A"),
		'etch start': Key("I"),
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
            'vim buffer next': Text(":bn") + Key("enter"), 
            'vim buffer previous': Text(":bp") + Key("enter"),
            'vim buffer <n>': Text(":b") + Key("%(n)d,enter"),
            'vim save': Text(":w") +  Key("enter"),
            'vim save quit': Text(":wq") +  Key("enter"),
            'vim quit': Text(":q")+    Key("enter"),
            'vim quit bang': Key("colon,q, exclamation, enter"),
            'vim save quit bang':Key("colon,w,q, exclamation, enter"),
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
		'lop': Key("d"),
                'lop dub [<n>]':  Key("d,%(n)d,w"),
                'lop nib [<n>]': Key("d,%(n)d,e"),
		'lop line': Key("d,d"), 
		'oust': Key("c"), 
                #'oust <text>': Key("c") +  Function(vim_movement), 
                'oust': Key("c"), 
   		'sub': Key("s"),
   		'sub line': Key("s-s"),
   		'swap': Key("r"),
   		'swap more': Key("s-r"),
	},
	extras = [
		Dictation("text")
	]
)
 
grammar.add_rule(navigation_rule)
grammar.add_rule(manipulation_rule)
grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
