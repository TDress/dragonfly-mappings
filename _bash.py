from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef,
                       Key, Text)



grammar = Grammar("bash")


general_rule = MappingRule(
	name = "general",
	mapping = {
		"cancel": Key("c-c"),
		"kay": Key("enter"),
		"left": Key("left"),
		"right": Key("right"),

		"say <text>": Text("%(text)s"),
		},
	extras = [
		Dictation("text"),
		],
)



file_extensions_rule = MappingRule(
	name = "file extensions",
	mapping = {
		"dot text": Text(".txt"),
		"dot pie": Text(".py"),
		},
	extras = [
		],
)


bash_rule = MappingRule(
	name = "bash",
	mapping = {
		"P. W. D.": Text("pwd\n"),

		"CD dot dot": Text("cd ..\n"),
		"CD double dot": Text("cd ..\n"),
		"CD triple dot": Text("cd ../..\n"),
		"CD ": Text("cd ") + Key("tab:3"),
		"CD <text>": Text("cd %(text)s"),

		"copy": Text("cp "),
		"copy <text>": Text("cp %(text)s"),

		"make directory ": Text("mkdir "),
		"make directory <text>": Text("mkdir %(text)s\n"),

		"move": Text("mv "),
		"move <text>": Text("mv %(text)s"),
		"remove": Text("rm "),
		"remove <text>": Text("rm %(text)s"),

		"secure copy": Text("scp"),
		"secure copy <text>": Text("scp %(text)"),

		"change mode": Text("chmod "),

		"grep <text>": Text("grep %(text)s"),

		"cat": Text("cat "),
		"cat <text>": Text("cat %(text)s"),
		"exit": Text("exit\n"),

		"list": Text("ls\n"),
		"list <text>": Text("ls %(text)s"),
		"list minus L.": Text("ls -l\n"),
		"list minus A.": Text("ls -a\n"),
		"list minus one": Text("ls -1 "),

		"pipe": Text(" | "),

		"D. P. K. G. ": Text("dpkg "),
		"D. P. K. G. minus L.": Text("dpkg -l "),
		"D. P. K. G. minus I.": Text("dpkg -i "),

		"manual page": Text("man "),

		"word count": Text("wc "),
		"word count minus L.": Text("wc -l "),

		"repeat previous argument": Key("a-dot"),
		"up": Key("up"),

		# cursor movement
		"back": Key("a-b"),
		"[<n>] back": Key("a-b:%(n)d"),
		"[<n>] whiskey": Key("a-f:%(n)d"),
		"dollar": Key("c-e"),
		"hat": Key("c-a"),

		"scratch": Key("c-w"),
		"[<n>] scratch": Key("c-w:%(n)d"),
		"paste": Key("c-y"),

		"make": Text("make\n"),
		"make clean": Text("make clean\n"),

		"evince": Text("evince "),
		"evince <text>": Text("evince %(text)s"),

                "Python": Text("python "),

		"aptitude search": Text("aptitude search "),
		"pseudo-aptitude install": Text("sudo aptitude install "),
		"pseudo-aptitude update": Text("sudo aptitude update "),
		"pseudo-aptitude remove": Text("sudo aptitude remove "),

		"A. P. T. file search": Text("apt-file search "),

		"vim": Text("vim "),
		"vim <text>": Text("vim %(text)s"),


		"W. get ": Text("wget "),
		},
	extras = [
		Dictation("text"),
		IntegerRef("n", 1, 20)
		],
	defaults = {
		"n": 1
	}
)


git_rule = MappingRule(
	name = "git",
	mapping = {
		# commands for git version control
		"annals add": Text("git add "),
		"annals remove": Text("git rm "),
		"annals move": Text("git move "),
		"annals status": Text("git status\n"),
		"annals patch": Text("git add -p\n"),

		"annals branch": Text("git branch "),

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
		"annals (checkout | check out) new <text>": Text("git checkout -b  %(text)s"),
		"annals (checkout | check out) <text>": Text("git checkout %(text)s"),
		"annals (checkout | check out) minus F.": Text("git checkout -f\n"),

		"annals stash": Text("git stash\n"),

		"annals pull": Text("git pull "),
		"annals push": Text("git push "),

		"annals help": Text("git help"),
		"annals help push": Text("git help push\n"),

		"annals remote add": Text("git remote add "),
		
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
grammar.add_rule(bash_rule)
grammar.add_rule(screen_rule)
grammar.add_rule(git_rule)
grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None