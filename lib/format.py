import re
import string

from dragonfly import (
    Clipboard,
    Pause,
     Text,
      Key
)

from dragonfly.actions.keyboard import Keyboard

specialCharacterTranslations = {
    "?\\question-mark": "?",
    ":\\colon": ":",
    ";\\semicolon": ";",
    "*\\asterisk": "*",
    "~\\tilde": "~",
    ",\\comma": ",",
    ".\\period": ".",
    ".\\dot": ".",
    "/\\slash": "/",
    "_\\underscore": "_",
    "!\\exclamation-mark": "!",
    "@\\at-sign": "@",
    "\\backslash": "\\",
    "(\\left-parenthesis": "(",
    ")\\right-parenthesis": ")",
    "[\\left-square-bracket": "[",
    "]\\right-square-bracket": "]",
    "{\\left-curly-bracket": "{",
    "}\\right-curly-bracket": "}",
    "<\\left-angle-bracket": "<",
    ">\\right-angle-bracket": ">",
    "|\\vertical-bar": "|",
    "$\\dollar-sign": "$",
    "=\\equals-sign": "=",
    "+\\plus-sign": "+",
    "-\\minus-sign": "-",
    "--\\dash": "-",
    "\x96\\dash": "-",
    "-\\hyphen": "-",
    "\"\\right-double-quote": "\"",
    "\"\\left-double-quote": "\"",
}

specialCharacterTranslationsRe = re.compile('|'.join(re.escape(key) for key in specialCharacterTranslations.keys()))

class SCText(Text):  # Special Characters Text.
    def __init__(self, spec=None, static=False, pause=0.02, autofmt=False):
        Text.__init__(self, spec, static, pause, autofmt)

        # Since we're not actually part of the Dragonfly Action hierarchy and dynamically dispatch to one of two
        # Action implementations, we can't simply subclass and rely on polymorphism to call the correct method.
        # That's because this class is a subclass of the container, not of the Action itself.  So, in order to ensure
        # our overridden method is called on the correct Action, we must add an unbound copy of the method to each
        # of the Actions.

        # setattr(self._dragonfly_action, "_parse_spec", self._parse_spec)
        # setattr(self._aenea_action, "_parse_spec", self._parse_spec)

    def _parse_spec(self, spec):
        """Overrides the normal Text class behavior. To handle dictation of
        special characters like / . _
        Unfortunately, I have not found a better place to solve this.

        """
        events = []
        try:
            parts = re.split("\%\([a-z_0-9]+\)s", self._spec)
            if len(parts) > 2:
                raise Exception("SCText only supports one variable, yet.")
            start = len(parts[0])
            end = len(spec) - len(parts[1])
            words = spec[start:end]
            words = strip_dragon_info(words)
            newText = ""
            for word in words:
                if (newText != "" and newText[-1:].isalnum() and
                        word[-1:].isalnum()):
                    word = " " + word  # Adds spacing between normal words.
                newText += word
            spec = parts[0] + newText + parts[1]
            for character in spec:
                if character in self._specials:
                    typeable = self._specials[character]
                else:
                    typeable = Keyboard.get_typeable(character)
                events.extend(typeable.events(self._pause))
        except Exception as e:
            print self._spec, parts
            print("Error: %s" % e)
        return events

letterMap = {
    "A\\letter": "alpha",
    "B\\letter": "bravo",
    "C\\letter": "charlie",
    "D\\letter": "delta",
    "E\\letter": "echo",
    "F\\letter": "foxtrot",
    "G\\letter": "golf",
    "H\\letter": "hotel",
    "I\\letter": "india",
    "J\\letter": "juliet",
    "K\\letter": "kilo",
    "L\\letter": "lima",
    "M\\letter": "mike",
    "N\\letter": "november",
    "O\\letter": "oscar",
    "P\\letter": "papa",
    "Q\\letter": "quebec",
    "R\\letter": "romeo",
    "S\\letter": "sierra",
    "T\\letter": "tango",
    "U\\letter": "uniform",
    "V\\letter": "victor",
    "W\\letter": "whiskey",
    "X\\letter": "x-ray",
    "Y\\letter": "yankee",
    "Z\\letter": "zulu",
}


