from dragonfly import Grammar, MappingRule, Text, Key

grammar = Grammar('programming')

class SymbolsRule(MappingRule):
    mapping = {
	//comparison operators
	  '(Stowe | stow)': Key("space, equal, space"),
	  'tick single': Key("apostrophe"),
	  'tick double': Key("dquote"),
	  '(way | weigh) (stow | Stowe)': Key("space, equal, equal, space"),
	  'way (stow | Stowe) strict': Key("space, equal, equal, equal, space"),
	  'way bang': Key("space, exclamation, equal, space"),
	  'way bang strict': Key("space, exclamation, equal, equal, space"),
	  'way trout equal': Key("space, rangle, equal, space"),
	  'way whale flip': Key("space,langle, equal, space"),
	  'crypt': Key("question"),
	  'crypt optic': Key("question,colon"),
	  
	// mappings, brackets and miscellaneous
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

	// arithmetic
	  'Christ space': Text(" + "),
	  'Christ': Text("+"),
	  'shorn space': Text(" - "),
	  'shorn': Text("-"),
	  
        }

grammar.add_rule(SymbolsRule())
grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None