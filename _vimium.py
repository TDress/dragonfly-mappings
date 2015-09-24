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
    'leaf back': Key("s-l"),
    'leaf forward': Key("s-r"),
    'leaf fresh': Key("c-r"),
    'leaf link': Key("f"),
    'leaf link new': Key("s-f"),

    #  Moving around
    'more': Key("j"),
    'less': Key("k"),
    'more': Key("j:10"),
    'less': Key("k:10"),
    'top': Key("g, g"),
    'bottom hobble': Key("s-g"),
    'back': Key("s-h"),
    'forward': Key("s-l"),

    #  Searching
    'find <text>': Key("escape, slash") + Text("%(text)s") + Key("enter"),
    'next': Key("n"),
    'prev|previous': Key("N"),
}

gmail_mapping = {
    'open': Key("o"),
    'inbox': Key("g, i"),
    '[go to] label <text>': Key("g, l") + Text("%(text)s") + Key("enter"),
    'trash': Key("hash"),
    'archive': Key("e"),
    '(earl|early|earlier)': Key("j"),
    '(late|later)': Key("k"),
}


class Mapping(MappingRule):
    mapping = window_mapping
    extras = [
        IntegerRef('n', 1, 99),
        Dictation('text'),
    ]

class MappingMail(MappingRule):
     mapping = gmail_mapping
     extras = [
        Dictation('text')
     ]


grammar.add_rule(Mapping())
grammar.add_rule(MappingMail())
grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None