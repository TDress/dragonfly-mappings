from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text)

import lib.combination

grammar = Grammar("vimium")

window_rule = MappingRule(
	name = "window",
	mapping = {
    		# Tab navigation
    		'browse back': Key("cs-tab"),
    		'browse next': Key("c-tab"),
    		'browse <n>': Key("c-%(n)d"),
    		'browse new': Key("c-t"),
    		'revive': Key("cs-t"),
                'gash <n>': Key("c-tab,c-w:%(n)"),
    		'gash': Key("c-w"),
    		'refresh': Key("c-r"),
    		'address': Key("c-l"),

	    	#  Moving around
    		'slump more': Key("c-d"),
    		'slump most': Key("pgdown"),
    		'boost more':  Key("c-u"),
    		'boost most':  Key("pgup"),
    		'top': Key("escape, g, g"),
    		'bottom': Key("escape, s-g"),
    		'(passed | past)': Key("a-left"),
    		'future': Key("a-right"),
    
    		#  Searching
    		'braille <text>': Key("escape, slash") + Text("%(text)s") + Key("enter"),
    		'<n> Noah': Key("%(n)d, n"),
    		'[<n>] rev': Key("%(n)d, N"),

		#  page actions
                'scope': Key('f'),
    		'show page atoms': Key("g,s"),
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
