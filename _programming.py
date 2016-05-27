from dragonfly import Grammar, MappingRule, Text, Key, Function,  Dictation,IntegerRef

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

            '(tick | take) word': Key('escape, e, a, apostrophe, escape, b, i, apostrophe, escape'),
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
            'bang twice': Text('! !') + Key('left,backspace,right'),
            'bang [<text>]': Key("exclamation") +  Function(lib.combination.executeCombo),
            '(breathed | breathe) [<text>]': Key("comma") +  Function(lib.combination.executeCombo),
            'snake Id': Text('_id'),
            'snake [<text>]': Key("underscore") +  Function(lib.combination.executeCombo),
            'snake word [<text>]': Text('_%(text)s'),
            'spec word [<text>]': Text('.%(text)s'),

            'optic [<text>]': Key("colon") +  Function(lib.combination.executeCombo),
            'optic twice [<text>]': Key("colon:2") +  Function(lib.combination.executeCombo),
            'optic space': Key("colon, space"),
            'optic Url': Text('://'),
            'arc [<text>]': Key("lparen") +  Function(lib.combination.executeCombo),
            'arc push': Key('lparen,enter:2,escape,k:2,A'),
            'arc end': Key("rparen"),
            'whale [<text>]': Text(" => ") +  Function(lib.combination.executeCombo),
            'shark': Text("->"),
            'shark [<text>]': Text("->%(text)s"),
            'trout [<text>]': Text(">") +  Function(lib.combination.executeCombo),
            'trout less [<text>]': Text("<") + Function(lib.combination.executeCombo),
            'Cork ternary': Key('right') + Text(' ?  : ') + Key('left:3'),
            'ternary': Text(" ?  : ") +  Key('left:3'),
            'ternary start': Text("?  : ") +  Key('left:3'),
            'ternary short': Text(" ? :") +  Key("left,backspace,right,space"),
            'ternary optic': Text(' : '),
            'ternary crypt': Text(' ? '),

            'raft block': Text('[ ]') + Key('left, enter:2, up, tab'),
            'raft [<text>]': Text("[") +  Function(lib.combination.executeCombo),
            'raft end': Text("]"),
            'crimp [<text>]': Text("{") +  Function(lib.combination.executeCombo),
            'crimp push': Text('{') + Key('enter:2,escape,k:2,A'),
            'crimp end': Text("}"),
            'sever [<text>]':Text(";") +  Function(lib.combination.executeCombo),
            
            'string [<text>]': Text("'%(text)s'"),

            #  tags
            'Rasmus tag': Text('< ?php>') + Key('backspace,left:4,backspace,right:4,space'),
            'Rasmus close tag':  Key('question,rangle') + Key('backspace,rangle'),
            'Rasmus tag short': Text('< ?=>') + Key('backspace,left:2,backspace,right:2,space'),

            # logical operators
            'amp': Text("&"),
            'amp space':  Key('space,ampersand,space'),
            'amp twice':  Text(' & &') + Key('escape,X,a,space'),
            'amp twice start':  Text('& &') + Key('escape,X,a,space'),
            
            'or': Key('space,bar,space:2,bar,left,backspace:2,right,space'),
            'Cork or': Key('right,space,bar,space:2,bar,left,backspace:2,right,space'),

            # arithmetic
            'increment': Text('+ +') + Key('left, backspace, right'),
            'Christ space [<text>]': Text(" + ") + Function(lib.combination.executeCombo),
            'Christ [<text>]': Text("+") +  Function(lib.combination.executeCombo),
            "Christ equals": Text(" += "),
            'Christ twice': Text("++"),
            "(minus|subtract|subtraction)": Text(" - "),
            "(minus|subtract|subtraction) <n>": Text(" - %(n)d"),
            "(minus|subtract|subtraction) equals": Text(" -= "),
            'divide': Text(' / '),

            'mod [<text>]':  Key("percent") +  Function(lib.combination.executeCombo),
            'oust mod': Key('c, percent'),
            '(Lopp | lop) mod': Key('d, percent'),
            'slug space':  Key("space,asterisk,space"),
            'slug':  Key("asterisk"),
            'hash': Key("hash"),

            # common abbreviations and terms
            'JavaScript': Text('javascript'),
            'self': Text('self'),
            'Js': Text('js'),
            'Jason': Text('json'),
            'Jason big': Text('JSON'),
            'Id':  Text("id"),

    },
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 999999),
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
        'capital case [<text>]': Function(lib.format.capital_text),       
        'Pascal case [<text>]': Function(lib.format.pascal_case_text),
        'snake case [<text>]': Function(lib.format.snake_case_text),
        'path case [<text>]': Function(lib.format.path_case_text),
        'namespace case [<text>]': Function(lib.format.namespace_case_text),
        'squash case [<text>]': Function(lib.format.squash_text),
        'sentence case [<text>]': Function(lib.format.sentence_text),
        '(uppercase | upper case) [<text>]': Function(lib.format.uppercase_text),
        '(lowercase | lower case) [<text>]': Function(lib.format.lowercase_text),
        'hyphen case [<text>]': Function(lib.format.dash_text),
        '(spec | speck) case [<text>]': Function(lib.format.dot_text),
        'Ip case <n> <m> <x> <y>': Text('%(n)d.%(n)d.%(n)d.%(n)d'),
        'version case <n> <x> <y>': Text('%(n)d.%(n)d.%(n)d'),
        'float case <n> <x>': Text('%(n)d.%(n)d'),
    },
    extras = [
		Dictation("text"),
		IntegerRef("n", 1, 999),
		IntegerRef("m", 1, 999),
		IntegerRef("x", 1, 999),
		IntegerRef("y", 1, 999),
	]
)

