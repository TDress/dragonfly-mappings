from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text)



grammar = Grammar("vimium")

window_rule = MappingRule(
	name = "window",
	mapping = {
    		# Tab navigation
    		'leaf left': Key("cs-tab"),
    		'leaf right': Key("c-tab"),
    		'leaf <n>': Key("c-%(n)d"),
    		'leaf new': Key("c-t"),
    		'leaf reopen': Key("cs-t"),
    		'leaf close': Key("c-w"),
    		'leaf fresh': Key("c-r"),
    		'leaf link': Key("f"),
    		'leaf link new': Key("s-f"),
    		'leaf bar': Key("c-l"),

	    	#  Moving around
    		'[<n>] slump': Key("j:%(n)d"),
    		'[<n>] boost': Key("k:%(n)d"),
    		'slump more': Key("c-d"),
    		'slump most': Key("pgdown"),
    		'boost more':  Key("c-u"),
    		'boost most':  Key("pgup"),
    		'leaf top': Key("escape, g, g"),
    		'leaf bottom': Key("escape, s-g"),
    		'[<n>] bump': Key("l:%(n)d"),
    		'[<n>] tug': Key("h:%(n)d"),
    		'leaf past': Key("a-left"),
    		'leaf future': Key("a-right"),
    
    		#  Searching
    		'braille <text>': Key("escape, slash") + Text("%(text)s") + Key("enter"),
    		'Vance': Key("escape, n"),
    		'rev': Key("escape, N"),

		#  page actions
    		'show page atoms': Key("g,s"),
    		'etch': Key("i"),
    		'etch <text>': Key("i") + Text("%(text)")
	},
    	extras = [
        	IntegerRef('n', 1, 99),
        	Dictation('text'),
    	],
    	defaults = {
		"n": 1
	}
)

grammar.add_rule(window_rule)
grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
