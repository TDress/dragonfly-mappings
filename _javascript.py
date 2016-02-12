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
        "debugger": Text("debugger"),
        "default": Text("default"),
        "function": Text("function "),
        "function <text>": Function(define_function),
        "instanceof": Text("instanceof ") + Key("left"),
        "in": Text("in "),
        "in <text>": SCText("in %(text)s"),
        "((jquery|jay query) (variable|var)|dollar paren)": Text("$()") + Key("left"),  # @IgnorePep8
        "object": Text("Object "),
        "reg exp": Text("RegExp"),
        "string object": Text("String"),
        "this": Text("this"),
        "typeof": Text("typeof "),
        "to String": Text("toString()") + Key("left"),
        'variable short': Text('var'),
        "variable (define | defined)": Text("var "),
        "(variable|var) (define | defined) <text>": SCText("var %(text)s"),
        "with": Text("with () {") + Key("left:3"),
        "with <text>": SCText("with (%(text)s) {") + Key("left:3"),
        # Global variables and objects.
        "window": Text("window"),
        "undefined": Text("undefined"),
    },
    extras=[
        IntegerRef("n", 1, 100),
        Dictation("text"),
    ],
    defaults={
        "n": 1
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
