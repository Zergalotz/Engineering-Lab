Todays Learning - Bridging the digital world and the physical world - 01/01/2026 @ 3:55 PM CST

Goal: 

- Use a Arduino UNO R3 board and connect it my MacBook. 

Learning Notes: 

I have been wanting to learn about how software engineering (the digital world) connects to the infrastructure (the physical world).
How they combine together to make our world operate on a daily bases. Now a UNO R3 board is just one small piece but I wanted to start small and learn about this integrations. 

Today I connected the gap between the physical and the digital. I deployed a C++ firmware to an Arduino Uno that monitors voltage states and reports them via Serial communication. For me understanding the 'Why' behind the baud rates and hardware handshakes is the first step in my transition into IIoT, IoT, and Systems Integration. 

Details:

I captured a screen shot of my VSCode and the extension PlatformIO, I created the project where I am working with the UNO R3 board and my Mac. The screen shot show the main.cpp file where I write the serial communciations for the connection Serial.begin(9600) and the two signals of High (5V) and Low (0V). 

Steps to setup your UNO R3 board and creating the handshake
1. If using VSCode, you will need two main extension
	- PlatformIO
	- C++/C extension pack
	
	PlatformIO and C/C++ extension may seem overboard for just talking with the UNO board. But they are needed for the 	translation layer. Info - my Mac speaks Apple Silicon, while the Uno speaks AVR. i.e. two people speaking to different 
	languages from two different parts of the world.
	
	PlatformIO - is like the factory & logistics, c++ is the dictionary for the files, while platformio is the shipping port 	and factory. The compiler takes the human-readable c++ and translates it into a hex file (basically a string binary file)
	which is how the UNO's brain can understand. Then library manager pulls in the arduino.h files you see at the top of the 
	code file. Without platformio, the computer wouldn't know what the digitalWrite or Serial.begin() means. Finally, the
	uploader (avrdude), which is one of the critical parts, it knows how to shove the 1s and 0s through the USB cable and
	"burns" them into the UNO's memory chip.

2. Open PlatformIO extension and create a project. Name you project, the type of board your using, UNO, arduino. Then select the 
location of you want the project to be stored. 

3. When you have the project one there will be provide code. If you don't want that provided code then you will need to add your
own code in the main.cpp file. 

4. Once you project is created and your code is added into the main.cpp file. Plug, in your UNO board into your pc (mine is macbook)
via usb (note: since I have a mac I have a usb to type c adapter).

5. At the bottom of the VSCode window you will see a arrow ->, click on it. Then wait for your mainl.cpp file to run and setup the details for your UNO board (Connection, Reading, and Writing) to the memory of your board's chip memory. If your board and project are set up correctly you will see in the termainl "SUCCESS" (refer to screen shot). Additionally, if you click on the "plug" icon at the bottom of your VSCode window, you will see another window how and now your UNO board is trying to communication and you'll see the serial communcation print repeatedly "SIGNAL: HIGH (5V)", "SIGNAL: Low (0V)". This is the void loop running in our main.cpp file.

Trouble shooting:

When I went to plug the board back in the following day. In the terminal of my VSCode after clicking the -> button again, it failed. It provided me a message via the avrdude: programmer is not responding, attempt 1 of 10: not in sync. It repeated this until the 10th attempt and then failed.  

So, I begain to trouble shoot by checking the main.cpp file to see if I added any additional code and forgot to close a statement. Everything in the file checked out with no errors or highlights. Then I begain searching for any hardware issues by checking the PWM led for power, it was on, then checking the L led it was also on but the TX led was not on. So, as any professional working with software or hardware, I just restarted the process. I unplugged the USB and plugged it in and it resolved the issue. 

Result of learning:

What I learned is that when you get the "programmer is not responding", it means he VSCode sent the message to the USB port, and it was not recieved. So, this could mean the port is locked out by another process, it could be the computer doesn't realize the UNO board is there, or possibly the cable isn't seated/connected properly. That is common with usb to c adapters.

The software/ digital world when you run apps, api request could be sent and it gets back a 404. The handshake wasn't meet and it very well could be another issue outside of your code. The endpoint might have changed on the database side or maybe there is no connection due to no internet. In the physical world it would be LED indicator isn't on or the translation from app/tool to hardware is not occuring. There are many ways to verify and identify where the issue lies which could be either the software or the hardware side. Understanding where to start finding the issue is very important if the IoT and IIoT world, especially when working with critical infrastructure. This UNO is but a small part, but imagine working with pressure valves, oilers, automation lines and power systems this is critical to understand.