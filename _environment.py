from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text,  Function, Pause,  Mimic)

import lib.format
import lib.combination

grammar = Grammar("environment")

general_rule = MappingRule(
	name = "general",
	mapping = {
                'browser (console | consul)': Key('cs-j'),
                'integer <n>': Text('%(n)d'),
                "[<n>] up [<text>]": Key("up:%(n)d") + Function(lib.combination.executeCombo),
                "[<n>] down [<text>]": Key("down:%(n)d") + Function(lib.combination.executeCombo),
                '[<n>] space [<text>]':Key('space:%(n)d') + Function(lib.combination.executeCombo), 
                "[<n>] tab [<text>]":Key("tab:%(n)d") + Function(lib.combination.executeCombo),
                '[<n>] tab back': Key("s-tab:%(n)d"),
                'text copy': Key("c-c"),
                'text paste': Key("c-v"),
                'lock screen': Key('win:down,l'),
                'shards': Mimic('list', 'all', 'windows'),
                'window close': Key('a-f4'),
                'window last': Key('a-tab') + Key('alt')
		},
	extras = [
		Dictation("text"),
                 IntegerRef('n',1,  1000000)
		],
        defaults = {
            "n":1,
            "text":''
        }
)

lubuntu_rule = MappingRule(
	name = "lubuntu",
	mapping = {
            'terminal new': Key('a-f2') +  Pause('100') + Text('gnome-terminal') + Key('enter'),
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
