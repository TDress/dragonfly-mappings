from dragonfly import Grammar, MappingRule, Text, Key, Function,  Dictation

import lib.combination
from lib.format import SCText

grammar = Grammar('programming')

symbols_rule = MappingRule(
    name = 'symbols',
    mapping = {
            # comparison operators
            '(Stowe | stow) [<text>]': Key("equal") +  Function(lib.combination.executeCombo),
            '(Stowe | stow) space': Key("space, equal, space") +  Function(lib.combination.executeCombo),
            "less than": Text(" < "),
            "less equals": Text(" <= "),
            "greater than": Text(" > "),
            "greater equals": Text(" >= "),

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
            '(breathed | breathe) [<text>]': Key("comma") +  Function(lib.combination.executeCombo),
            'snake [<text>]': Key("underscore") +  Function(lib.combination.executeCombo),
            'optic [<text>]': Key("colon") +  Function(lib.combination.executeCombo),
            'optic twice [<text>]': Key("colon,space,colon,left,backspace,right") +  Function(lib.combination.executeCombo),
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
            'Rasmus tag': Key('langle,delete,question,p,h,p,space'),
            'Rasmus tag close':  Key('question,rangle') + Key('backspace,rangle'),
            'Rasmus tag short':   Key('langle,delete,question,equal,space'),

            # logical operators
            'amp': Text("&"),
            'amp space':  Key('space,ampersand,space'),
            'amp twice':  Key('space,ampersand,space,ampersand,left,backspace,right,space'),
            
            'or': Key('space,bar,space:2,bar,left,backspace:2,right,space'),

            # arithmetic
            'Christ space [<text>]': Text(" + ") + Function(lib.combination.executeCombo),
            'Christ [<text>]': Text("+") +  Function(lib.combination.executeCombo),
            "Christ equals": Text(" += "),
            'Christ twice': Text("++"),
            "(minus|subtract|subtraction)": Text(" - "),
            "(minus|subtract|subtraction) equals": Text(" -= "),

            'mod [<text>]':  Key("percent") +  Function(lib.combination.executeCombo),
            'slug space':  Key("space,asterisk,space"),
            'slug':  Key("asterisk"),
            'hash': Key("hash"),

            # common abbreviations and terms
            'JavaScript': Text('javascript'),
            'Js': Text('js'),
            'Id':  Text("id"),

    },
    extras = [
        Dictation("text"),
        ],
    defaults = {
        "text":''
        }

)

text_formatting_rule = MappingRule(
    name = 'text',
    mapping = {
        'camel case [<text>]': Function(lib.format.camel_case_text),
        'capital [<text>]': Function(lib.format.pascal_case_text),       
        'Pascal case [<text>]': Function(lib.format.pascal_case_text),
        'snake case [<text>]': Function(lib.format.snake_case_text),
        'squash case [<text>]': Function(lib.format.squash_text),
        '(uppercase | upper case) [<text>]': Function(lib.format.uppercase_text),
        '(lowercase | lower case) [<text>]': Function(lib.format.lowercase_text),
        'hyphen case [<text>]': Function(lib.format.dash_text),
        '(spec | speck) case [<text>]': Function(lib.format.dot_text),
    },
    extras = [
        Dictation("text"),
    ]
)

builtin_statement_rule = MappingRule(
    name = 'builtin_statement',
    mapping = {
        '(brake | break)': Text('break'),
        '(brake | break) finish': Text('break;') +  Key('enter'), 
        "case": Text("case "),
        "case <text>": SCText("case %(text)s"),
        "catch": Text("catch () {") + Key("left:3"),
        "continue": Text("continue"),
        'continue finish':  Text('continue;') +  Key('enter'),
        "close comment": Text(" */"),
        "do while": Text("do {") +  Key('enter, rbrace,space') 
            + Text('while('),
        "else": Text("else"),
        "else if": Text("else if () {") + Key("left:3"),
        "extends ": Text("extends "),
        "for": Text("for () {") + Key("left:3"),
        "false": Text("false"),
        "finally": Text("finally {") + Key("enter"),
                "if": Text("if ("),
        "if <text>": Text("if (%(text)s) {") + Key("left:3"),
        'integer short': Text('int '),
        "(several | Sever) line": Key("escape,end") + Text(";"),

        "new": Text("new "),
        "return": Text("return "),
        "return finish":  Text('return;') +  Key('enter'),
        "switch": Text("switch () {") + Key("left:3"),
        "switch <text>": SCText("switch (%(text)s) {") + Key("left:3"),
        "throw": Text("throw "),
        "true": Text("true"),
        "try": Text("try {") + Key("enter"),
        "while": Text("while () {") + Key("left:3"),
        "while <text>": SCText("while (%(text)s) {") + Key("left:3"),


    },
    extras = [
        Dictation("text"),
    ]
)

php_rule = MappingRule(
    name = 'php',
    mapping = {
        'comment':Text('// '),
        'comment more': Text('/*') + Key('enter'),
        'empty': Text('empty( )') +  Key('left,backspace'),
        'for each': Text('foreach( as ) {') +  Key('enter:2,up:2,escape,dollar,6,h'),
        'for each short': Text('foreach( as )') + Key('escape,4,h'),
        'namespace': Text('namespace '),
        'nil': Text('null'),
        'PHP': Text("php"),
        'in array': Text('in_array('),
        'array shift': Text('array_shift('),
        'string to time': Text('strtotime('),
        'Rasmus print custom': Text('pr( );') +  Key('left,left,backspace'),
        'Rasmus print custom exit': Text('pr( );exit;') +  Key('escape,b:3,a,delete'),
        'Rasmus print readable': Text('print_r( )') +  Key('left,backspace'),
        'Rasmus <text>': SCText('$%(text)s'),
        'static access': Key('colon,space,colon,left,backspace,right'),  
        'use': Text('use '),
        'variable dump': Text('var_dump( );') + Key('left,left,backspace'),
        'variable dump exit': Text('var_dump( );exit;') + Key('escape,b:3,a,delete'),
    },
    extras = [
        Dictation("text"),
    ]

)

vocabulary_rule = MappingRule(
        name = 'vocabulary',
        mapping = {
            'parameter short': Text('param')
        }
)

grammar.add_rule(symbols_rule)
grammar.add_rule(php_rule)
grammar.add_rule(text_formatting_rule)
grammar.add_rule(vocabulary_rule)
grammar.add_rule(builtin_statement_rule)
grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