builtin_statement_rule = MappingRule(
    name = 'builtin_statement',
    mapping = {
        '(brake | break)': Text('break'),
        '(brake | break) finish': Text('break;') +  Key('enter'), 
        "case": Text("case "),
        "case <text>": SCText("case '%(text)s'"),
        "catch": Text("catch () {") + Key("left:3"),
        "continue": Text("continue"),
        'continue finish':  Text('continue;') +  Key('enter'),
        "close comment": Text(" */"),
        "do while": Text("do {") +  Key('enter, rbrace,space') 
            + Text('while('),
        "else": Text("else"),
        "else if": Text("else if ( )") + Key("left, backspace"),
        "extends ": Text("extends "),
        "for": Text("for ( )") + Key("left, backspace"),
        "false": Text("false"),
        "finally": Text("finally {") + Key("enter"),
        "if": Text("if ("),
        "if not": Text("if ( !") + Key('left,backspace,escape,l,a'),
        "if <text>": Text("if (%(text)s) {") + Key("left:3"),
        'integer short': Text('int'),
        "(several | Sever) line": Key("escape,end") + Text(";"),

        "new": Text("new "),
        "return": Text("return "),
        "return finish":  Text('return;'),
        "return true": Text("return true;"),
        "return false": Text("return false;"),
        "switch": Text("switch ( ) { }") + Key('left,enter:2,up:2, escape, 0, w:2, a, delete'),
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
        'comment more': Text('/* *') + Key('left, backspace, right, enter'),
        'comment line': Key('escape,I') + Text('// ') + Key('escape'),
        'comment line <n>': Key('escape,0,c-v,%(n)d,j,k,I') + Text('// ') + Key('escape'),
        '(comment | comments) remove': Key('escape, I, delete:3, escape'),
        'echo': Text('echo '),
        'Rasmus Christ string': Key('escape,A,space,enter') + Text('. ') + Key('squote'),
        'empty': Text('empty( )') +  Key('left,backspace'),
        'not empty': Text('!empty( )') +  Key('left,backspace'),
        'for each': Text('foreach( as ) {') +  Key('enter:2,up:2,escape,dollar,6,h,i'),
        'for each short': Text('foreach( as )') + Key('escape,4,h'),
        'namespace': Text('namespace '),
        'nil': Text('null'),
        'PHP': Text("php"),
        'in array': Text('in_array('),
        "if (is | it's | its | his) set": Text("if (isset("),
        "if not (is | it's | its | his) set": Text("if ( !") + Key('left,backspace,escape,l,a')
        + Text('isset('),
        'is set': Text('isset('),
        'not is set': Text('!isset('),
        'if empty': Text('if(empty('),
        'string length': Text('strlen('),
        'block': Text('{ }') + Key('left,enter:2,up,tab'),
        'arc block': Text('( )') + Key('left,enter:2,up,tab'),
        'seal block': Key('escape,A,space') + Text('{ }') + Key('left,enter:2,up,tab'),
        'block remove': Key('percent,d:2,c-o,x'),
        "if not empty": Text("if ( !") + Key('left,backspace,escape,l,a')
        + Text('empty('),
        'Jason (in code | encode)': Text('json_encode('),
        'Jason (the code | decode)': Text('json_decode('),
        'lithium log': Text('Logger: :debug(') + Key('escape,b,h,X,e,l,a'),
        'Rasmus method': Text('_ _method_ _') + Key('escape, X, b, l, v, 5, l, tilde, h, X'),
        'die': Text('die;'),
        'index zero': Text('[0]'),
        'lithium log (air  | error)': Text('Logger: :error(') + Key('escape,b,h,X,e,l,a'),
        'lithium log notice': Text('Logger: :notice(') + Key('escape,b,h,X,e,l,a'),
        'array keys': Text('array_keys('),
        'array shift': Text('array_shift('),
        'array filter': Text('array_filter('),
        'array reduce': Text('array_reduce('),
        'array map': Text('array_map('),
        'array values': Text('array_values('),
        'Rasmus regular expression match': Text('preg_match()'),
        'string to time': Text('strtotime('),
        'Rasmus print custom': Text('pr( );') +  Key('left,left,backspace'),
        'Rasmus print custom exit': Text('pr( );exit;') +  Key('escape,b:3,a,delete'),
        'exit': Text('exit;'),
        'Rasmus print readable': Text('print_r( )') +  Key('left,backspace'),
        'Rasmus <text>': SCText('$%(text)s'),
        'static access': Text(': :') + Key('left,backspace,escape,l,a'),
        'static access <text>': Text(': :') + Key('left,backspace,escape,l,a') 
            + Text('%(text)s'),
        'static function <text>': Text(': :%(text)s( )') + Key('escape,X,b:2,h,X,w:2,a'),
        'use': Text('use '),
        'variable dump': Text('var_dump( );') + Key('left,left,backspace'),
        'variable dump exit': Text('var_dump( );exit;') + Key('escape,b:3,a,delete'),
        'whale (string | strings)': Text("'' => ''") + Key('escape,h:7,a'),
        'unset': Text('unset('),
    },
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 999)
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
