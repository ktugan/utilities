if __name__ == '__main__':
	import wmi
	import sys

	no_argument = len(sys.argv) != 2 
	no_number = not sys.argv[1].isdigit()
	brightness = int(sys.argv[1]) # percentage [0-100]
	no_valid_range = brightness < 0 or brightness > 100
	
	if no_argument or no_number or no_valid_range:
		print('Include brightness in %% as a number [0-100].')
		exit()

	c = wmi.WMI(namespace='wmi')

	methods = c.WmiMonitorBrightnessMethods()[0]
	methods.WmiSetBrightness(brightness, 0)