def angle(angles,pin_code):
	"""
	Arguments: angles(dicionary),pin_code(string)
	returns: angles(dictionary),degree(integer)
	Return Note:
	angles: modified dictionary
	degree: the value to be rotated
	"""
	angles = dict(angles)
	try:
		x=angles[pin_code]
		return angles,x
	except:
		if(len(angles)==0):
			angles[pin_code]=150
		elif(len(angles)==1):
			angles[pin_code]=180
		else:
			angles[pin_code]=210
		return angles,angles[pin_code]
