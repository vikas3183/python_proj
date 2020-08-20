import os
import pyttsx3
import datetime

# Start the loop
while True:

    # Get the curent date to determine the greeting
	dt=datetime.datetime.now()
	currentTime = dt.hour
	#print(currentTime)

	# Set greeting based on the time of the day
	if (currentTime >= 5 and currentTime < 12) :
		print("Good Morning! How can I help you?  ",end="")
		#pyttsx3.speak("Good Morning! How can I help you?")

	elif (currentTime >= 12 and currentTime < 18) :
		print("Good Afternoon! How can I help you?  ",end="")
		#pyttsx3.speak("Good Afternoon! How can I help you?")

	elif ((currentTime >= 18 and currentTime <=24) or (currentTime >= 0 and currentTime < 5)) :
		print("Good Evening! How can I help you?  ",end="")
		#pyttsx3.speak("Good Evening! How can I help you?")

	else:
	    print ("Hello ! How can I help you?  ",end="")
		#pyttsx3.speak("Hello ! How can I help you?")

	input_string=input()

	# convert input into lower case to ensure checks are consitent
	ip=input_string.lower()

    # Check for chrome
	if (((("run" in ip)  or ("open" in ip) or ("launch" in ip)) and ("chrome" in ip)) or ("chrome" in ip)):
		os.system("chrome")
	
	# Check for gmail		
	elif (((("run" in ip)  or ("open" in ip) or ("launch" in ip)) and ("gmail" in ip)) or ("gmail" in ip)):
		os.system("chrome gmail.com")
	
	# Check for google		
	elif (((("run" in ip)  or ("open" in ip) or ("launch" in ip)) and ("google" in ip)) or ("google" in ip)) :
		os.system("chrome google.com")		

    # Check for notepad
	if (((("run" in ip)  or ("open" in ip) or ("launch" in ip)) and (("notepad" in ip)  or ("editor" in ip) or ("textpad" in ip))) or (("notepad" in ip)  or ("editor" in ip) or ("textpad" in ip))):
		os.system("notepad")
	
	# Check for msword		
	elif (((("run" in ip)  or ("open" in ip) or ("launch" in ip)) and ("word" in ip)) or ("word" in ip)):
		os.system("winword")
	
	# Check for msexcel		
	elif (((("run" in ip)  or ("open" in ip) or ("launch" in ip)) and ("excel" in ip)) or ("excel" in ip)) :
		os.system("excel")

	# exit program
	elif (("end" in ip) or ("exit" in ip) or ("quit" in ip) or ("nothing" in ip) or ("thanks" in ip) or ("thank" in ip)):		
		print("Thank you !!!")
		break

    # Invalid input provided by user
	else:
		print("Apologies - Unable to support")