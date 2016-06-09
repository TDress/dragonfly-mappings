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
	  	'zilch [<text>]': Key("0") + Function(lib.combination.executeCombo),
    		'[<n>] slump [<text>]': Key("j:%(n)d")  + Function(lib.combination.executeCombo),
                'safe boost': Key('9,k,9,k,9,k'),
                'safe slump': Key('9,j,9,j,9,j'),
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
                'scape start': Key('escape, 0, w'),
                'scape [<text>]': Key("escape") + Function(lib.combination.executeCombo),
    		'etch [<text>]': Key("i") + Function(lib.combination.executeCombo),
                'etch indent': Key('i') + Text('stub') + Key('escape,b,equal:2,c,a,w'),
		'etch start [<text>]': Key("escape,I") + Function(lib.combination.executeCombo),
		'[<n>] dub [<text>]': Key("%(n)d,w") + Function(lib.combination.executeCombo),
		'[<n>] (Hynde | hind) [<text>]': Key("%(n)d,b") + Function(lib.combination.executeCombo),
		'<n> Eli [<text>]': Key("%(n)d,e") + Function(lib.combination.executeCombo),
                'cork Christ': Key('right,space,plus,space'),
                'cork (spec | speck)': Key('right,dot'),
                'Cork (paz | pause | paws)': Key('right, comma,space'), 
                '(Cork | quirks) Stowe': Key('right,space,equal,space'),
                '(Cork | quirks) shark': Key('right') + Text('->'),

                '(paz | pause | paws) space': Key('comma,space'),
                '(paz | pause | paws) shoot': Key('comma,enter'),
                'cork optic': Key('right,colon,space'),
                'Cork whale': Key('right,space,equal,rangle,space'),
                'Cork shoot': Key('right, enter'),
                'seal (sever | several)': Key('escape,A') + Text(';') + Key('escape'),
                'seal (paz | pause | paws)': Key('escape,A,comma,escape'),
                '(paz | pause | paws) [<text>]': Key('comma') + Function(lib.combination.executeCombo),


                # more searching actions
                'braille ignore case': Key('escape') +  Text('/\c'),
                'braille ignore case [<text>]': Key('escape') +  Text('/\c%(text)s'),
                'braille word boundaries': Key('escape') + Text('/\<\>') + Key('left:2'),
                'go to [a] stowed': Key('escape,g,d'),
                'go to [a] stowed global': Key('escape,g,D'),
                '(Brielle|braille) capital <text>': Key('escape,slash') + Function(lib.format.pascal_case_text) + Key('enter'),
                '(Brielle|braille) integer <n>': Key('escape') + Text('/%(n)d') + Key('enter'),
                'highlight off': Key('escape,colon,n,o,h,enter'),

                # substitution
                'code substitute': Key('escape,colon') + Text('%s///gc') + Key('left:4'),

                # marking and returning to spots in the buffer
                'Mark Alpha': Key("escape,m,a"),
                'Mark (Brava|bravo)': Key("escape,m,b"),
                'Mark Charlie': Key("escape,m,c"),
                # add jumping to previous location and forward to next?

	},
	extras = [
		Dictation("text"),
		IntegerRef("n", 1, 10000)
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
            'code file': Key('escape,colon,f,enter'),
            'code name':Key("escape,colon") +  Text("buffer "),
            'code next':  Key("escape,colon,b,n,enter"),
            'code back': Key("escape,colon,b,p,enter"),
            'code last': Key("c-caret"),
            'code <n>': Key("escape,colon,b") + Text("%(n)d") +  Key('enter'),
            'code line <n>': Key('escape, colon') + Text('%(n)d\n'),
            'code save': Key("escape,colon,w,enter"),
            'code save bang': Key("escape,colon,w,exclamation,enter"),
            'code save quit': Key("escape,colon,w,q,enter"),
            'code quit': Key("escape,colon,q,enter"),
            'code quit bang': Key("escape,colon,q,exclamation,enter"),
            'code remove':  Key('escape,colon,b,d,enter'),
            'code save quit bang': Key("escape,colon,w,q,space,exclamation,left,backspace,enter"),
            'code edit': Key("escape,colon,e,space"),
            'code shell': Key("escape,colon,s,h,enter"),
            'code search file':Key('escape,colon') + Text('CtrlP '),
            'code search libraries':Key('escape,colon') + Text('CtrlP ~/ecom/webdev_trunk/libraries/') + Key('enter'),
            'code search applications':Key('escape,colon') + Text('CtrlP ~/ecom/webdev_trunk/applications/') + Key('enter'),
            'code search function': Key('escape,colon') + Text(' Flisttoggle') + Key('enter'),

            #common options
            'code ignore case': Key("escape,colon") +  Text("set ignorecase") +  Key("enter"),
            'code respect case': Key("escape,colon") +  Text("set ignorecase!") +  Key("enter"),

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
		IntegerRef("n", 1, 5000)
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
                '(Cleve | cleave) push': Key("escape,o,enter,up"), 
                '(Cleve | cleave) up push': Key("escape,O,enter, up"),
                '[<n>] jump right':  Key('escape, v, l,%(n)d,rangle'),
                '[<n>] jump left':  Key('escape, v, l,%(n)d,langle'),
                'jump right <n>': Key('escape,v, j:%(n)d, rangle'),
                'jump left <n>': Key('escape,v,j:%(n)d, langle'),
                'code indent': Key('escape,G,equal,g:2,c-o,c-o'),
                'line indent': Key('escape,d:2,O'),
                'line indent <n>': Key('escape,v,j:%(n)d,equal'),
                'shoot push': Key('enter,up,tab'),
                '[<n>] shoot [<text>]': Key("enter:%(n)d") +  Function(lib.combination.executeCombo),
                'lop': Key('d'),
                'lop head': Key('d,g:2'),
                'lop tail': Key('d,G'),
		'[<n>] lop Eli': Key("%(n)d,d,e"),
                'lop Buck': Key('escape,d,dollar'),
		'[<n>] lop (Hynde | hind)': Key("%(n)d, d,b"),
		'[<n>] lop slump': Key("%(n)d,j"),
		'[<n>] lop boost': Key("%(n)d,k"),
		'lop word [<text>]': Key("escape,d,a,w") +  Function(lib.combination.executeCombo),
		'lop line [<n>]': Key("escape,%(n)d,d,d"),
                'lop line above': Key('escape,k,d:2'),
                'lop line below': Key('escape,j,d:2'),
		'lop line [<text>]': Key("escape,d,d") +  Function(lib.combination.executeCombo), 
                '[<n>] oust back': Key("escape,%(n)d,b,%(n)d,c,e"),
                '[<n>] oust next': Key("escape,%(n)d,c,e"),
'oust Buck':Key('escape,c,dollar'),
                'oust word':Key('escape,c,a,w'),
                'oust inside': Key('escape,c,i'),
                'oust line [<n>]': Key('escape, %(n)d,c,c'),

                '[<n>] oust [<text>]': Key("%(n)d,c") +  Function(lib.combination.executeCombo), 
                                'paste': Key("escape,p"),
                'paste front': Key("P"),
                'redo': Key("cs-r"),
   		'sub [<text>]': Key("s") +  Function(lib.combination.executeCombo),
   		'sub line [<text>]': Key("s-s") +  Function(lib.combination.executeCombo),
   		'swap [<text>]': Key("r") +  Function(lib.combination.executeCombo),
   		'swap more [<text>]': Key("s-r") +  Function(lib.combination.executeCombo),
                'tilde first': Key('escape, b, tilde'),
                'tilde word': Key('escape, l, e, v, b, tilde'),
                'tilde [<text>]': Key("tilde") +  Function(lib.combination.executeCombo),
                'top off [<text>]': Key("cs-p") + Function(lib.combination.executeCombo),
                'trim up': Key('escape,0,w,h,v,k,dollar,x'),
                '[<n>] trim [<text>]': Key("%(n)d,x")+  Function(lib.combination.executeCombo),
                '[<n>] trim back [<text>]': Key("%(n)d,X") +  Function(lib.combination.executeCombo),
                'undo': Key("escape,u"),
                'yank line <n>': Key('escape,0, v, %(n)d-1, j, $, y'),
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