class FormatTypes:
    camelCase = 1
    pascalCase = 2
    snakeCase = 3
    squash = 4
    upperCase = 5
    lowerCase = 6
    dashify = 7
    dotify = 8
    spokenForm = 9


def strip_backslash_info(text): 
    newWords = ""
    words = str(text).split(" ")
    for word in words:
        backslash_index = word.find("\\")
        if backslash_index > -1:
            word = word[:backslash_index]  # Remove spoken form info.
        if newWords[-1:].isalnum():
            word = " " + word  # Adds spacing between normal words.
        newWords += word
    return newWords

def strip_dragon_info(text):
    newWords = []
    words = str(text).split(" ")
    for word in words:
        word = specialCharacterTranslationsRe.sub(lambda m: specialCharacterTranslations[m.group()], word)

        backslash_index = word.find("\\")
        if backslash_index > -1:
            word = word[:backslash_index]  # Remove spoken form info.
        newWords.append(word)
    return newWords


def extract_dragon_info(text):
    newWords = []
    words = str(text).split(" ")
    for word in words:
        if word in letterMap.keys():
            word = letterMap[word]
        elif word.rfind("\\") > -1:
            pos = word.rfind("\\") + 1
            if (len(word) - 1) >= pos:
                word = word[pos:]  # Remove written form info.
            else:
                word = ""
        newWords.append(word)
    return newWords


