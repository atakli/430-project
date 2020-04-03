import os
for i in os.listdir():
	if not i.startswith('py') and i.endswith('.py'):
		os.startfile(i)