import sys
import time

ips = ([sys.argv[x+1] for x in xrange(len(sys.argv)-1)])
nb = []

FILE_PATH = "/path/to/iptables"
SEARCH_STRING = "#add ip here\n"

if __name__ == "__main__":
	with open(FILE_PATH, 'r') as f:
		for line in f:
			if line == SEARCH_STRING:
				line = line + "\n#" + time.ctime()
				for ip in ips:
					s = "-A INPUT -s " + ip + " -j DROP"
					line = line + "\n" + s
				line = line + "\n"
			nb.append(line)

	with open(FILE_PATH, 'w') as f:
		f.seek(0)
		f.truncate()

		for line in nb:
			f.write(line)