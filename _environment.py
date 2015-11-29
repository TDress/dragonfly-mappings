from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text,  Function)

import lib.combination

grammar = Grammar("environment")

general_rule = MappingRule(
	name = "general",
	mapping = {
                "[<n>] up [<text>]": Key("up:%(n)d") + Function(lib.combination.executeCombo),
                "[<n>] down [<text>]": Key("down:%(n)d") + Function(lib.combination.executeCombo),
                "[<n>] tab [<text>]":Key("tab:%(n)d") + Function(lib.combination.executeCombo),
                '[<n>] tab back': Key("shift-tab:%(n)d"),
                'text copy': Key("c-c"),
                'text paste': Key("c-v"),
                'lock screen': Key('w-l'),
                'window last': Key('a-tab'),
		},
	extras = [
		Dictation("text"),
                 IntegerRef('n',1, 99)
		],
        defaults = {
            "n":1,
            "text":''
        }
)

lubuntu_rule = MappingRule(
	name = "lubuntu",
	mapping = {
            'terminal new': Key('a-f2') +  Text('gnome-terminal') + Key('tab:2,enter'),
            'window full-screen': Key('f11'),
	}
)

grammar.add_rule(general_rule)
grammar.add_rule(lubuntu_rule)

grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
