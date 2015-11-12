from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text)

grammar = Grammar("environment")

general_rule = MappingRule(
	name = "general",
	mapping = {
                "[<n>] up": Key("up:%(n)d"),
                "[<n>] down": Key("down:%(n)d"),
                "[<n>] tab":Key("tab:%(n)d"),
                '[<n>] tab back': Key("shift-tab:%(n)d"),
                'text copy': Key("c-c"),
                'text paste': Key("c-v"),
		},
	extras = [
		Dictation("text"),
                 IntegerRef('n',1, 99)
		],
        defaults = {
            "n":1
        }
)

grammar.add_rule(general_rule)

grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
