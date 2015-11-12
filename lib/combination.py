from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text, Function)

import lib.vim 
import lib.chars 
#import lib.vim 
#import lib.vim 
#import lib.vim 
#import lib.vim 
#import lib.vim 

# combine all library mappings for inclusion in the combination function.
allMappings = reduce(
    # map update() has no return, so use logical or
    lambda acc,y: acc.update(y) or acc,
    [lib.vim.vimMapping, lib.chars.charMapping]
)
print lib.vim.vimMapping
print lib.chars.charMapping
print allMappings
# executes keystroke combinations 
#   @recursive
#   loops over all words in text and executes
#   any commands that exist in all vocabulary.
#   Recursive calls are made for any text after the command.
def executeCombo(text):
    text = str(text)
    if len(text) < 1:
        return
    words = text.split(" ")

    for i in range(len(words),0,-1):
        command = ' '.join(words[0:i])
        if command in allMappings.keys():
            Key(allMappings[command]).execute()
            if len(words)-1 > i:
                remainder = words[i+1:len(words)-1]
                remainder_text = ' '.join(remainder)
                return executeCombo(remainder_text)
            else:
                return
    #Text(text).execute()




