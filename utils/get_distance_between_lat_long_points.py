from math import sin, cos, sqrt, atan2, radians


def get_distance(point1, point2):
	R = 6370
	lon1 = radians(point1[0])  # insert value
	lat1 = radians(point1[1])
	lon2 = radians(point2[0])
	lat2 = radians(point2[1])

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))
	distance = R * c
	return distance


if __name__ == "__main__":
	point1 = (-80.478230, 25.565119)
	point2 = (-80.478080, 25.550508)
	print(round(get_distance(point2, point1),2))
