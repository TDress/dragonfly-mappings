from dragonfly import (
    Function,
    MappingRule,
    Grammar,
    Dictation,
    IntegerRef,
     Text,
      Key
)

import lib.format
from lib.format import SCText

def define_function(text):
    Text("function ").execute()
    lib.format.camel_case_text(text)
    Text("() {").execute()
    Key("left:3").execute()


rules = MappingRule(
    mapping={
        # Keywords:
        'console log': Text('console.log(.);') +  Key('left:2,backspace'),
        'console error': Text('console.error(.);') +  Key('left:2,backspace'),
        'console warn': Text('console.warn(.);') +  Key('left:2,backspace'),
        'constant [<text>]': Text('const %(text)s'),
        "debugger": Text("debugger"),
        "default": Text("default"),
        "function": Text("function "),
        "function <text>": Function(define_function),
        "instanceof": Text("instanceof ") + Key("left"),
        "in": Text("in "),
        "in <text>": SCText("in %(text)s"),
        "((jquery|jay query) (variable|var)|dollar paren)": Text("$()") + Key("left"),  # @IgnorePep8
        "object": Text("Object "),
        "for in": Text('for( var  in )') + Key('left:9,backspace,right:4'),
        "reg exp": Text("RegExp"),
        "string object": Text("String"),
        "this": Text("this"),
        "typeof": Text("typeof "),
        "to String": Text("toString()") + Key("left"),
        'variable short': Text('var'),
        "variable (define | defined)": Text("var "),
        "let (define | defined)": Text("let "),
        "(variable|var) (define | defined) <text>": SCText("var %(text)s"),
        "let (define | defined) <text>": SCText("let %(text)s"),
        "with": Text("with () {") + Key("left:3"),
        "with <text>": SCText("with (%(text)s) {") + Key("left:3"),
        # Global variables and objects.
        "window": Text("window"),
        "undefined": Text("undefined"),
        "use strict": Text("'use strict';"),
    },
    extras=[
        IntegerRef("n", 1, 100),
        Dictation("text"),
    ],
    defaults={
        "n": 1,
        "text": ''
    }
)

grammar = Grammar("JavaScript grammar")
grammar.add_rule(rules)
grammar.load()

# Unload function which will be called at unload time.
def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
