from dragonfly import Grammar, MappingRule, Text, Key, Function,  Dictation

import lib.combination

grammar = Grammar('programming')

symbols_rule = MappingRule(
    name = 'symbols',
    mapping = {
            # comparison operators
            '(Stowe | stow) [<text>]': Key("equal") +  Function(lib.combination.executeCombo),
            '(Stowe | stow) space': Key("space, equal, space") +  Function(lib.combination.executeCombo),

            'tick [<text>]': Key("apostrophe") +  Function(lib.combination.executeCombo),
            'tick twice [<text>]': Key("dquote") + Function(lib.combination.executeCombo),
            '(way | weigh) (stow | Stowe)': Key("space, equal, equal, space"),
            'way (stow | Stowe) strict': Key("space, equal, equal, equal, space"),
            'way bang': Key("space, exclamation, equal, space"),
            'way bang strict': Key("space, exclamation, equal, equal, space"),
            'way trout equal': Key("space, rangle, equal, space"),
            'way whale flip': Key("space,langle, equal, space"),
            'crypt [<text>]': Key("question") +  Function(lib.combination.executeCombo),
            'crypt optic': Key("question,colon"),

            # mappings, brackets and miscellaneous
            'bang [<text>]': Key("exclamation") +  Function(lib.combination.executeCombo),
            'comma [<text>]': Key("comma") +  Function(lib.combination.executeCombo),
            'snake [<text>]': Key("underscore") +  Function(lib.combination.executeCombo),
            'optic [<text>]': Key("colon") +  Function(lib.combination.executeCombo),
            'optic twice [<text>]': Key("colon") +  Function(lib.combination.executeCombo),
            'optic space': Key("colon, space"),
            'arc [<text>]': Key("lparen") +  Function(lib.combination.executeCombo),
            'arc end': Key("rparen"),
            'whale [<text>]': Text(" => ") +  Function(lib.combination.executeCombo),
            'shark [<text>]': Text("->") +  Function(lib.combination.executeCombo),
            'trout [<text>]': Text(">") +  Function(lib.combination.executeCombo),
            'trout less [<text>]': Text("<") + Function(lib.combination.executeCombo),
            'ternary': Text(" ?  :") +  Key("left:2"),
            'ternary short': Key("space,question,colon,space"),

            'raft [<text>]': Text("[") +  Function(lib.combination.executeCombo),
            'raft end': Text("]"),
            'crimp [<text>]': Text("{") +  Function(lib.combination.executeCombo),
            'crimp end': Text("}"),
            'dot space': Text(" . "),
            'dot [<text>]': Text(".") +  Function(lib.combination.executeCombo),
            'sever [<text>]':Text(";") +  Function(lib.combination.executeCombo),
            
            #  tags
            'Rasmus tag':   Key('langle,question,p,h,p'),
            'Rasmus tag close':  Key('question,rangle'),
            'Rasmus tag short':  Key('langle,question,equal'),

            # logical operators
            'amp': Text("&"),
            'amp space':  Key('space,ampersand,space'),
            'amp twice':  Key('ampersand,ampersand'),
            'amp twice space': Key('space,ampersand,ampersand,space'),

            # arithmetic
            'Christ space [<text>]': Text(" + ") + Function(lib.combination.executeCombo),
            'Christ [<text>]': Text("+") +  Function(lib.combination.executeCombo),
            'Christ twice': Text("++"),
            'minus space': Text(" - "),
            'minus': Text("-"),
            'mod [<text>]':  Key("percent") +  Function(lib.combination.executeCombo),
            'slug space':  Key("space,asterisk,space"),
            'slug':  Key("asterisk"),
            'hash': Key("hash"),

            # common abbreviations
            'Id':  Text("id"),

    },
    extras = [
        Dictation("text"),
        ],
    defaults = {
        "text":''
        }

)

php_rule = MappingRule(
    name = 'php',
    mapping = {
        'comment':Text('// '),
        'comment more': Text('/*') + Key('enter'),
        'PHP': Text("php"),
        'variable dump': Text('var_dump( );') + Key('left,left,backspace'),
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
