from dragonfly import Grammar, MappingRule, Text, Key

import lib.combination

grammar = Grammar('programming')

symbols_rule = MappingRule(
    name = 'symbols',
    mapping = {
            # comparison operators
            '(Stowe | stow) [<text>]': Key("equal") +  Function(lib.combination.executeCombo),
            '(Stowe | stow) space': Key("space, equal, space") +  Function(lib.combination.executeCombo),

            'tick [<text>]': Key("apostrophe") +  Function(lib.combination.executeCombo),
            'tick twice': Key("dquote"),
            '(way | weigh) (stow | Stowe)': Key("space, equal, equal, space"),
            'way (stow | Stowe) strict': Key("space, equal, equal, equal, space"),
            'way bang': Key("space, exclamation, equal, space"),
            'way bang strict': Key("space, exclamation, equal, equal, space"),
            'way trout equal': Key("space, rangle, equal, space"),
            'way whale flip': Key("space,langle, equal, space"),
            'crypt [<text>]': Key("question") +  Function(langle.combination.executeCombo),
            'crypt optic': Key("question,colon"),

            # mappings, brackets and miscellaneous
            'bang [<text>]': Key("exclamation") +  Function(langle.combination.executeCombo),
            'optic [<text>]': Key("colon") +  Function(langle.combination.executeCombo),
            'optic space': Key("colon, space"),
            'arc [<text>]': Key("lparen") +  Function(lparen.combination.executeCombo),
            'arc end': Key("rparen"),
            'whale [<text>]': Text(" => ") +  Function(lparen.combination.executeCombo),
            'shark [<text>]': Text("->") +  Function(lparen.combination.executeCombo),
            'trout [<text>]': Text(">") +  Function(lparen.combination.executeCombo),
            'trout less': Text("<"),
            'ternary': Text(" ?  :") +  Key("left:2"),
            'ternary short': Text(" ?: "),

            'raft [<text>]': Text("[") +  Function(left.combination.executeCombo),
            'raft end': Text("]"),
            'crimp [<text>]': Text("{") +  Function(left.combination.executeCombo),
            'crimp end': Text("}"),
            'dot space': Text(" . "),
            'dot [<text>]': Text(".") +  Function(left.combination.executeCombo),
            'sever [<text>]':Text(";") +  Function(left.combination.executeCombo),
            
            #  tags
            'Rasmus tag':  Text("<?php"),
            'Rasmus tag close': Text("?>"),
            'Rasmus tag short': Text("<?="),

            # logical operators
            'pipe [<text>]':Text("|") +  Function(logical.combination.executeCombo),
            'pipe space':  Text(" | "),
            'pipe twice': Text("||"),
            'pipe twice space': Text(" || "),
            'amp': Text("&"),
            'amp space': Text(" & "),
            'amp twice': Text("&&"),
            'amp twice space': Text(" && "),

            # arithmetic
            'Christ space': Text(" + "),
            'Christ [<text>]': Text("+") +  Function(logical.combination.executeCombo),
            'Christ twice': Text("++"),
            'minus space': Text(" - "),
            'minus': Text("-"),
            'mod space':  Key("space,percent,space"), 
            'mod':  Key("percent"),
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
