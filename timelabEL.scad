//# -*- coding: iso-8859-15 -*-
	//Message Keychain
//http://www.thingiverse.com/thing:52734
//By allenZ
//v2 allow adjustment by user to avoid unconnected parts

//Changed by Xiao Shi Zi/Wim/Lionel Timelab Gent.
//15/02/2014
//V0.01
//Added 3 layers of text
//Top layer		: Name about 4 mm high
//Midden layer	: Brand, about 3mm high
//Bottom layer	: Website, this will be cutout in the keychains bottom

include <Write.scad>
//Text,Font,size added into the Write.scad file to ease the making of a key by a script.
//messageT=Top text
//messageM=Middle text
//messageB=Bottom Text
//messageTF=Top text font (See explenation how to add fonts in http://www.thingiverse.com/thing:16193) 
//messageMF=Middle text font 
//messageBF=Bottom text font
//messageTFS=MessageTopFontize.
//messageMFS=MessageMiddleFontSize
//messageBFS=MessageBottomFontSize
//PosiT=Position of TopText adjustment
//PosiM=Position of MiddleText adjustment
//PosiB=Position of BottomText adjustment.

//messageT=Top text
//messageM=Middle text
//messageB=Bottom Text
//messageTF FontT=Top text font (See explenation how to add fonts in thingiverse:51251) 
//messageMF FontM=Middle text font
//messageBF FontB=Bottom text font
//messageTFS font_sizeT=MessageTopFontize.
//messageMFS font_sizeM=MessageMiddleFontSize
//messageBFS font_sizeB=MessageBottomFontSize
//Posit=Position of TopText adjustment
//Posim=Position of MiddleText adjustment
//Posib=Position of BottomText adjustment.

//messageT
//messageT = "Wim";
//messageT="Lionel";

//messageM= "e o s";
//To be changed to messageM
//possible to add a space inbetween the letters cause the space is layer defined in the dxf-font ;-)
//only (space)&(eos)" eos" are defined in the eos.dxf font!
//messageB="Timelab.org";
//To be changed to MessageB
//echo "message";

include <vartimelabEL.scad>
//messageT="Gçon";
//messageM="ç";
//messageB="timelab.org";
//Posit=-1.5; Y-Ax move
//Posim=-2.1;
//Posib=2.2;
//PositX=3;	X-Ax move
//PosimX=3;
//PosibX=-1.5;
//rotT=3;
//rotM=-4;
//rotB=1;

//echo (messageM);
//echo ("topL=",(font_sizeT*len(messageT)/1.4));
//echo ("MiddelL=",(font_sizeM*len(messageM)/1.4));
//echo ("BottomL=",(font_sizeB*len(messageB)/1.4));
//echo ("max=",max((font_sizeT*len(messageT)/1.4),(font_sizeM*len(messageM)/1.4),(font_sizeB*len(messageB)/1.4)));
TotalLenght=max((font_sizeT*len(messageT)/1.4),(font_sizeM*len(messageM)/1.4),(font_sizeB*len(messageB)/1.4));

//Add the posi to the length!

///echo ("Total",TotalLenght);
//FontT= "letters.dxf";
//include <varTMB.scad>
//To be changed in keyMakerTMB.py				DONE
//To be added Top Middle Bottom text to varTMB.scad		DONE
//To be added Posi Top Middel Bottom	
//To be added Font Top Middle Bottom
//To be added Fontsize Top Middel Bottom
//To be added Footstand Y/N

//Font = "braille.dxf";//["Letters.dxf":Basic,"orbitron.dxf":Futuristic,"braille.dxf":Braille,"BlackRose.dxf":Black]
//FontM="eos.dxf";
//FontB="orbitron.dxf";
//font_sizeT=10;
//font_sizeM=10;
//font_sizeB = 5;

font_thicknessT = 5;
font_thicknessM = 4;
font_thicknessB = 0.5;

stick_thickness = 3;
stick_width = 8.8;

hole_radius = 2.5;
Lengte = 1;

flat_bottom = 1; //[1:Yes,2:No]

union () {

if (flat_bottom == 1) translate ([0,0,-font_thicknessT/2+stick_thickness/2]) flatstickwithhole();

if (flat_bottom == 2) flatstickwithhole();

}

module flatstickwithhole() {

difference () {

union () {
//Middle 
//translate ([3,-2.1,0])
//text(t = "Text!", $fn = 20, size = 10, font = "ArialMT");
translate ([PosimX,Posim,0])
rotate([0,0,rotM])
color("green")write(messageM,t=font_thicknessM, h=font_sizeM, center = false, font = FontM);
//Top
//translate ([3,Posit,0])
translate ([PositX,Posit,0])
rotate([0,0,rotT])
color("red")write(messageT,t=font_thicknessT, h=font_sizeT, center = false, font = FontT);

translate ([0,0,0]) cube ([TotalLenght, stick_width, stick_thickness],center=false);//font_size*len(message)/1.4

translate ([TotalLenght,stick_width/2,0])cylinder (r=stick_width/2,h=stick_thickness,center=false,$fn=50);//font_size*len(message)/1.3+2

translate ([0,stick_width/2,0])cylinder (r=stick_width/2,h=stick_thickness,center=false,$fn=50);
}

translate ([0,stick_width/2,-1])cylinder (r=hole_radius,h=stick_thickness+2,center=false,$fn=50);

//Add timelab.org at bottom 
mirror([1,0,0]) translate ([-TotalLenght-1.5,2.2,-0.1]) rotate([0,0,rotB])
write(messageB,t=font_thicknessB, h=font_sizeB, center = false, font = FontB);
}}
