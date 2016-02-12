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
                'shoot <n>': Key('%(n)d,enter'),
                'zilch <n>': Text('0%(n)d'),
                "[<n>] up [<text>]": Key("up:%(n)d") + Function(lib.combination.executeCombo),
                "[<n>] down [<text>]": Key("down:%(n)d") + Function(lib.combination.executeCombo),
                '[<n>] space [<text>]':Key('space:%(n)d') + Function(lib.combination.executeCombo), 
                "[<n>] tab [<text>]":Key("tab:%(n)d") + Function(lib.combination.executeCombo),
                '[<n>] tab back': Key("s-tab:%(n)d"),
                'text copy': Key("c-c"),
                'text paste': Key("c-v"),
                'lock screen': Key('win:down,l'),
                'shards': Mimic('list', 'all', 'windows'),
                'shard browser': Mimic('switch','to','chrome'),
                'shard Ubuntu': Mimic('switch','to','lubuntu'),
                '(spawn | Spohn) Outlook': Key('win') + Pause('100') + Text('chrome') + Key('enter')
                     + Pause('300') + Text('Outlook') + Key('enter') + Pause('300') + Key('enter'),   
                '(spawn | Spohn) Ubuntu': Key('win') + Pause('100') + Text('Oracle') + Key('enter')
                    + Pause('400') + Key('enter:2'),
                'window close': Key('a-f4'),
                'flip': Key('a-tab') + Key('alt'),
                '(Spohn | spawn) bash dragonfly': Key('win') + Pause('100') + Text('git bash') + Key('enter') + Pause('1000') + Text('cd ../../') + Key('enter') + Pause('300') + Text('cd NatLink/NatLink/MacroSystem') + Key('enter'),
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
