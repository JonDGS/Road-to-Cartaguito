import json
import operator

with open("NewSaveFile.json", "r") as f:
	data = json.load(f)



def compare(data):
	x = data['players'][4]['total']
	y = data['players'][4]['laps']
	z = data['players'][4]['hits']
	i = 0
	for leader in data['players']:
		i += 1
		if x > leader['total']:
			a = x
			b = y
			c = z
			x = data['players'][i]['total']
			y = data['players'][i]['laps']
			z = data['players'][i]['hits']
			data['players'][i]['total'] = data['players'][a]['total']
			data['players'][i]['laps'] = data['players'][b]['laps']
			data['players'][i]['hits'] = data['players'][c]['hits']
		elif x == leader['total']:
			if y > leader['laps']:
				a = x
				b = y
				c = z
				x = data['players'][i]['total']
				y = data['players'][i]['laps']
				z = data['players'][i]['hits']
				data['players'][i]['total'] = data['players'][a]['total']
				data['players'][i]['laps'] = data['players'][b]['laps']
				data['players'][i]['hits'] = data['players'][c]['hits']
			elif y == leader['laps']:
				if z > leader['hits']:
					a = x
					b = y
					c = z
					x = data['players'][i]['total']
					y = data['players'][i]['laps']
					z = data['players'][i]['hits']
					data['players'][i]['total'] = data['players'][a]['total']
					data['players'][i]['laps'] = data['players'][b]['laps']
					data['players'][i]['hits'] = data['players'][c]['hits']
				elif z == leader['hits'] or z < leader['hits']:
					pass
			else:
				pass
		else:
			pass
	return data

		


def leaderboard(x, y, z):
	i = 0
	found = False
	changes = [0, 0, 0]
	global data
	for leader in data['players']:
		if not found:
			if x > leader['total']:
				changes[0] = x
				changes[1] = y
				changes[2] = z
				found = True
			elif x == leader['total']:
				if y > leader['laps']:
					changes[0] = x
					changes[1] = y
					changes[2] = z
					found = True
				elif y == leader['laps']:
					if z > leader['hits']:
						changes[0] = x
						changes[1] = y
						changes[2] = z
						found = True
					elif z == leader['hits'] or z < leader['hits']:
						pass
				else:
					pass
			else:
				pass
		else:
			pass
	if found == True and changes[0] != 0:
		for leader in data['players']:
			i += 1
			if i == 5:
				leader['total'] = x
				leader['laps'] = y
				leader['hits'] = z
			else:
				pass
		data = compare(data)
		json.dump(data, open("NewSaveFile.json", "w"), indent=2)
	else:
		pass



