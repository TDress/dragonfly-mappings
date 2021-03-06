from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text, Function)
import lib.format

import lib.vim 
import lib.chars 
import lib.environment
import lib.programming 
import lib.bash 
#import lib.vim 
#import lib.vim 

# combine all library mappings for inclusion in the combination function.
allMappings = reduce(
    # map update() has no return, so use logical or
    lambda acc,y: acc.update(y) or acc,
    [
        lib.vim.vimMapping, 
        lib.chars.charMapping, 
        lib.environment.environment_mapping,
        lib.programming.programming_mapping,
        lib.bash.bashMapping
    ]
)

# executes keystroke combinations 
#   @recursive
#   loops over all words in text and executes
#   any commands that exist in all vocabulary.
#   Recursive calls are made for any text after the command.
def executeCombo(text):
    words = lib.format.strip_backslash_info(text).split(" ")

    print 'calling execute combo'
    print words
    if len(words) < 1:
        return

    for i in range(len(words),0,-1):
        command = ' '.join(words[0:i]).lower()
        print command
        if command in allMappings.keys():
            Key(allMappings[command]).execute()
            if len(words) > i:
                remainder = words[i:len(words)]
                remainder_text = ' '.join(remainder)
                return executeCombo(remainder_text)
            else:
                return
    #Text(text).execute()




