from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text, Function)

import lib.combination

# vocabulary mappings of single command words to key string representations.
#  these are used in combination functions to retrieve key strokes.
# the command words are not necessarily usable in isolation,
# i.e. outside of combinations

# vocabulary mappings for vim  normal mode
nmodeVocabulary = {
        "paste": "p",
        "indent": "equal,equal",
        "dub": "w",
        "nib": "e",
        "slump": "j",
        "boost": "k",
        "leave top": "g,g",
        "leaf bottom": "G",
}

# vocabulary mappings for vim visual mode
vmodeVocabulary = {
        "dub": "w",
        "nib": "e",
        "slump": "j",
        "boost": "k",
        "leaf top": "g,g",
        "leaf bottom": "G",
} 


# functions to determine the vim mode of a combination

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
                '[<n>] buff future':  Key("c-i"),
                '[<n>] buff past':  Key("c-o"),
                'buff help search':  Text(":helpgrep "),
                'buff list errors': Text(":clist") +  Key("enter"),
                '(Lance | lance)': Key("escape,a"),
		'(Lance | lance) end': Key("escape,A"),
                'scape': Key("escape"),
		'etch start': Key("escape,I"),
		'[<n>] dub': Key("%(n)d,w"), 
		'[<n>] (Hynde | hind)': Key("%(n)d,b"),
		'[<n>] nib': Key("%(n)d,e"), 

                # more searching actions
                'braille word boundaries': Key('escape') + Text('/\<\>') + Key('left:2'),
                'go to [a] stowed': Key('escape,g,d'),
                'go to [a] stowed global': Key('escape,g,D'),
                'optic vex': Key('escape,colon,V,e,x,enter'),
                'go to (braille|Brielle) (1st|first)': Key('escape,g,g,n'),
                'go to (Brielle|braille) last': Key('escape,G,N'),
                '(Brielle|braille) function': Key('escape') + Text('/function '),

                # marking and returning to spots in the buffer
                'Mark Alpha': Key("escape,m,a"),
                'Mark (Brava|bravo)': Key("escape,m,b"),
                'Mark Charlie': Key("escape,m,c"),
                # add jumping to previous location and forward to next?

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
            'buff list': Key("escape") +  Text(":buffers") +  Key("enter"),
            'buff name':Key("escape,colon") +  Text("buffer "),
            'buff next':  Key("escape,colon,b,n,enter"),
            'buff back': Key("escape,colon,b,p,enter"),
            'buff last': Key("c-caret"),
            'buff last': Key("escape,colon,b,l,enter"),
            'buff <n>': Key("escape,colon,b,%(n)d,enter"),
            'buff save': Key("escape,colon,w,enter"),
            'buff save quit': Key("escape,colon,w,q,enter"),
            'buff quit': Key("escape,colon,q,enter"),
            'buff quit bang': Key("escape,colon,q,exclamation,enter"),
            'buff save quit bang': Key("escape,colon,w,q,exclamation,enter"),
            'buff edit': Key("escape,colon,e,space"),
            'buff shell': Key("escape,colon,s,h,enter"),

            #common options
            'buff ignore case': Key("escape,colon") +  Text("set ignorecase") +  Key("enter"),

            # window actions
            'split horizontal': Key("escape,colon,s,p,enter"),
            'split vertical': Key("escape,colon,v,s,p,enter"),
            'split new': Key("escape,colon,v,n,e,w,space"),
            'split (Stowe|stow)': Key('c-w,equal'),
            'buff wide <n>': Text(':vertical resize +%(n)d') +  Key('enter'),
            'buff narrow <n>': Text(':vertical resize -%(n)d') +  Key('enter'),
            'buff window right':  Key('c-w,l'),
            'buff window left':  Key('c-w,h'),
            'buff window up':  Key('c-w,k'),
            'buff window down':  Key('c-w,j'),
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
		'(cleave | Cleve) up <text>': Key("escape,O") + Function(lib.combination.executeCombo),
                '(Cleve | cleave) <text>': Key("escape,o") + Function(lib.combination.executeCombo),
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
                'paste front': Key("P"),
                'redo': Key("cs-r"),
   		'sub': Key("s"),
   		'sub line': Key("s-s"),
   		'swap': Key("r"),
   		'swap more': Key("s-r"),
                'tilde': Key("tilde"),
                'top off': Key("cs-p"),
                '[<n>] trim': Key("escape, x:%(n)d"),
            '[<n>] trim back': Key("escape, X:%(n)d"),
                'undo': Key("escape,u"),
                'yank': Key("y"),
                'yank line': Key("y,y"),
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
