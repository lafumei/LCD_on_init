#!/usr/bin/python
# Display the IP Address of the RPI Device
import time
import socket


# import Adafruit_CharLCD as LCD
def little_btn_interface():
	# Make list of button value, text, and backlight color.
	buttons = ( (LCD.SELECT, 'Select', (1,1,1)),
				(LCD.LEFT,   'Left'  , (1,0,0)),
				(LCD.UP,     'Up'    , (0,0,1)),
				(LCD.DOWN,   'Down'  , (0,1,0)),
				(LCD.RIGHT,  'Right' , (1,0,1)) )
 
	print 'Press Ctrl-C to quit.'
	while True:
		# Loop through each button and check if it is pressed.
		for button in buttons:
			if lcd.is_pressed(button[0]):
				# Button is pressed, change the message and backlight.
				lcd.clear()
				lcd.message(button[1])
				lcd.set_color(button[2][0], button[2][1], button[2][2])
	return 
				
def get_ip_address():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(('8.8.8.8', 0))  # connecting to a UDP address doesn't send packets
	local_ip_address = s.getsockname()[0]
	return local_ip_address

def init_sys(ip_addr):
	# Initialize the LCD using the pins
	lcd = LCD.Adafruit_CharLCDPlate()

	# create some custom characters
	lcd.create_char(1, [2, 3, 2, 2, 14, 30, 12, 0])
	lcd.create_char(2, [0, 1, 3, 22, 28, 8, 0, 0])
	lcd.create_char(3, [0, 14, 21, 23, 17, 14, 0, 0])
	lcd.create_char(4, [31, 17, 10, 4, 10, 17, 31, 0])
	lcd.create_char(5, [8, 12, 10, 9, 10, 12, 8, 0])
	lcd.create_char(6, [2, 6, 10, 18, 10, 6, 2, 0])
	lcd.create_char(7, [31, 17, 21, 21, 21, 21, 17, 31])

	# Show some basic colors.
	lcd.message('Initialize LCD...')
	lcd.set_color(1.0, 0.0, 0.0)
	time.sleep(1.0)
	lcd.set_color(0.0, 1.0, 0.0)
	time.sleep(1.0)
	lcd.set_color(0.0, 0.0, 1.0)
	time.sleep(1.0)
	
	lcd.clear()
	lcd.message('IP ADDR: ' + ip_addr)
	return 

def read_temp():
	
def main():
		init_sys(get_ip_address())
		pass
	
	if __name__ == "__main__":
		main()
