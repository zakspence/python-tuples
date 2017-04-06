zoo = 'octopus', 'starfish', 'dolphin', 'sperm whale', 'manta ray'

print(zoo)

animal=zoo.index('starfish')

print(animal)

for val in zoo:
	if val=='octopus':
		print(True)
	else:
		print('Here a {}'.format(val))

zoo=list(zoo)
zoo.extend(['sea urchin', 'sea horse', 'sea turtle'])
print('new zoo be like {}'.format(zoo))

zoo=tuple(zoo)
print(type(zoo))