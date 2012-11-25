#!/usr/bin/env python

import os
import sys
import json

PHANTOMJS_PATH="/opt/phantomjs/"
CASPER_PATH = "/Users/sunil/github/casperjs/"

"""
Some portion of this script has been taken original casperjs
script from the casperjs project at https://github.com/n1k0/casperjs
Details of capserjs project can be found at
http://casperjs.org/
"""

PHANTOMJS_NATIVE_ARGS = [
    'cookies-file',
    'config',
    'debug',
    'disk-cache',
    'ignore-ssl-errors',
    'load-images',
    'load-plugins',
    'local-storage-path',
    'local-storage-quota',
    'local-to-remote-url-access',
    'max-disk-cache-size',
    'output-encoding',
    'proxy',
    'proxy-auth',
    'proxy-type',
    'remote-debugger-port',
    'remote-debugger-autorun',
    'script-encoding',
    'web-security',
]

def construct_command(args):
    CASPER_ARGS = []
    PHANTOMJS_ARGS = []

    for arg in args:
	found = False
	for native in PHANTOMJS_NATIVE_ARGS:
	    if arg.startswith('--%s' % native):
		PHANTOMJS_ARGS.append(arg)
		found = True
	if not found:
	    CASPER_ARGS.append(arg)

    CASPER_COMMAND = ['%s/bin/phantomjs' % (PHANTOMJS_PATH)]
    CASPER_COMMAND.extend(PHANTOMJS_ARGS)
    CASPER_COMMAND.extend([
	os.path.join(CASPER_PATH, 'bin', 'bootstrap.js'),
	'--casper-path=%s' % CASPER_PATH,
	'--cli'
    ])
    CASPER_COMMAND.extend(CASPER_ARGS)
    return CASPER_COMMAND

def command_runner(args):
    cmd = construct_command(args)
    print cmd
    import subprocess
    p = subprocess.Popen(cmd, shell=False, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    if p:
	for line in iter(p.stdout.readline, b''):
	    if line.startswith('resp:'):
		r = json.loads(line[5:])
		yield r
	    else:
		yield {
			't': 'log',
			'message': line
			}

