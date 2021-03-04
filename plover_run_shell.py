'''
Execute shell command in Plover using strokes.
'''

import os


def shell_cmd(_: 'plover.engine.StenoEngine', command: str):
	'''
	Command to execute a shell command.
	:param _: The Plover engine that is executing the command.
	:param command: The command to execute.
	'''
	os.system(command)
