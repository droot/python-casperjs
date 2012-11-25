
from runner import construct_command, command_runner

SCRIPTS_DIR = "/Users/sunil/github/casperjs/samples/"

def execute_command(cmd):
    output = command_runner(cmd)
    for r in output:
	print 'JSON Line: %s' % r 
    return 0

if __name__ == '__main__':
    try:
	args = ["%s/%s"% (SCRIPTS_DIR, 'ss.js')]
	rc = execute_command(args)
    except Exception as err:
	print(('Fatal: %s; did you install phantomjs?' % err))
	sys.exit(1)
