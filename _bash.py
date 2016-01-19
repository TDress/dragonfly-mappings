from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text, Function)

import lib.combination

grammar = Grammar("bash")


general_rule = MappingRule(
	name = "general",
	mapping = {
                'bash back': Key('c-pgup'),
                'bash (clothes | close)': Key('cs-w'),
                'bash copy': Key('cs-c'),
                'bash next': Key('c-pgdown'),
                'bash new': Key('cs-t'),
                'bash paste':Key('cs-v'),
                'bash page up': Key('s-pgup'),
                'Bash page down': Key('s-pgdown'),
		"cancel": Key("c-c"),
                'end of file': Key('c-d'),
                "Lennix | Lenox": Text("linux"),
		"say <text>": Text("%(text)s"),
		},
	extras = [
		Dictation("text"),
                 IntegerRef('n',1, 99)
		],
        defaults = {
            "n":1
        }
)



file_extensions_rule = MappingRule(
	name = "file extensions",
	mapping = {
		"dot text": Text(".txt"),
		"dot pie": Text(".py"),
                'dot Php': Text('.php'),
                'dot Js': Text('.js'),
                'dot Html': Text('.html')
		},
	extras = [
		],
)

symbol_rule = MappingRule(
        name = "symbols",
        mapping = {
            'backslash [<text>]':  Key('backslash') +  Function(lib.combination.executeCombo),
            'slash [<text>]':  Key('slash') +  Function(lib.combination.executeCombo),
            "caret | carrot":  Text("^"),
            'hyphen [<text>]': Key('hyphen') +  Function(lib.combination.executeCombo),
        },
        extras = [
             Dictation("text")
        ],
        defaults = {
            'text':''
        }
)

bash_rule = MappingRule(
	name = "bash",
	mapping = {
                "curl [<text>]": Text("curl ") +  Function(lib.combination.executeCombo),
		"P. W. D.": Text("pwd\n"),

		"CD dot dot": Text("cd ..\n"),
		"CD double dot": Text("cd ..\n"),
                'double dot':Text('../'),
		"CD triple dot": Text("cd ../..\n"),
		"CD ": Text("cd ") + Key("tab:2"),
		"CD <text>": Text("cd %(text)s"),

		"copy": Text("cp "),
		"copy <text>": Text("cp %(text)s"),

                "disc freedom": Text("df -h"),

		"make directory ": Text("mkdir "),
		"make directory <text>": Text("mkdir %(text)s\n"),

		"move": Text("mv "),
		"move <text>": Text("mv %(text)s"),
		"remove": Text("rm "),
		"remove recursive": Text("rm -r "),
		"remove <text>": Text("rm %(text)s"),

		"secure copy": Text("scp"),
		"secure copy <text>": Text("scp %(text)"),

                "perms mod": Text("chmod "),
                #"perms mod": Text("chmod "),

                "rake history":  Text("history | grep ''"),
		"(rate recursive | rake recursive | Raker cursive)": Text("grep -r ''") + Key('left'),
		"rake": Text("grep ''") +  Key('left'),

                # viewing files and text
		"cat": Text("cat "),
		"cat <text>": Text("cat %(text)s"),
                '(tail|tale)': Text("tail "),
                '(tail|tale) follow': Text("tail -f "),

		"exit": Text("exit\n"),

		"list": Text("ls\n"),
		"list <text>": Text("ls %(text)s"),
		"list minus L.": Text("ls -l\n"),
		"list minus A.": Text("ls -a\n"),
		"list minus one": Text("ls -1 "),

                'symbolic link': Text('ln -s '),
		"pipe space": Text(" | "),
		"pipe": Text("|"),
        'pipe twice': Key('bar,space:2,bar,left,backspace:2,right'),

		"D. P. K. G. ": Text("dpkg "),
		"D. P. K. G. minus L.": Text("dpkg -l "),
		"D. P. K. G. minus I.": Text("dpkg -i "),

		"man": Text("man "),
                "S Sh":Text("ssh "),

                "Cron | Craun": Text("cron"),

		"word count": Text("wc "),
		"word count minus L.": Text("wc -l "),

		"bash previous argument": Key("a-dot"),

		# cursor movement
                "[<n>] left [<text>]": Key("left:%(n)d") + Function(lib.combination.executeCombo),
                "[<n>] right [<text>]": Key("right:%(n)d") + Function(lib.combination.executeCombo),

		"[<n>] left word": Key("a-b:%(n)d"),
		"[<n>] right word": Key("a-f:%(n)d"),
		"bash Buck": Key("c-e"),

                "[<n>] backspace": Key("backspace:%(n)d"),
                '[<n>] delete [<text>]': Key("delete:%(n)d") + Function(lib.combination.executeCombo),
		"[<n>] scratch back": Key("a-backspace:%(n)d"),
		"[<n>] scratch next": Key("a-d:%(n)d"),
                "scratch tail":Key("c-k"),
                "scratch head":Key("c-u"),

                "Sudo":Text("sudo "),
		"pseudo-aptitude install": Text("sudo apt-get install "),
		"pseudo-aptitude update": Text("sudo apt-get update "),
		"pseudo-aptitude remove": Text("sudo apt-get remove "),

		"A. P. T. file search": Text("apt-file search "),

		"vim": Text("vim "),

		"W. get ": Text("wget "),

                # screen
                "screen start": Text("screen") +  Key('enter:2'),
                "screen new": Key('c-a,c'),
                "screen next": Key('c-a,space'),
                "screen back": Key('c-a,backspace'),
                "screen list": Key('c-a,c-w'),
                "screen last": Key('c-a,c-a'),
                "screen <n>": Key('c-a,%(n)d'),
                "screen copy":Key('c-a,lbracket'),
                "screen paste":Key('c-a,rbracket'),
                "screen kill": Key('c-a,k'),
                # node package manager
                'node packages':  Text('npm '),
                'node packages install':  Text('npm install') +  Key('enter'),
                'node packages build':  Text('npm build') +  Key('enter'),

        },
	extras = [
		Dictation("text"),
		IntegerRef("n", 0, 50)
		],
	defaults = {
		"n": 1,
                "text": ""
	}
)


