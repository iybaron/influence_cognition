import sys

s = 'FPWT'

sys.stdout.write('\'' + s + '\', ')
for i in range(1, 81):
	sys.stdout.write('\'' + s + str(i) + '\', ')
sys.stdout.flush()