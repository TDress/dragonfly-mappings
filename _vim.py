from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text, Function,  Pause)

import lib.combination

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
	  	'zilch [<text>]': Key("escape,0") + Function(lib.combination.executeCombo),
    		'[<n>] slump [<text>]': Key("j:%(n)d")  + Function(lib.combination.executeCombo),
    		'[<n>] boost [<text>]': Key("k:%(n)d") + Function(lib.combination.executeCombo),
    		'[<n>] bump [<text>]': Key("l:%(n)d") + Function(lib.combination.executeCombo),
    		'[<n>] tug [<text>]': Key("h:%(n)d") +  Function(lib.combination.executeCombo),
                '[<n>] page up': Key("pgup:%(n)d"),
                '[<n>] page down': Key("pgdown:%(n)d"),
                'code future': Key("c-i"),
                'code past':  Key("c-o"),
                'code help rake':  Key("escape") + Text(":helpgrep "),
                'code list errors': Text(":clist") +  Key("enter"),
                '(Lance | lance) [<text>]': Key("escape,a") + Function(lib.combination.executeCombo),
		'(Lance | lance) end [<text>]': Key("escape,A") + Function(lib.combination.executeCombo),
                'scape [<text>]': Key("escape") + Function(lib.combination.executeCombo),
    		'etch [<text>]': Key("i") + Function(lib.combination.executeCombo),
		'etch start [<text>]': Key("escape,I") + Function(lib.combination.executeCombo),
		'[<n>] dub [<text>]': Key("%(n)d,w") + Function(lib.combination.executeCombo),
		'[<n>] (Hynde | hind) [<text>]': Key("%(n)d,b") + Function(lib.combination.executeCombo),
		'<n> Eli [<text>]': Key("%(n)d,e") + Function(lib.combination.executeCombo),

                # more searching actions
                'braille ignore case': Key('escape') +  Text('/\c'),
                'braille ignore case [<text>]': Key('escape') +  Text('/\c%(text)s'),
                'braille word boundaries': Key('escape') + Text('/\<\>') + Key('left:2'),
                'go to [a] stowed': Key('escape,g,d'),
                'go to [a] stowed global': Key('escape,g,D'),
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
		IntegerRef("n", 1, 50)
	],
	defaults = {
		"n": 1,
                "text": ''
	}
)

buffer_rule = MappingRule(
	name = "buffer",
	mapping = {
            'code buffers': Key("escape") +  Text(":buffers") +  Key("enter"),
            'code name':Key("escape,colon") +  Text("buffer "),
            'code next':  Key("escape,colon,b,n,enter"),
            'code back': Key("escape,colon,b,p,enter"),
            'code last': Key("c-caret"),
            'code <n>': Key("escape,colon,b") + Text("%(n)d") +  Key('enter'),
            'code save': Key("escape,colon,w,enter"),
            'code save quit': Key("escape,colon,w,q,enter"),
            'code quit': Key("escape,colon,q,enter"),
            'code quit bang': Key("escape,colon,q,exclamation,enter"),
            'code remove':  Key('escape,colon,b,d,enter'),
            'code save quit bang': Key("escape,colon,w,q,exclamation,enter"),
            'code edit': Key("escape,colon,e,space"),
            'code shell': Key("escape,colon,s,h,enter"),

            #common options
            'code ignore case': Key("escape,colon") +  Text("set ignorecase") +  Key("enter"),

            # window actions
            'horizontal split': Key("escape,colon,s,p,enter"),
            'vertical split': Key("escape,colon,v,s,p,enter"),
            'split new': Key("escape,colon,v,n,e,w,space"),
            'split (Stowe|stow)': Key('c-w,equal'),
            'code wide <n>': Text(':vertical resize +%(n)d') +  Key('enter'),
            'code narrow <n>': Text(':vertical resize -%(n)d') +  Key('enter'),
            'vertical (explore | Explorer)': Key('escape, colon') 
                + Key('e,left,V,right') + Text('xplore') +  Key('enter'),
            'code (Explorer | explore)': Key('escape, colon') +  Key('x,left,E,enter'),
            'code window right':  Key('escape,c-w,l'),
            'code window left':  Key('escape,c-w,h'),
            'code window up':  Key('c-w,k'),
            'code window down':  Key('c-w,j'),
	},
	extras = [
		Dictation("text"),
		IntegerRef("n", 1, 500)
	],
	defaults = {
		"n": 1
	}
)

manipulation_rule = MappingRule(
	name = "manipulation",
	mapping = {
		'bag [<text>]': Key("v") +  Function(lib.combination.executeCombo), 
		'bag block [<text>]': Key("c-v") +  Function(lib.combination.executeCombo), 
		'(cleave | Cleve) up [<text>]': Key("escape,O") + Function(lib.combination.executeCombo),
                '(Cleve | cleave) [<text>]': Key("escape,o") + Function(lib.combination.executeCombo),
                '[<n>] jump right':  Key('%(n)d,rangle') +  Pause('20') +  Key('rangle'),
                '[<n>] jump left':  Key('%(n)d,langle') +  Pause('20') +  Key('langle'),
                '[<n>] shoot [<text>]': Key("enter:%(n)d") +  Function(lib.combination.executeCombo),
		'lop [<text>]': Key("d") +  Function(lib.combination.executeCombo),
		'lop line [<text>]': Key("d,d") +  Function(lib.combination.executeCombo), 
                'oust [<text>]': Key("c") +  Function(lib.combination.executeCombo), 
                'oust back': Key("escape,b,c,e"),
                'oust line': Key('c:2'),
                'paste': Key("escape,p"),
                'paste front': Key("P"),
                'redo': Key("cs-r"),
   		'sub [<text>]': Key("s") +  Function(lib.combination.executeCombo),
   		'sub line [<text>]': Key("s-s") +  Function(lib.combination.executeCombo),
   		'swap [<text>]': Key("r") +  Function(lib.combination.executeCombo),
   		'swap more [<text>]': Key("s-r") +  Function(lib.combination.executeCombo),
                'tilde [<text>]': Key("tilde") +  Function(lib.combination.executeCombo),
                'top off [<text>]': Key("cs-p") + Function(lib.combination.executeCombo),
                '[<n>] trim [<text>]': Key("%(n)d,x")+  Function(lib.combination.executeCombo),
                '[<n>] trim back [<text>]': Key("%(n)d,X") +  Function(lib.combination.executeCombo),
                'undo': Key("escape,u"),
                'yank [<text>]': Key("y") +  Function(lib.combination.executeCombo),
                'yank line [<text>]': Key("y,y") + Function(lib.combination.executeCombo),
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