git_rule = MappingRule(
	name = "git",
	mapping = {
		# commands for git version control
                "annals": Text("git "),
		"annals add": Text("git add "),
		"annals remove": Text("git rm "),
		"annals move": Text("git move "),
		"annals status": Text("git status\n"),
		"annals patch": Text("git add -p\n"),

		"annals branch": Text("git branch "),
                "annals branch description[s]":Text('git-branch') + Key('enter'),
                "annals branch edit description": Text('git branch --edit-description '),

		"annals merge": Text("git merge "),
		"annals merge not fast forward": Text("git merge --no-ff "),

		"annals log": Text("git log\n"),
		"annals log [color] words": Text("git log -p --color-words\n"),
		"annals log minus (P.|patch)": Text("git log -p\n"),
		"annals log minus stat": Text("git log --stat\n"),

		"annals diff": Text("git diff\n"),
		"annals diff [color] words": Text("git diff --color-words\n"),
		"annals diff (cache | cash)": Text("git diff --color-words --cached\n"),

		"annals commit message": Text("git commit -m ''") + Key("left"),
		"annals commit add message": Text("git commit -a -m ''") + Key("left"),
		"annals commit": Text("git commit "),
		"annals commit --amend": Text("git commit --amend\n"),

		"annals (checkout | check out)": Text("git checkout "),
		"annals (checkout | check out) new": Text("git checkout -b "),
		"annals (checkout | check out) fresh": Text("git checkout -- "),
		"annals (checkout | check out) new <text>": Text("git checkout -b  %(text)s"),
		"annals (checkout | check out) <text>": Text("git checkout %(text)s"),
		"annals (checkout | check out) minus F.": Text("git checkout -f\n"),
		"annals (checkout | check out) master": Text("git checkout master") + Key('enter'),

                "annals push": Text("git push "),
                'annals push origin':  Text('git push origin '),
                'annals push origin master':  Text('git push origin master'),
                'annals (Paul | pull)':Text('git pull '),
                'annals (Paul | pull) origin':Text('git pull origin'),
                'annals (Paul | pull) origin master':Text('git pull origin master'),
                'annals show': Text('git show '),
		"annals stash": Text("git stash\n"),

		"annals help": Text("git help"),
		"annals help push": Text("git help push\n"),

		"annals remote add": Text("git remote add "),
		"annals remote version": Text("git remote -v") + Key("enter")		
		},
	extras = [
		Dictation("text"),
		],
)

apache_rule = MappingRule(
	name = "apache",
	mapping = {
                "Apache": Text("apache "),
                "Apache restart":Text("sudo apachectl restart")
		},
	extras = [
		Dictation("text"),
		],
)


prefix_key = "c-a"

screen_rule = MappingRule(
	name = "screen",
	mapping = {
		"switch to (screen | window) <n>": Key(prefix_key) + Key("%(n)d"),
		"switch to (window next | next window | screen next | next screen)":
			Key(prefix_key) + Key("n"),
		"switch to (window previous | previous window | screen previous | previous screen)":
			Key(prefix_key) + Key("p"),
		"create (screen | window)": Key(prefix_key) + Key("c"),
		},
	extras = [
		IntegerRef("n", 0, 20)
		]
)


grammar.add_rule(general_rule)
grammar.add_rule(file_extensions_rule)
grammar.add_rule(symbol_rule)
grammar.add_rule(bash_rule)
grammar.add_rule(screen_rule)
grammar.add_rule(git_rule)
grammar.add_rule(apache_rule)
grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
