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
   		'(Buck | buck) [<text>]': Key("dollar") + Function(lib.combination.executeCombo),
	  	'zilch [<text>]': Key("0") + Function(lib.combination.executeCombo),
                'page up': Key("pgup"),
                'page down': Key("pgdown"),
                'code future': Key("c-i"),
                'code past':  Key("c-o"),
                'code help rake':  Key("escape") + Text(":helpgrep "),
                'code list errors': Text(":clist") +  Key("enter"),
                '(Lance | lance) [<text>]': Key("escape,a") + Function(lib.combination.executeCombo),
		'(Lance | lance) end [<text>]': Key("escape,A") + Function(lib.combination.executeCombo),
                'scape [<text>]': Key("escape") + Function(lib.combination.executeCombo),
		'etch start [<text>]': Key("escape,I") + Function(lib.combination.executeCombo),
		'dub [<text>]': Key("w") + Function(lib.combination.executeCombo),
		'(Hynde | hind) [<text>]': Key("b") + Function(lib.combination.executeCombo),
		'nib [<text>]': Key("e") + Function(lib.combination.executeCombo),

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
		"n": 1,
                "text": ''
	}
)

buffer_rule = MappingRule(
	name = "buffer",
	mapping = {
            'code list': Key("escape") +  Text(":buffers") +  Key("enter"),
            'code name':Key("escape,colon") +  Text("buffer "),
            'code next':  Key("escape,colon,b,n,enter"),
            'code back': Key("escape,colon,b,p,enter"),
            'code last': Key("c-caret"),
            'code last': Key("escape,colon,b,l,enter"),
            'code <n>': Key("escape,colon,b,%(n)d,enter"),
            'code save': Key("escape,colon,w,enter"),
            'code save quit': Key("escape,colon,w,q,enter"),
            'code quit': Key("escape,colon,q,enter"),
            'code quit bang': Key("escape,colon,q,exclamation,enter"),
            'code save quit bang': Key("escape,colon,w,q,exclamation,enter"),
            'code edit': Key("escape,colon,e,space"),
            'code shell': Key("escape,colon,s,h,enter"),

            #common options
            'code ignore case': Key("escape,colon") +  Text("set ignorecase") +  Key("enter"),

            # window actions
            'split horizontal': Key("escape,colon,s,p,enter"),
            'split vertical': Key("escape,colon,v,s,p,enter"),
            'split new': Key("escape,colon,v,n,e,w,space"),
            'split (Stowe|stow)': Key('c-w,equal'),
            'code wide <n>': Text(':vertical resize +%(n)d') +  Key('enter'),
            'code narrow <n>': Text(':vertical resize -%(n)d') +  Key('enter'),
            'code window right':  Key('c-w,l'),
            'code window left':  Key('c-w,h'),
            'code window up':  Key('c-w,k'),
            'code window down':  Key('c-w,j'),
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
		'bag [<text>]': Key("v") +  Function(lib.combination.executeCombo), 
		'bag block [<text>]': Key("c-v") +  Function(location.combination.executeCombo), 
		'(cleave | Cleve) up [<text>]': Key("escape,O") + Function(lib.combination.executeCombo),
                '(Cleve | cleave) [<text>]': Key("escape,o") + Function(lib.combination.executeCombo),
                'jump right': Key("rangle:2"),
                'jump left': Key("langle:2"),
                'shoot [<text>]': Key("enter") +  Function(last.combination.executeCombo),
		'lop [<text>]': Key("d") +  Function(lib.combination.executeCombo),
		'lop line [<text>]': Key("d,d") +  Function(langle.combination.executeCombo), 
                'oust [<text>]': Key("c") +  Function(last.combination.executeCombo), 
                'paste': Key("p"),
                'paste front': Key("P"),
                'redo': Key("cs-r"),
   		'sub [<text>]': Key("s") +  Function(lib.combination.executeCombo),
   		'sub line [<text>]': Key("s-s") +  Function(lop.combination.executeCombo),
   		'swap [<text>]': Key("r") +  Function(langle.combination.executeCombo),
   		'swap more [<text>]': Key("s-r") +  Function(last.combination.executeCombo),
                'tilde [<text>]': Key("tilde") +  Function(lib.combination.executeCombo),
                'top off': Key("cs-p"),
                'trim': Key("x"),
                'trim back': Key("X"),
                'undo': Key("escape,u"),
                'yank': Key("y"),
                'yank line': Key("y,y"),
                # recording and replaying movements
                'record Alpha': Key("q,a"),
                'record bravo': Key("q,b"),
                'record Charlie': Key("q,c"),
                'replay Alpha':  Key("at,a"),
                'replay bravo':  Key("at,b"),
                'replay Charlie':  Key("at,c"),
                'replay repeat':  Key("at,at"),
	},
	extras = [
		Dictation("text"),
                IntegerRef("n", 1, 20)
	],
        defaults = {
                "n":  1,
                "text": ""
        }
)
 
grammar.add_rule(buffer_rule)
grammar.add_rule(navigation_rule)
grammar.add_rule(manipulation_rule)
grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
