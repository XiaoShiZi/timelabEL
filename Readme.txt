timelabEL.py is used to create the img, stl and Gcode for an Ultimaker.
pre-requisted are:
python, OpenScad, Cura & a 3D-printer ;-)
The goal was to keep the printing time around 10-12 minutes.
Three names on one timelab label keychain hanger.
One is the name of a visitor, the otherone is the name of the brand/exhibition/event/etc.
The third one is our website.

This was made to be able to produce different keychain's with 3 name-tags.
We opt for a version that runs offline from the internet.
timelab is a fablab who's 3D-printing on several events/locations sometimes with poor internet connection.
That's why we've made this script to ease the production of making a personalized keychain.
As the proof has been with the keychain of Suzanne.
On holliday to Asia she regained here lost keys thanks to one of those personalized keychains.

Changes:
timelabEL.scad
shape of the keychain with rounded ends.
Top Middle & Bottom text added ;-)
added Posi to put higher or lower the text corresponding to the keyholder.
add in the .py possibility to change posi (X & Y!)
Add in scad the posi to the lenght!
added Posi to the output in vartimelabEL.scad by the timelabELgui.py corresponding to the selected textfont.

openscad -o test.png --camera=33,20,-50,55,0,55,330 --imgsize=1024,768 --projection=p timelabEL.scad