def format_camel_case(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        if newText == '':
            newText = word[:1].lower() + word[1:]
        else:
            newText = '%s%s' % (newText, word.capitalize())
    return newText

def format_capital_case(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        if newText != "" and newText[-1:].isalnum() and word[-1:].isalnum():
            word = " " + word  # Adds spacing between normal words.
        newText += string.capwords(word)
    return newText

def format_pascal_case(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        newText = '%s%s' % (newText, word.capitalize())
    return newText


def format_snake_case(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        if newText != "" and newText[-1:].isalnum() and word[-1:].isalnum():
            word = "_" + word  # Adds underscores between normal words.
        newText += word.lower()
    return newText

def format_path_case(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        if newText != "" and newText[-1:].isalnum() and word[-1:].isalnum():
            word = "/" + word  # Adds dashes between normal words.
        newText += word
    return newText + "/"

def format_namespace_case(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        if newText != "" and newText[-1:].isalnum() and word[-1:].isalnum():
            word = "\\" + word  # Adds dashes between normal words.
        newText += word
    return newText

def format_dashify(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        if newText != "" and newText[-1:].isalnum() and word[-1:].isalnum():
            word = "-" + word  # Adds dashes between normal words.
        newText += word
    return newText


def format_dotify(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        if newText != "" and newText[-1:].isalnum() and word[-1:].isalnum():
            word = "." + word  # Adds dashes between normal words.
        newText += word
    return newText


def format_squash(text):
    newText = ""
    words = strip_dragon_info(text)
    print words
    for word in words:
        newText = '%s%s' % (newText, word)
    return newText


def format_upper_case(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        if newText != "" and newText[-1:].isalnum() and word[-1:].isalnum():
            word = " " + word  # Adds spacing between normal words.
        newText += word.upper()
        print word.upper()
    return newText

def format_sentence_case(text):
    newText = ""
    words = strip_dragon_info(text)
    isFirstWordCapitalized = False
    for word in words:
        if newText != "" and newText[-1:].isalnum() and word[-1:].isalnum():
            word = " " + word  # Adds spacing between normal words.
        if isFirstWordCapitalized:
            newText += word
            continue
        else:
            newText += " " + string.capwords(word)
    return newText

def format_lower_case(text):
    newText = ""
    words = strip_dragon_info(text)
    for word in words:
        if newText != "" and newText[-1:].isalnum() and word[-1:].isalnum():
            if newText[-1:] != "." and word[0:1] != ".":
                word = " " + word  # Adds spacing between normal words.
        newText += word.lower()
    return newText


def format_spoken_form(text):
    newText = ""
    words = extract_dragon_info(text)
    for word in words:
        if newText != "":
            word = " " + word
        newText += word
    return newText


FORMAT_TYPES_MAP = {
    FormatTypes.camelCase: format_camel_case,
    FormatTypes.pascalCase: format_pascal_case,
    FormatTypes.snakeCase: format_snake_case,
    FormatTypes.squash: format_squash,
    FormatTypes.upperCase: format_upper_case,
    FormatTypes.lowerCase: format_lower_case,
    FormatTypes.dashify: format_dashify,
    FormatTypes.dotify: format_dotify,
    FormatTypes.spokenForm: format_spoken_form,
}


def format_text(text, formatType=None):
    if formatType:
        if type(formatType) != type([]):
            formatType = [formatType]
        result = ""
        method = None
        for value in formatType:
            if not result:
                if formatType == FormatTypes.spokenForm:
                    result = text.words
                else:
                    result = str(text)
            method = FORMAT_TYPES_MAP[value]
            result = method(result)
        Text("%(text)s").execute({"text": result})


def remove_spaces_text(text):
    s = str(text)
    print s
    Text(re.sub('\s', '', text)).execute()
    
def namespace_case_text(text):
    """Formats dictated text to namespace case

    Example:
    "'path case my new variable'" => "my\new\variable".

    """
    newText = format_namespace_case(text)
    Text("%(text)s").execute({"text": newText})


def path_case_text(text):
    """Formats dictated text to path case

    Example:
    "'path case my new variable'" => "my/new/variable".

    """
    newText = format_path_case(text)
    Text("%(text)s").execute({"text": newText})


def camel_case_text(text):
    """Formats dictated text to camel case.

    Example:
    "'camel case my new variable'" => "myNewVariable".

    """
    newText = format_camel_case(text)
    Text("%(text)s").execute({"text": newText})


def camel_case_count(n):
    """Formats n words to the left of the cursor to camel case.
    Note that word count differs between editors and programming languages.
    The examples are all from Eclipse/Python.

    Example:
    "'my new variable' *pause* 'camel case 3'" => "myNewVariable".

    """
    saveText = _get_clipboard_text()
    cutText = _select_and_cut_text(n)
    if cutText:
        endSpace = cutText.endswith(' ')
        text = _cleanup_text(cutText)
        newText = _camelify(text.split(' '))
        if endSpace:
            newText = newText + ' '
        newText = newText.replace("%", "%%")  # Escape any format chars.
        Text(newText).execute()
    else:  # Failed to get text from clipboard.
        Key('c-v').execute()  # Restore cut out text.
    _set_clipboard_text(saveText)


def _camelify(words):
    """Takes a list of words and returns a string formatted to camel case.

    Example:
    ["my", "new", "variable"] => "myNewVariable".

    """
    newText = ''
    for word in words:
        if newText == '':
            newText = word[:1].lower() + word[1:]
        else:
            newText = '%s%s' % (newText, word.capitalize())
    return newText


def pascal_case_text(text):
    """Formats dictated text to pascal case.

    Example:
    "'pascal case my new variable'" => "MyNewVariable".

    """
    newText = format_pascal_case(text)
    Text("%(text)s").execute({"text": newText})


def pascal_case_count(n):
    """Formats n words to the left of the cursor to pascal case.
    Note that word count differs between editors and programming languages.
    The examples are all from Eclipse/Python.

    Example:
    "'my new variable' *pause* 'pascal case 3'" => "MyNewVariable".

    """
    saveText = _get_clipboard_text()
    cutText = _select_and_cut_text(n)
    if cutText:
        endSpace = cutText.endswith(' ')
        text = _cleanup_text(cutText)
        newText = text.title().replace(' ', '')
        if endSpace:
            newText = newText + ' '
        newText = newText.replace("%", "%%")  # Escape any format chars.
        Text(newText).execute()
    else:  # Failed to get text from clipboard.
        Key('c-v').execute()  # Restore cut out text.
    _set_clipboard_text(saveText)

def strip_dragon_info_text(text): 
    newText = strip_dragon_info(text)
    Text("%(text)s").execute({"text": newText})

def snake_case_text(text):
    """Formats dictated text to snake case.

    Example:
    "'snake case my new variable'" => "my_new_variable".

    """
    newText = format_snake_case(text)
    Text("%(text)s").execute({"text": newText})

def dash_text(text):
    """Formats dictated text to dash case.

    """
    newText = format_dashify(text)
    Text("%(text)s").execute({"text": newText})

def dot_text(text):
    """Formats dictated text to dot case.

    """
    newText = format_dotify(text)
    Text("%(text)s").execute({"text": newText})

def snake_case_count(n):
    """Formats n words to the left of the cursor to snake case.
    Note that word count differs between editors and programming languages.
    The examples are all from Eclipse/Python.

    Example:
    "'my new variable' *pause* 'snake case 3'" => "my_new_variable".

    """
    saveText = _get_clipboard_text()
    cutText = _select_and_cut_text(n)
    if cutText:
        endSpace = cutText.endswith(' ')
        text = _cleanup_text(cutText.lower())
        newText = '_'.join(text.split(' '))
        if endSpace:
            newText = newText + ' '
        newText = newText.replace("%", "%%")  # Escape any format chars.
        Text(newText).execute()
    else:  # Failed to get text from clipboard.
        Key('c-v').execute()  # Restore cut out text.
    _set_clipboard_text(saveText)


def squash_text(text):
    """Formats dictated text with whitespace removed.

    Example:
    "'squash my new variable'" => "mynewvariable".

    """
    newText = format_squash(text)
    Text("%(text)s").execute({"text": newText})


def squash_count(n):
    """Formats n words to the left of the cursor with whitespace removed.
    Excepting spaces immediately after comma, colon and percent chars.

    Note: Word count differs between editors and programming languages.
    The examples are all from Eclipse/Python.

    Example:
    "'my new variable' *pause* 'squash 3'" => "mynewvariable".
    "'my<tab>new variable' *pause* 'squash 3'" => "mynewvariable".
    "( foo = bar, fee = fye )", 'squash 9'" => "(foo=bar, fee=fye)"

    """
    saveText = _get_clipboard_text()
    cutText = _select_and_cut_text(n)
    if cutText:
        endSpace = cutText.endswith(' ')
        text = _cleanup_text(cutText)
        newText = ''.join(text.split(' '))
        if endSpace:
            newText = newText + ' '
        newText = _expand_after_special_chars(newText)
        newText = newText.replace("%", "%%")  # Escape any format chars.
        Text(newText).execute()
    else:  # Failed to get text from clipboard.
        Key('c-v').execute()  # Restore cut out text.
    _set_clipboard_text(saveText)


def expand_count(n):
    """Formats n words to the left of the cursor by adding whitespace in
    certain positions.
    Note that word count differs between editors and programming languages.
    The examples are all from Eclipse/Python.

    Example, with to compact code:
    "result=(width1+width2)/2 'expand 9' " => "result = (width1 + width2) / 2"

    """
    saveText = _get_clipboard_text()
    cutText = _select_and_cut_text(n)
    if cutText:
        endSpace = cutText.endswith(' ')
        cutText = _expand_after_special_chars(cutText)
        reg = re.compile(
            r'([a-zA-Z0-9_\"\'\)][=\+\-\*/\%]|[=\+\-\*/\%][a-zA-Z0-9_\"\'\(])')
        hit = reg.search(cutText)
        count = 0
        while hit and count < 10:
            cutText = cutText[:hit.start() + 1] + ' ' + \
                cutText[hit.end() - 1:]
            hit = reg.search(cutText)
            count += 1
        newText = cutText
        if endSpace:
            newText = newText + ' '
        newText = newText.replace("%", "%%")  # Escape any format chars.
        Text(newText).execute()
    else:  # Failed to get text from clipboard.
        Key('c-v').execute()  # Restore cut out text.
    _set_clipboard_text(saveText)


def _expand_after_special_chars(text):
    reg = re.compile(r'[:,%][a-zA-Z0-9_\"\']')
    hit = reg.search(text)
    count = 0
    while hit and count < 10:
        text = text[:hit.start() + 1] + ' ' + text[hit.end() - 1:]
        hit = reg.search(text)
        count += 1
    return text


def uppercase_text(text):
    """Formats dictated text to upper case.

    Example:
    "'upper case my new variable'" => "MY NEW VARIABLE".

    """
    newText = format_upper_case(text)
    Text("%(text)s").execute({"text": newText})

def sentence_text(text):
    """Formats dictated text to upper case for only the first letter of first word.

    Example:
    "'upper case my new variable'" => "My new variable"

    """
    newText = format_sentence_case(text)
    Text("%(text)s").execute({"text": newText})

def capital_text(text):
    """Formats dictated text to capitalized words.

    Example:
    "'upper case my new variable'" => "My New Variable"

    """
    newText = format_capital_case(text)
    Text("%(text)s").execute({"text": newText})

def uppercase_count(n):
    """Formats n words to the left of the cursor to upper case.
    Note that word count differs between editors and programming languages.
    The examples are all from Eclipse/Python.

    Example:
    "'my new variable' *pause* 'upper case 3'" => "MY NEW VARIABLE".

    """
    saveText = _get_clipboard_text()
    cutText = _select_and_cut_text(n)
    if cutText:
        newText = cutText.upper()
        newText = newText.replace("%", "%%")  # Escape any format chars.
        Text(newText).execute()
    else:  # Failed to get text from clipboard.
        Key('c-v').execute()  # Restore cut out text.
    _set_clipboard_text(saveText)

def strip_backslash_case(text): 
    newText = strip_backslash_info(text)
    Text("%(text)s").execute({"text": newText})

def lowercase_text(text):
    """Formats dictated text to lower case.

    Example:
    "'lower case John Johnson'" => "john johnson".

    """
    newText = format_lower_case(text)
    Text("%(text)s").execute({"text": newText})


def lowercase_count(n):
    """Formats n words to the left of the cursor to lower case.
    Note that word count differs between editors and programming languages.
    The examples are all from Eclipse/Python.

    Example:
    "'John Johnson' *pause* 'lower case 2'" => "john johnson".

    """
    saveText = _get_clipboard_text()
    cutText = _select_and_cut_text(n)
    if cutText:
        newText = cutText.lower()
        newText = newText.replace("%", "%%")  # Escape any format chars.
        Text(newText).execute()
    else:  # Failed to get text from clipboard.
        Key('c-v').execute()  # Restore cut out text.
    _set_clipboard_text(saveText)


def _cleanup_text(text):
    """Cleans up the text before formatting to camel, pascal or snake case.

    Removes dashes, underscores, single quotes (apostrophes) and replaces
    them with a space character. Multiple spaces, tabs or new line characters
    are collapsed to one space character.
    Returns the result as a string.

    """
    prefixChars = ""
    suffixChars = ""
    if text.startswith("-"):
        prefixChars += "-"
    if text.startswith("_"):
        prefixChars += "_"
    if text.endswith("-"):
        suffixChars += "-"
    if text.endswith("_"):
        suffixChars += "_"
    text = text.strip()
    text = text.replace('-', ' ')
    text = text.replace('_', ' ')
    text = text.replace("'", ' ')
    text = re.sub('[ \t\r\n]+', ' ', text)  # Any whitespaces to one space.
    text = prefixChars + text + suffixChars
    return text


def _get_clipboard_text():
    """Returns the text contents of the system clip board."""
    clipboard = Clipboard()
    return clipboard.get_system_text()


def _select_and_cut_text(wordCount):
    """Selects wordCount number of words to the left of the cursor and cuts
    them out of the text. Returns the text from the system clip board.

    """
    clipboard = Clipboard()
    clipboard.set_system_text('')
    Key('cs-left/3:%s/10, c-x/10' % wordCount).execute()
    return clipboard.get_system_text()


def _set_clipboard_text(text):
    """Sets the system clip board content."""
    clipboard = Clipboard()
    clipboard.set_text(text)  # Restore previous clipboard text.
    clipboard.copy_to_system()
