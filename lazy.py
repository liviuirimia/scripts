import time, sys, subprocess, shlex, socket

ips = ([sys.argv[x+1] for x in xrange(len(sys.argv)-1)])
nb = []
lst = []

FILE_PATH = "iptables.b"
SEARCH_STRING = "#add ip here\n"

def banIP(ip):
	with open(FILE_PATH, 'r') as f:
		for line in f:
			if line == SEARCH_STRING:
				line = line + "\n#" + time.ctime()
				for x in ip:
					s = "-A INPUT -s " + x + " -j DROP"
					line = line + "\n" + s
				line = line + "\n"
			nb.append(line)

	with open(FILE_PATH, 'w') as f:
		f.seek(0)
		f.truncate()

		for line in nb:
			f.write(line)

def validateIP(ip):
	if ip.count('.') != 3:
		return False
	try:
		socket.inet_aton(ip)
	except socket.error:
		return False
	else:
		return True

if __name__ == "__main__":
	grep_cmd = "grep -E -o \"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\""
	cmd = grep_cmd + " " + FILE_PATH
	args = shlex.split(cmd)
	p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	p.wait()

	lst = p.stdout.read().split("\n")
	uip = [ips[i] for i in xrange(len(ips)) if ips[i] not in lst]
	banIP([uip[x] for x in xrange(len(uip)) if validateIP(uip[x])])