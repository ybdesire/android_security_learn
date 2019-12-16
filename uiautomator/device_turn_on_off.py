from uiautomator import device as d

if d.screen == "on":  # of d.screen != "off"
	print('device is turn on, will turn off now')
    # Turn off screen
	d.screen.off()
if d.screen == "off":  # of d.screen != "on"
	print('device is turn off, will turn on now')
	# Turn on screen
	d.screen.on()

