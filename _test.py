from dragonfly import Grammar, MappingRule, Text, Key

grammar = Grammar('test')

class TestRule(MappingRule):
    mapping = {
          'bottom hobble test': Key("s-g"),
        }

grammar.add_rule(TestRule())
grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None