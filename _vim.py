from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text, Function)

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

# vocabulary mappings for vim insert mode. Always return to insert mode.
imodeVocabulary = {
        "paste": "escape,p,A",
        "indent": "escape,equal,equal,A",
        "tick": "squote",
        "tick twice": "dquote",
        "raft": "lbracket",
        "raft end": "rbracket",
        "crimp": "lbrace",
        "crimp end": "rbrace",
        "arc": "lparen",
        "arc end": "rparen",
        "trout": "rangle",
        "trout less": "langle",
        "buck": "dollar",
}

# vocabulary mappings for vim visual mode
vmodeVocabulary = {
        "dub": "w",
        "nib": "e",
        "slump": "j",
        "boost": "k",
        "leave top": "g,g",
        "leaf bottom": "G",
} 


# functions to determine the vim mode of a combination


# executes keystroke combinations in insert mode
#   @recursive
#   loops over all words in text and executes
#   any commands that exist in the insert mode vocabulary.
#   Recursive calls are made for any text after the command.
def imode_combo(text):
    text = str(text)
    if len(text) < 1:
        return
    words = text.split(" ")
    for i in range(len(words)-1,0,-1):
        command = ' '.join(words[0:i])
        if command in imodeVocabulary.keys():
            Key(imodeVocabulary[command]).execute()
            if len(words)-1 > i:
                remainder = words[i+1:len(words)-1]
                remainder_text = ' '.join(remainder)
                return imode_combo(remainder_text)
            else:
                return
    #Text(text).execute()



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

                # more searching actions
                'braille word boundaries': Key('escape') + Text('/\<\>') + Key('left:2'),
                'go to [a] stowed': Key('escape,g,d'),
                'go to [a] stowed global': Key('escape,g,D'),
                'optic vex': Key('escape,colon,V,e,x,enter'),
                'go to (braille|Brielle) (1st|first)': Key('escape,g,g,n'),
                'go to (Brielle|braille) last': Key('escape,G,N'),
                '(Brielle|braille) function': Key('escape') + Text('/function '),

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
            'code buffer list': Key("escape") +  Text(":buffers") +  Key("enter"),
            'code buffer name':Key("escape,colon") +  Text("buffer "),
            'code buffer next':  Key("escape,colon,b,n,enter"),
            'code buffer back': Key("escape,colon,b,p,enter"),
            'code buffer last': Key("c-caret"),
            'code buffer last': Key("escape,colon,b,l,enter"),
            'code buffer <n>': Key("escape,colon,b,%(n)d,enter"),
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
            'code split horizontal': Key("escape,colon,s,p,enter"),
            'code split vertical': Key("escape,colon,v,s,p,enter"),
            'code split new': Key("escape,colon,v,n,e,w,space"),
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
		'(cleave | Cleve) up <text>': Key("escape,O") + Function(imode_combo),
                '(Cleve | cleave) <text>': Key("escape,o") + Function(imode_combo),
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
