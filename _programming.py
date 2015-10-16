from dragonfly import Grammar, MappingRule, Text, Key

grammar = Grammar('programming')

symbols_rule = MappingRule(
    name = 'symbols',
    mapping = {
            # comparison operators
            '(Stowe | stow)': Key("equal"),
            '(Stowe | stow) space': Key("space, equal, space"),

            'tick': Key("apostrophe"),
            'tick twice': Key("dquote"),
            '(way | weigh) (stow | Stowe)': Key("space, equal, equal, space"),
            'way (stow | Stowe) strict': Key("space, equal, equal, equal, space"),
            'way bang': Key("space, exclamation, equal, space"),
            'way bang strict': Key("space, exclamation, equal, equal, space"),
            'way trout equal': Key("space, rangle, equal, space"),
            'way whale flip': Key("space,langle, equal, space"),
            'crypt': Key("question"),
            'crypt optic': Key("question,colon"),

            # mappings, brackets and miscellaneous
            'bang': Key("exclamation"),
            'optic': Key("colon"),
            'optic space': Key("colon, space"),
            'arc': Key("lparen"),
            'arc end': Key("rparen"),
            'whale': Text(" => "),
            'shark': Text("->"),
            'trout': Text(">"),
            'trout less': Text("<"),
            'raft': Text("["),
            'raft end': Text("]"),
            'crimp': Text("{"),
            'crimp end': Text("}"),
            'dot space': Text(" . "),
            'dot': Text("."),

            # logical operators
            'pipe':Text("|"),
            'pipe space':  Text(" | "),
            'pipe twice': Text("||"),
            'pipe twice space': Text(" || "),

            # arithmetic
            'Christ space': Text(" + "),
            'Christ': Text("+"),
            'shorn space': Text(" - "),
            'shorn': Text("-"),
            'mod space':  Key("space,percent,space"), 
            'mod':  Key("percent"),
            'slug space':  Key("space,asterisk,space"),
            'slug':  Key("asterisk"),
            'hash': Key("hash")
    }
)

php_rule = MappingRule(
    name = 'php',
    mapping = {
        'PHP': Text("php")
    }
)

grammar.add_rule(symbols_rule)
grammar.add_rule(php_rule)
grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
