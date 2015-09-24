from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text)



grammar = Grammar("vim")
navigation_mapping = {
   '(Buck | buck)': Key("$"),
   'zilch': Key("0")
}


class Mapping(MappingRule):
    mapping = navigation_mapping
    extras = [
        Dictation('text'),
    ]


grammar.add_rule(Mapping())
grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None