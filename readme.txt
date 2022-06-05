Project Description:
Attempting to create a script that will continually sample the average/dominant (to be be decided) colour along the edges of my screen through screen capture.
Once complete, the idea is that I can then push this data to a raspberry pie, connected to four (4) seperate LED strips. A future script will match the certain areas of the screen to certain sections of LEDs and then display the respective average/dominant colour. These LED strips can be attached to the edge of my screen for a fantastic ambient colour experience.

Current State:

Further attempts to optimize the intial version of my screen sampler.

Harvey's review helped restructure with good code practices and more efficient functions

Main aim is to sample set areas along the edge of my display and average/find the dominant colour of each area before passing this through to a Raspberry Pi.

Currently I am able sample but downstream efficiency might be an issue. Currently need to setup a VMC with Raspberry Pi (or similar) and use a simple WinSock class to send UDP packets to the Pi (Atleast this is what has been recommedned
