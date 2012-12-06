#!/usr/bin/python

import os, re, sys

def getargs(cmd):

	matches = re.search('^[^#]*', cmd)
	return matches.group(0).split()

def execute(args):

	childpid = 0 # Child process ID.
	childpid = os.fork()

	if (childpid == -1):
		print("fork (failed to execute command)")

	elif (childpid == 0): 
		# Executes command in args[0]. 
		# Searches for that file in the directories.
		if (-1 == os.execvp(args[0], args)):
			print("execvp (couldn't find command)")
			sys.exit(0)

	else:
		# Wait until child process finishes.
		os.waitpid(childpid, 0)

	return

def shell():

	shellArgs = sys.argv	# Shell Arguments
	argc = len(sys.argv)	# Count of Arguments

	# Read from the file.
	if (len(sys.argv) >= 2):
		mystdin = file(sys.argv[1])
		my_args = getargs(mystdin.readline())
		execute(my_args)

	while True:

		# Print our shell prompt.
		sys.stdout.write('(myshell) ')
		# Flush from output buffer to terminal.
		sys.stdout.flush()

		# Read command.
		command = sys.stdin.readline()
		my_args = getargs(command)

		# Check first for built-in commands.
		if (argc > 0 and my_args[0] == "exit"):
			sys.exit(0)
		elif (argc > 0 and my_args[0] == "logout"):
			sys.exit(0)
		else:
			execute(my_args)

shell()
