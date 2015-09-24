from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text)



grammar = Grammar("vimium")

window_mapping = {
    # Tab navigation
    'leaf left': Key("cs-tab"),
    'leaf right': Key("c-tab"),
    'leaf <n>': Key("c-%(n)d"),
    'leaf new': Key("c-t"),
    'leaf reopen': Key("cs-t"),
    'leaf close': Key("c-w"),
    'leaf fresh': Key("c-r"),
    'leaf link': Key("f"),
    'leaf link new': Key("s-f"),
    'leaf bar': Key("c-l"),

    #  Moving around
    'slump <n>': Key("j:(n)"),
    'boost <n>': Key("k:(n)"),
    'slump more': Key("c-d"),
    'slump most': Key("pgdown"),
    'boost more':  Key("c-u"),
    'boost most':  Key("pgup"),
    'leaf top': Key("g, g"),
    'leaf bottom': Key("s-g"),
    'bump <n>': Key("l:(n)"),
    'tug <n>': Key("h:(n)"),
    'leaf past': Key("a-left"),
    'leaf future': Key("a-right"),
    
    #  Searching
    'braille <text>': Key("escape, slash") + Text("%(text)s") + Key("enter"),
    'Vance': Key("n"),
    'rev': Key("N"),

    #  page actions
    'show page atoms': Key("g,s"),
    'etch': Key("i"),
    'etch <text>': Key("i") + Text("%(text)")
}


class Mapping(MappingRule):
    mapping = window_mapping
    extras = [
        IntegerRef('n', 1, 99),
        Dictation('text'),
    ]


grammar.add_rule(Mapping())
grammar.add_rule(MappingMail())
grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None