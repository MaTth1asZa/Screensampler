
Further attempts to optimize the intial version of my screen sampler.

Harvey's review helped restructure with good code practices and more efficient functions

Main aim is to sample set areas along the edge of my display and average/find the dominant colour of each area before passing this through to a Raspberry Pi.

Currently I am able sample but downstream efficiency might be an issue. Currently need to setup a VMC with Raspberry Pi (or similar) and use a simple WinSock class to send UDP packets to the Pi (Atleast this is what has been recommedned
