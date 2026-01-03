Todays Learning - Bridging the digital world and the physical world - 01/02/2026 @ 9:22 PM CST

Goal: 

- Use a Arduino UNO R3 board and connect it my MacBook. 
	* The Macbook is acting as the power supply to the UNO board.
- Connect UNO R3 board to a breadboard and a potentiometer 10k dial. 
- Create a "industrial safety" logic to inform the user that the similuate tank is reaching 90% capacity.
	* The void loop should contain logic that prints a message it the telemetry is reaching critical high levels or low feed.
- Understand and review the breadboard 830 Tie-Points.

Learning Notes: 

It is my second time out of college working with breadboards and jumper wires. It was great review and brushing up on the layout of a breadboard and handy reminders about how to bridge your components if they do not fit on a single breadboard column. The need to sometimes "center straddle" the ravine when a component is a "space hog". 

This was also a great in understanding the UNO R3 board such as the GND is short for ground, A0 is Analog in, and the 5v which is the voltage. Plus, making sure that the GND and the 5V power jumpers are not touch in order to prevent any short circuits. 

Details:

1. Connect the UNO board to the breadboard.
	- Get your UNO board and identify the main ports (A0 - analog in, v5 - your power, GND - your ground)
	- Get your breadboard (mine is a 830 Tie-Points)
	- Map out your pins to best place your component (the potentiometer) because you may need to straddle the ravine if 
	  your potentiometer is large. This is to ensure you can connect your jumper pins to the respect connections.
	  
2. Review and keep safety in mind.
	- before plugging in your UNO board in a power source (my case is my MacBook) make sure your GND and your 5V power jumper
	  pin cables are not touching. Even though the is small power and a small UNO board it can still short circuit. Imagine 
	  working with a larger power supply and more costly baords. It could be costly and dangerious. Safety is important.
	  
3. Create your PlatformIO project and get it configured. 
	- Open your tools of choice. I am using a polyglot setup so I have VSCode with PlatformIO extension and the c/c++ 	 	  extension.
	- Once you IDE or tool is ready create your project. Name your project, select Arduino Uno, and the file location of your 	  project.
	- Open you main.cpp file in your project and add your code. Refer to my project for the code details. 
	- Review code, clear any warnings or error highlights before proceeding. 
	
4. Build and Run.
	- Once step 3 is complete you may proceed.
	- At the bottom of the VSCode window there is a arrow icon ->, click on it and wait.
	- If your "build" was successful (connection, reading, and writing) you should see the "SUCCESS" in your terminal.
		* Your UNO board will be showing the LED indicators L, TX, and ON (aka power) are on.
	- Now click on the plug icon. This will open another terminal where your uno board is communcating to you. You should 
	  see in a repeat sequence of either "System Nominal", "ALARM: CRITICAL HIGH LEVEL [!]", or "ALARM: LOW FEED DETECTED   	  [!]". The message is based on the percentage level that is tied to your potentiometer dial. If it is based 90% the 	  	  safety logic will trigger the warning. If is within safe levels it will print "System Nominal".
	  
5. Stop execution.
	- To stop the code executing unplug the usb connecting to the UNO board.
		* WARNING - make sure your GND and 5V jumper cables are not touching. This is to ensure you do not short circuit 
		  your board. So, proceed with caution and at your own risk.
		  
6. Unplug your UNO, breadboard, and clean up your station.
	- As a professional always level your components and work space clean.
	- Unplug your jumper pins from your UNO and breadboard.
	- Organize your components and put them in there respected storage containers. 
	
This completes this session. Screen shots and video recording the session will be added to the repo and linked. 

Trouble shooting:

Most of the trouble shoot was related to the breadboard and the UNO board. I have not worked with a UNO outside of this session and the previous session where I was simple connecting the UNO board to my MacBook. 

I had review how to properly straddle the breadboard ravine in order to provide space for the jumper pins to connect. Plus, I chose to go with a direct connection from breadboard to UNO board. I opted for this because it is small board and not working with other components. Tomorrow I will be adding additional components so my configruation will be different in order to handle the additions. 

Then I need to understand the lingo of the UNO board such as GND = ground, and that on a UNO R3 board there are a total of three GND. Then also understanding the layout of the UNO board in order to map it safely to the breadboard. Again refer to screen shots and records of the breadboard and UNO board. 

Result of learning:

I learned the layout of my UNO board, refreshed my knowledge on the breadboard, wrote cpp logic to simulate a safety measures for a tank getting to full or the feed is to low. Connected my UNO and breadboard correctly and established connection with my MacBook. 

Plus, all though this is a simple project, have knowledge of circuits, how to connect them, and understand safety for yourself and your components when handle any voltage is important. Solid foundations in the basic are important and make understanding advance topics like MQTT and other IoT or IIoT concepts easier.
