#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import wx, sys, getopt, os
import thread
#from time import sleep

#timelabEL
#timelabEL=timelab labEL with three nametags on a keychain.
#Text input for each layer by script.
#TO be added onmouse over explanation text of input values.
#To be added 3 checkboxes to produce the png stl and gcode. 
# If Gcode is selected then stl is to be made also.
# If version OpenScad < 2013.06 then no img file.
# Check if png file exists before displaying it on the canvas.
# If not wait a sec.
# Based on thingiverse write & keychain.
# thingiverse
# http://www.thingiverse.com/thing:16193
# http://www.thingiverse.com/thing:52734
# 
# As it's based on the write.scad only 128 characters are possible.
# Not possible yet to use ç à ñ Ñ etc.
# added the openscad possibility to export an image & STL.
# added the command line cura to export the gcode.
# parameters for Cura ar in the timelabEL.ini
 
fontvar = 'Font = "orbitron.dxf";\n'
fontsize='1'
title='timelabEL- Label Key maker V0.01 by Timelab: 小狮子 & Wim ;-)'
# 小狮子 Xiao Shi Zi

class timelabELPanel(wx.Panel):
  def __init__(self, parent,pos=(350,150),size=(850,655)):
    #self.CreateStatusckr(style=0) # A StatusBar in the bottom of the window
    wx.Panel.__init__(self, parent)
    self.count = 0
#  global editnameTPX

# A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
    self.logger = wx.TextCtrl(self, pos=(40,280), size=(360,222), style=wx.TE_MULTILINE | wx.TE_READONLY)

#CheckBox
    self.cbPNG = wx.CheckBox(self, -1, 'Show Img (Only supported from OpenScad Version 2013.06)', (450, 210))
    self.cbSTL = wx.CheckBox(self, -1, 'Create STL', (450,230))
    self.cbGcode = wx.CheckBox(self,-1, 'Create Gcode', (450,250))
    self.cbPNG.SetValue(True)#False
    self.cbSTL.SetValue(True)#False
    self.cbGcode.SetValue(True)#False

# A button
#        self.button =wx.Button(self, label="Maak sleutelhanger", pos=(260, 210))
    imageFile="LogoBut1.png"
    image=wx.Image(imageFile,wx.BITMAP_TYPE_ANY).ConvertToBitmap()
    self.button =wx.BitmapButton(self,bitmap=image, pos=(260, 210))
    self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
  
#Afsluiten
    wx.Button(self, 10, 'Close', (20, 220))
    self.Bind(wx.EVT_BUTTON, self.OnClose, id=10)

#    font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
    font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
    font1 = wx.Font(10, wx.NORMAL, wx.ITALIC, wx.NORMAL)
    font2 = wx.Font(10, wx.ROMAN, wx.NORMAL, wx.NORMAL)
    font3 = wx.Font(12, wx.MODERN, wx.NORMAL, wx.BOLD)

        # the edit control - one line version. 
  #Top
    self.lblnameT = wx.StaticText(self, label="Name :", pos=(15,25))
    self.lblnameT.SetFont(font3)
    self.editnameT = wx.TextCtrl(self, pos=(90, 20), size=(160,-1))
#    self.lblnameT = wx.StaticText(self, label="Uw naam :", pos=(20,25))
#    self.lblnameT = wx.StaticText(self, label="Uw naam :", pos=(21,25))
#    self.lblnameT = wx.StaticText(self, label="Uw naam :", pos=(20,24))
#    self.lblnameT = wx.StaticText(self, label="Uw naam :", pos=(21,24))
#    self.editnameT = wx.TextCtrl(self, pos=(90, 20), size=(160,-1))
        # Checklist Font controlled by the amount of dxf files if possible
  #Top
    self.sampleListT = ['','orbitron', 'letters', 'knewave', 'braille', 'blackrose']
    self.lblhearT = wx.StaticText(self, label="Font:", pos=(15, 55))
    self.lblhearT.SetFont(font3)
    self.edithearT = wx.ComboBox(self, pos=(90, 50), size=(105, -1), choices=self.sampleListT, style=wx.CB_DROPDOWN)
    self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxT, self.edithearT)
#    self.lblhearT = wx.StaticText(self, label="Font:", pos=(20, 55))
#    self.lblhearT = wx.StaticText(self, label="Font:", pos=(21, 55))
#    self.lblhearT = wx.StaticText(self, label="Font:", pos=(20, 54))
#    self.lblhearT = wx.StaticText(self, label="Font:", pos=(21, 54))
#    self.edithearT = wx.ComboBox(self, pos=(90, 50), size=(105, -1), choices=self.sampleListT, style=wx.CB_DROPDOWN)
#    self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxT, self.edithearT)
#Top position X
    self.lblnameTPX = wx.StaticText(self, label="Horizontal :", pos=(360,25))
    self.lblnameTPX.SetFont(font3)
    self.editnameTPX = wx.SpinCtrl(self, -1, '30', min=-666, max=666, size=(56, -1),pos=(480,20)) #To be changed by choices of font and user...
    self.lblnameTPx=wx.StaticText(self,label="*0.1mm",pos=(540,25))
#    self.lblnameTPX = wx.StaticText(self, label="Links of rechts :", pos=(360,25))
#    self.lblnameTPX = wx.StaticText(self, label="Links of rechts :", pos=(361,25))
#    self.lblnameTPX = wx.StaticText(self, label="Links of rechts :", pos=(360,24))
#    self.lblnameTPX = wx.StaticText(self, label="Links of rechts :", pos=(361,24))
#    self.editnameTPX = wx.SpinCtrl(self, -1, '30', min=-666, max=666, size=(56, -1),pos=(480,20)) #To be changed by choices of font and user...
 #   self.lblnameTPx=wx.StaticText(self,label="*0.1mm",pos=(540,25))
#Top position rotation
    self.lblnameTR = wx.StaticText(self, label="Rotation :", pos=(580,40))
    self.lblnameTR.SetFont(font3)
    self.editnameTR = wx.SpinCtrl(self, -1, '66', min=-66, max=66, size=(56, -1),pos=(680,35)) #To be changed by choices of font and user...
    self.lblnameTR=wx.StaticText(self,label="*0.1°",pos=(750,40))
#    self.lblnameTR = wx.StaticText(self, label="Draai :", pos=(600,40))
#    self.lblnameTR = wx.StaticText(self, label="Draai :", pos=(601,40))
#    self.lblnameTR = wx.StaticText(self, label="Draai :", pos=(600,39))
#    self.lblnameTR = wx.StaticText(self, label="Draai :", pos=(601,39))
#    self.editnameTR = wx.SpinCtrl(self, -1, '66', min=-66, max=66, size=(56, -1),pos=(680,40)) #To be changed by choices of font and user...
#    self.lblnameTR=wx.StaticText(self,label="*0.1°",pos=(750,40))
#fontSize
    self.sampleListTF = ['','5','6', '8', '10', '12', '14']
    self.lblhearTF = wx.StaticText(self, label="Size:", pos=(200, 55))
    self.lblhearTF.SetFont(font3)
    self.edithearTF = wx.ComboBox(self, pos=(250, 50), size=(105, -1), choices=self.sampleListTF, style=wx.CB_DROPDOWN)
    self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxTF, self.edithearTF)
#    self.sampleListTF = ['','5','6', '8', '10', '12', '14']
#    self.lblhearTF = wx.StaticText(self, label="Size:", pos=(215, 55))
#    self.lblhearTF = wx.StaticText(self, label="Size:", pos=(216, 55))
#    self.lblhearTF = wx.StaticText(self, label="Size:", pos=(215, 54))
#    self.lblhearTF = wx.StaticText(self, label="Size:", pos=(216, 54))
#    self.edithearTF = wx.ComboBox(self, pos=(250, 50), size=(105, -1), choices=self.sampleListTF, style=wx.CB_DROPDOWN)
#    self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxTF, self.edithearTF)
#Top position Y
    self.lblnameTPY = wx.StaticText(self, label="Vertical :", pos=(360,55))
    self.lblnameTPY.SetFont(font3)
    self.editnameTPY = wx.SpinCtrl(self, -1, '-15', min=-666, max=666, size=(56, -1),pos=(480,50))#To be changed by choices of font and user...
    self.lblnameTPy=wx.StaticText(self,label="*0.1mm",pos=(540,55))
#    self.lblnameTPY = wx.StaticText(self, label="Boven of onder :", pos=(360,55))
#    self.lblnameTPY = wx.StaticText(self, label="Boven of onder :", pos=(361,55))
#    self.lblnameTPY = wx.StaticText(self, label="Boven of onder :", pos=(360,54))
#    self.lblnameTPY = wx.StaticText(self, label="Boven of onder :", pos=(361,54))
#    self.editnameTPY = wx.SpinCtrl(self, -1, '-15', min=-666, max=666, size=(56, -1),pos=(480,50))#To be changed by choices of font and user...
#    self.lblnameTPy=wx.StaticText(self,label="*0.1mm",pos=(540,55))

  #Middle
    self.lblnameM = wx.StaticText(self, label="Brand :", pos=(15,85))
    self.lblnameM.SetFont(font3)
    self.editnameM = wx.TextCtrl(self, pos=(90, 80), size=(160,-1))
#    self.lblnameM = wx.StaticText(self, label="Uw merk :", pos=(20,85))
#    self.lblnameM = wx.StaticText(self, label="Uw merk :", pos=(21,85))
#    self.lblnameM = wx.StaticText(self, label="Uw merk :", pos=(20,84))
#    self.lblnameM = wx.StaticText(self, label="Uw merk :", pos=(21,84))
#    self.editnameM = wx.TextCtrl(self, pos=(90, 80), size=(160,-1))
  #Middle
    self.sampleListM = ['','orbitron', 'letters', 'knewave', 'braille', 'blackrose', 'eos']
    self.lblhearM = wx.StaticText(self, label="Font:", pos=(15, 115))
    self.lblhearM.SetFont(font3)
    self.edithearM = wx.ComboBox(self, pos=(90, 110), size=(105, -1), choices=self.sampleListM, style=wx.CB_DROPDOWN)
    self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxM, self.edithearM)
#    self.sampleListM = ['','orbitron', 'letters', 'knewave', 'braille', 'blackrose', 'eos']
#    self.lblhearM = wx.StaticText(self, label="Font:", pos=(20, 115))
#    self.lblhearM = wx.StaticText(self, label="Font:", pos=(21, 115))
#    self.lblhearM = wx.StaticText(self, label="Font:", pos=(20, 114))
#    self.lblhearM = wx.StaticText(self, label="Font:", pos=(21, 114))
#    self.edithearM = wx.ComboBox(self, pos=(90, 110), size=(105, -1), choices=self.sampleListM, style=wx.CB_DROPDOWN)
#    self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxM, self.edithearM)
#Middle position X
    self.lblnameMPX = wx.StaticText(self, label="Horizontal :", pos=(360,85))
    self.lblnameMPX.SetFont(font3)
    self.editnameMPX = wx.SpinCtrl(self, -1, '30', min=-666, max=666, size=(56, -1),pos=(480,80))
#To be changed by choices of font and user...
    self.lblnameMPx=wx.StaticText(self,label="*0.1mm",pos=(540,85))
#    self.lblnameMPX = wx.StaticText(self, label="Links of rechts :", pos=(360,85))
#    self.lblnameMPX = wx.StaticText(self, label="Links of rechts :", pos=(361,85))
#    self.lblnameMPX = wx.StaticText(self, label="Links of rechts :", pos=(360,84))
#    self.lblnameMPX = wx.StaticText(self, label="Links of rechts :", pos=(361,84))
#    self.editnameMPX = wx.SpinCtrl(self, -1, '30', min=-666, max=666, size=(56, -1),pos=(480,80))#To be changed by choices of font and user...
#    self.lblnameMPx=wx.StaticText(self,label="*0.1mm",pos=(540,85))
#Middle position rotation
    self.lblnameMR = wx.StaticText(self, label="Rotation :", pos=(580,100))
    self.lblnameMR.SetFont(font3)
    self.editnameMR = wx.SpinCtrl(self, -1, '-66', min=-66, max=66, size=(56, -1),pos=(680,95)) #To be changed by choices of font and user...
    self.lblnameMR=wx.StaticText(self,label="*0.1°",pos=(750,100))
#    self.lblnameMR = wx.StaticText(self, label="Draai :", pos=(600,100))
#    self.lblnameMR = wx.StaticText(self, label="Draai :", pos=(601,100))
#    self.lblnameMR = wx.StaticText(self, label="Draai :", pos=(600,99))
#    self.lblnameMR = wx.StaticText(self, label="Draai :", pos=(601,99))
#    self.editnameMR = wx.SpinCtrl(self, -1, '-66', min=-66, max=66, size=(56, -1),pos=(680,90)) #To be changed by choices of font and user...
#    self.lblnameMR=wx.StaticText(self,label="*0.1°",pos=(750,90))
#fontSize
    self.sampleListMF = ['','6', '8', '10', '12', '14']
    self.lblhearMF = wx.StaticText(self, label="Size:", pos=(200, 115))
    self.lblhearMF.SetFont(font3)
    self.edithearMF = wx.ComboBox(self, pos=(250, 110), size=(105, -1), choices=self.sampleListMF, style=wx.CB_DROPDOWN)
    self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxMF, self.edithearMF)
#    self.sampleListMF = ['','6', '8', '10', '12', '14']
#    self.lblhearMF = wx.StaticText(self, label="Size:", pos=(215, 115))
#    self.lblhearMF = wx.StaticText(self, label="Size:", pos=(216, 115))
#    self.lblhearMF = wx.StaticText(self, label="Size:", pos=(215, 114))
#    self.lblhearMF = wx.StaticText(self, label="Size:", pos=(216, 114))
#    self.edithearMF = wx.ComboBox(self, pos=(250, 110), size=(105, -1), choices=self.sampleListMF, style=wx.CB_DROPDOWN)
#    self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxMF, self.edithearMF)
#Middle position Y
    self.lblnameMPY = wx.StaticText(self, label="Vertical :", pos=(360,115))
    self.lblnameMPY.SetFont(font3)
    self.editnameMPY = wx.SpinCtrl(self, -1, '0', min=-666, max=666, size=(56, -1),pos=(480,110))#To be changed by choices of font and user...
    self.lblnameMPy=wx.StaticText(self,label="*0.1mm",pos=(540,115))
#    self.lblnameMPY = wx.StaticText(self, label="Boven of onder :", pos=(360,115))
#    self.lblnameMPY = wx.StaticText(self, label="Boven of onder :", pos=(361,115))
#    self.lblnameMPY = wx.StaticText(self, label="Boven of onder :", pos=(360,114))
#    self.lblnameMPY = wx.StaticText(self, label="Boven of onder :", pos=(361,114))
#    self.editnameMPY = wx.SpinCtrl(self, -1, '0', min=-666, max=666, size=(56, -1),pos=(480,110))#To be changed by choices of font and user...
#    self.lblnameMPy=wx.StaticText(self,label="*0.1mm",pos=(540,115))

  #Bottom
    self.lblnameB = wx.StaticText(self, label="Site :", pos=(15,145))
    self.lblnameB.SetFont(font3)
    self.editnameB = wx.TextCtrl(self, value="timelab.org", pos=(90, 140), size=(160,-1))
#    self.lblnameB = wx.StaticText(self, label="Uw site :", pos=(20,145))
#    self.lblnameB = wx.StaticText(self, label="Uw site :", pos=(21,145))
#    self.lblnameB = wx.StaticText(self, label="Uw site :", pos=(20,144))
#    self.lblnameB = wx.StaticText(self, label="Uw site :", pos=(21,144))
#    self.editnameB = wx.TextCtrl(self, value="timelab.org", pos=(90, 140), size=(160,-1))
  #Bottom
    self.sampleListB = ['','orbitron', 'letters', 'knewave', 'braille', 'blackrose']
    self.lblhearB = wx.StaticText(self, label="Font:", pos=(15, 175))
    self.lblhearB.SetFont(font3)
    self.edithearB = wx.ComboBox(self, pos=(90, 170), size=(105, -1), choices=self.sampleListB, style=wx.CB_DROPDOWN)
    self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxB, self.edithearB)
#    self.sampleListB = ['','orbitron', 'letters', 'knewave', 'braille', 'blackrose']
#    self.lblhearB = wx.StaticText(self, label="Font:", pos=(20, 175))
#    self.lblhearB = wx.StaticText(self, label="Font:", pos=(21, 175))
#    self.lblhearB = wx.StaticText(self, label="Font:", pos=(20, 174))
#    self.lblhearB = wx.StaticText(self, label="Font:", pos=(21, 174))
#    self.edithearB = wx.ComboBox(self, pos=(90, 170), size=(105, -1), choices=self.sampleListB, style=wx.CB_DROPDOWN)
#    self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxB, self.edithearB)
#Bottom position X
    self.lblnameBPX = wx.StaticText(self, label="Horizontal :", pos=(360,145))
    self.lblnameBPX.SetFont(font3)
    self.editnameBPX = wx.SpinCtrl(self, -1, '15', min=-666, max=666, size=(56, -1),pos=(480,140))#To be changed by choices of font and user...
    self.lblnameBPx=wx.StaticText(self,label="*0.1mm",pos=(540,145))
#    self.lblnameBPX = wx.StaticText(self, label="Links of rechts :", pos=(360,145))
#    self.lblnameBPX = wx.StaticText(self, label="Links of rechts :", pos=(361,145))
#    self.lblnameBPX = wx.StaticText(self, label="Links of rechts :", pos=(360,144))
#    self.lblnameBPX = wx.StaticText(self, label="Links of rechts :", pos=(361,144))
#    self.editnameBPX = wx.SpinCtrl(self, -1, '15', min=-666, max=666, size=(56, -1),pos=(480,140))#To be changed by choices of font and user...
#    self.lblnameBPx=wx.StaticText(self,label="*0.1mm",pos=(540,145))
#Bottom position rotation
    self.lblnameBR = wx.StaticText(self, label="Rotation :", pos=(580,160))
    self.lblnameBR.SetFont(font3)
    self.editnameBR = wx.SpinCtrl(self, -1, '0', min=-66, max=66, size=(56, -1),pos=(680,155)) #To be changed by choices of font and user...
    self.lblnameBR=wx.StaticText(self,label="*0.1°",pos=(750,160))

#    self.lblnameBR = wx.StaticText(self, label="Draai :", pos=(600,160))
#    self.lblnameBR = wx.StaticText(self, label="Draai :", pos=(601,160))
#    self.lblnameBR = wx.StaticText(self, label="Draai :", pos=(600,159))
#    self.lblnameBR = wx.StaticText(self, label="Draai :", pos=(601,159))
#    self.editnameBR = wx.SpinCtrl(self, -1, '0', min=-66, max=66, size=(56, -1),pos=(680,150)) #To be changed by choices of font and user...
#    self.lblnameBR=wx.StaticText(self,label="*0.1°",pos=(750,150))
#fontSize
    self.sampleListBF = ['','5','6', '8', '10', '12', '14']
    self.lblhearBF = wx.StaticText(self, label="Size:", pos=(200, 175))
    self.lblhearBF.SetFont(font3)
    self.edithearBF = wx.ComboBox(self, pos=(250, 170), size=(105, -1), choices=self.sampleListBF, style=wx.CB_DROPDOWN)
    self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxBF, self.edithearBF)
#    self.sampleListBF = ['','5','6', '8', '10', '12', '14']
#    self.lblhearBF = wx.StaticText(self, label="Size:", pos=(215, 175))
#    self.lblhearBF = wx.StaticText(self, label="Size:", pos=(216, 175))
#    self.lblhearBF = wx.StaticText(self, label="Size:", pos=(215, 174))
#    self.lblhearBF = wx.StaticText(self, label="Size:", pos=(216, 174))
#    self.edithearBF = wx.ComboBox(self, pos=(250, 170), size=(105, -1), choices=self.sampleListBF, style=wx.CB_DROPDOWN)
#    self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxBF, self.edithearBF)
#Bottom position Y
    self.lblnameBPY = wx.StaticText(self, label="Vertical :", pos=(360,175))
    self.lblnameBPY.SetFont(font3)
    self.editnameBPY = wx.SpinCtrl(self, -1, '22', min=-666, max=666, size=(56, -1),pos=(480,170))#To be changed by choices of font and user...
    self.lblnameBPy=wx.StaticText(self,label="*0.1mm",pos=(540,175))
#    self.lblnameBPY = wx.StaticText(self, label="Boven of onder :", pos=(360,175))
#    self.lblnameBPY = wx.StaticText(self, label="Boven of onder :", pos=(361,175))
#    self.lblnameBPY = wx.StaticText(self, label="Boven of onder :", pos=(360,174))
#    self.lblnameBPY = wx.StaticText(self, label="Boven of onder :", pos=(361,174))
#    self.editnameBPY = wx.SpinCtrl(self, -1, '22', min=-666, max=666, size=(56, -1),pos=(480,170))#To be changed by choices of font and user...
#    self.lblnameBPy=wx.StaticText(self,label="*0.1mm",pos=(540,175))
      
  # Img
#  img = wx.EmptyImage(340,340)
#        self.imageCtrl = wx.StaticBitmap(self, wx.ID_ANY, wx.BitmapFromImage(img))
#  img=('/home/Documenten/Bakfiets/Print/Keychain5.00/eosT.png')
#  self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
#  self.refresh()
    self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
    self.frame = parent
    self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

  #create a gauge
    self.g2 = wx.Gauge(self, -1, 80, (110, 510), (550, 25))
    self.Bind(wx.EVT_TIMER, self.TimerHandler)
    self.timer = wx.Timer(self)
    self.timer.Start(100)
    self.g2.Hide()

#     def OnClose(self, event):
#         self.Close()


  def ShowTitle(self, event):
    if self.cb.GetValue():
      self.SetTitle('checkbox.py')
      self.logger.AppendText('Selected Img: \n' )
#      self.cb1.SetValue(False)
    else: self.SetTitle('')


  def __del__(self):
    self.timer.Stop()

  def OnClose(self, event):
    self.logger.AppendText('Thx for using timelabEL.\n')
    print('Thx for using timelabEL.')
    self.timer.Stop()
    self.Destroy()
    frame.Destroy()
#    self.Close()

  def TimerHandler(self, event):
    self.count = self.count + 1
    if self.count >= 50:
      self.count = 0
      # self.g1.SetValue(self.count)

    self.g2.Pulse()
#    self.BgChangBmp="0"

  # Font versus Size connection adjusted!
  
  #Cheklist parameters for Cura settings Find/change version to do

  def EvtComboBoxT(self, event):
#Top
    global fontvarTF
    global fontvar1TF
    global fontsizeTF  
    global posit
  #global BgChangBmp=0
#  global BgChangBmp
#  BgChangBmp='0'     
    fontvarTF = 'FontT = "%s.dxf";\n' 
    fontvarTF %= event.GetString()
    fontvar1TF = event.GetString()
    print fontvarTF
    print event.GetString()
    if fontvar1TF=='orbitron':
      fontsizeTF='10'
#    posit='Posit = -1.5;\n'

    if fontvar1TF=='letters':
      fontsizeTF='11'
#    posit='Posit = -1.5;\n'

    if fontvar1TF=='knewave':
      fontsizeTF='10'
#    posit='Posit = -1.5;\n'

    if fontvar1TF=='braille':
      fontsizeTF='13'
#    posit='Posit = -2;\n'

    if fontvar1TF=='blackrose':
      fontsizeTF='15'
#    posit='Posit = -2;\n'

    if fontvar1TF=='eos':
      fontsizeTF='10'
#    posit='Posit = -1.5;\n'
    self.logger.AppendText('Selected font Name: %s\n' % event.GetString())
    self.g2.Hide()

  def EvtComboBoxTF(self, event):
#TopFont
    global fontvarTSF
    global fontvar1TSF
    global fontsizeTSF  
    global posit
  #global BgChangBmp=0
#  global BgChangBmp
#  BgChangBmp='0'     
    fontvarTSF = 'Font Top Size= "%s"\n' 
    fontvarTSF %= event.GetString()
    fontvar1TSF = event.GetString()
    fontsizeTSF=event.GetString()
    print fontvarTSF
    print event.GetString()
    if fontvar1TSF=='5':
      fontsizeTSF='5'
    #posit='Posit = -1.5;\n'

    if fontvar1TSF=='6':
      fontsizeTSF='6'
    #posit='Posit = -1.5;\n'

    if fontvar1TSF=='8':
      fontsizeTSF='8'
    #posit='Posit = -1.5;\n'

    if fontvar1TF=='10':
      fontsizeTSF='10'
    #posit='Posit = -2;\n'

    if fontvar1TSF=='12':
      fontsizeTSF='12'
    #posit='Posit = -2;\n'

    if fontvar1TSF=='14':
      fontsizeTSF='14'
    #posit='Posit = -1.5;\n'

    self.logger.AppendText('Selected font Name Size: %s\n' % event.GetString())
    self.g2.Hide()

  def EvtComboBoxM(self, event):
#Middle
    global fontvarMF
    global fontvar1MF
    global fontsizeMF  
    global posim
  #global BgChangBmp=0
#  global BgChangBmp
#  BgChangBmp='0'     
    fontvarMF = 'FontM = "%s.dxf";\n' 
    fontvarMF %= event.GetString()
    fontvar1MF = event.GetString()
    print fontvarMF
    print event.GetString()
    if fontvar1MF=='orbitron':
      fontsizeMF='10'
#    posim='Posim = -2.1;\n'

    if fontvar1MF=='letters':
      fontsizeMF='11'
#    posim='Posim = -1.5;\n'

    if fontvar1MF=='knewave':
      fontsizeMF='10'
#    posim='Posim = -1.5;\n'

    if fontvar1MF=='braille':
      fontsizeMF='13'
#    posim='Posim = -2;\n'

    if fontvar1MF=='blackrose':
      fontsizeMF='15'
#    posim='Posim = -2;\n'

    if fontvar1MF=='eos':
      fontsizeMF='10'
#    posim='Posim = -1.5;\n'

    self.logger.AppendText('Selected font Brand: %s\n' % event.GetString())
    self.g2.Hide()

  def EvtComboBoxMF(self, event):
#MiddleFont
#self.sampleListBF = ['','5','6', '8', '10', '12', '14']
    global fontvarMSF
    global fontvar1MSF
    global fontsizeMSF  
    global posim
  #global BgChangBmp=0
#  global BgChangBmp
#  BgChangBmp='0'     
    fontvarMSF = 'Font Midden Size = "%s";\n' 
    fontvarMSF %= event.GetString()
    fontvar1MSF = event.GetString()
    print fontvarMSF
    print event.GetString()
    if fontvar1MSF=='5':
      fontsizeMSF='5'
    #posim='Posim = -1.5;\n'

    if fontvar1MSF=='6':
      fontsizeMSF='6'
    #posim='Posim = -1.5;\n'

    if fontvar1MSF=='8':
      fontsizeMSF='8'
    #posim='Posim = -1.5;\n'

    if fontvar1MSF=='10':
      fontsizeMSF='10'
    #posim='Posi = -2;\n'

    if fontvar1MSF=='12':
      fontsizeMSF='12'
    #posim='Posim = -2;\n'

    if fontvar1MSF=='14':
      fontsizeMSF='14'
    #posim='Posim = -1.5;\n'

    self.logger.AppendText('Selected font Brand Size: %s\n' % event.GetString())
    self.g2.Hide()

  def EvtComboBoxB(self, event):
#Bottom
    global fontvarBF
    global fontvar1BF
    global fontsizeBF
    global posib
  #global BgChangBmp=0
#  global BgChangBmp
#  BgChangBmp='0'     
    fontvarBF = 'FontB= "%s.dxf";\n' 
    fontvarBF %= event.GetString()
    fontvar1BF = event.GetString()
    print fontvarBF
    print event.GetString()
    if fontvar1BF=='orbitron':
      fontsizeBF='10'
#    posib='Posib = -1.5;\n'

    if fontvar1BF=='letters':
      fontsizeBF='11'
#    posib='Posib = -1.5;\n'

    if fontvar1BF=='knewave':
      fontsizeBF='10'
#    posib='Posib = -1.5;\n'

    if fontvar1BF=='braille':
      fontsizeBF='13'
#    posib='Posib = -2;\n'

    if fontvar1BF=='blackrose':
      fontsizeBF='15'
#    posib='Posib = -2;\n'

    if fontvar1BF=='eos':
      fontsizeBF='10'
#    posib='Posib = -1.5;\n'

    self.logger.AppendText('Selected font Site: %s\n' % event.GetString())
    self.g2.Hide()

  def EvtComboBoxBF(self, event):
#BottomFont
#self.sampleListBF = ['','5','6', '8', '10', '12', '14']
    global fontvarBSF
    global fontvar1BSF
    global fontsizeBSF  
    global posib
  #global BgChangBmp=0
#  global BgChangBmp
#  BgChangBmp='0'     
    fontvarBSF = 'Font Bottom Size = "%s";\n' 
    fontvarBSF %= event.GetString()
    fontvar1BSF = event.GetString()
    print fontvarBSF
    print event.GetString()
    if fontvar1BSF=='5':
      fontsizeBSF='5'
    #posib='Posib = -1.5;\n'

    if fontvar1BSF=='6':
      fontsizeBSF='6'
    #posib='Posib = -1.5;\n'

    if fontvar1BSF=='8':
      fontsizeBSF='8'
    #posib='Posib = -1.5;\n'

    if fontvar1BSF=='10':
      fontsizeBSF='10'
    #posib='Posib = -2;\n'

    if fontvar1BSF=='12':
      fontsizeBSF='12'
    #posib='Posib = -2;\n'

    if fontvar1BSF=='14':
      fontsizeBSF='14'
    #posib='Posib = -1.5;\n'

    self.logger.AppendText('Selected font Site Size: %s\n' % event.GetString())
    self.g2.Hide()

   
  def OnClick(self,event):
    self.g2.Show()
    thread.start_new_thread(self.longRunning, ())

  def longRunning(self):
    nameT = self.editnameT.GetValue()
    nameM=self.editnameM.GetValue()
    nameB=self.editnameB.GetValue()
    editnameTPX=self.editnameTPX.GetValue()*0.1
    editnameTPY=self.editnameTPY.GetValue()*0.1
    editnameMPX=self.editnameMPX.GetValue()*0.1
    editnameMPY=self.editnameMPY.GetValue()*0.1
    editnameBPX=self.editnameBPX.GetValue()*0.1
    editnameBPY=self.editnameBPY.GetValue()*0.1
    editnameTR=self.editnameTR.GetValue()*0.1
    editnameMR=self.editnameMR.GetValue()*0.1
    editnameBR=self.editnameBR.GetValue()*0.1

#  self.logger.AppendText("\n\n\n\n\n\n\n\n\n\n\n\n")       
    self.logger.AppendText("Making timelabEL Label key for %s\n" %nameT)
  
#  self.logger.AppendText("TPX %s\n" %editnameTPX)
    self.g2.Pulse()
    fo = open("vartimelabEL.scad","w")
    writelineT = 'messageT="%s";\n'
    writelineT %= nameT
    writelineT=writelineT.encode('utf-8')
    fo.write(writelineT)
    fo.close()
    fo = open ("vartimelabEL.scad","a")
    writeline2T=("font_sizeT=%s;\n" %fontsizeTSF)
    fo.write(writeline2T)
    fo.write(fontvarTF)
    positY='Posit= %s;\n'
    positY %=editnameTPY
    fo.write(positY)
#  fo.write(posit)
    positX='PositX= %s;\n'
    positX %=editnameTPX
    fo.write(positX)
    fo.write("rotT= %s;\n" %editnameTR)
    writelineM = 'messageM="%s";\n'
    writelineM %= nameM
    writelineM=writelineM.encode('utf-8')
    fo.write(writelineM)
    writeline2M=("font_sizeM=%s;\n" %fontsizeMSF)
    fo.write(writeline2M)
    fo.write(fontvarMF)
    posimY='Posim= %s;\n'
    posimY %=editnameMPY
    fo.write(posimY)
#  fo.write(posim)
    posimX='PosimX= %s;\n'
    posimX %=editnameMPX
    fo.write(posimX)
    fo.write("rotM= %s;\n" %editnameMR)
    writelineB = 'messageB="%s";\n'
    writelineB %= nameB
    writelineB=writelineB.encode('utf-8')
    fo.write(writelineB)
    writeline2B=("font_sizeB=%s;\n" %fontsizeBSF)
    fo.write(writeline2B)
    fo.write(fontvarBF)
    posibY='Posib= %s;\n'
    posibY %=editnameBPY
    fo.write(posibY)
#  fo.write(posib)
    posibX='PosibX= %s;\n'
    posibX %=editnameBPX
    fo.write(posibX)
    fo.write("rotB= %s;\n" %editnameBR)
    fo.close()
    directory = 'out'
#Check version of OpenSad > 2013.06 
#  wx.EVT_CHECKBOX(self, self.cbPNG.GetId(), self.ShowTitle)
    if self.cbPNG.GetValue():
#    OpenscadV='openscad --version > Openv.txt'
#    os.system(OpenscadV)
#png if OpenScad > 2013.06
      runcommand3 = 'openscad -o %s/TMB%s.png --camera=-35,-5,0,50,0,10,250 --imgsize=824,268 --projection=p timelabEL.scad'
      runcommand3 %= directory,nameT
      runcommand3=runcommand3.encode('utf-8')
      os.system(runcommand3)
      message3 = 'TMB-Key %s.png is ready.'
      message3 %= nameT
      print message3
      self.logger.AppendText('Img Selected.\n' )
    #      self.cb1.SetValue(False)
    else: self.logger.AppendText('No img selected.\n')

#stl
    if self.cbSTL.GetValue():
      runcommand = 'openscad -o %s/TMBkey%s.stl timelabEL.scad'
      runcommand %= directory,nameT
      runcommand=runcommand.encode('utf-8')
      os.system(runcommand)
      message = 'TMB-Key %s.stl is ready to be sliced'
      message %= nameT
      print message
      self.logger.AppendText("TMB-Key %s.stl is ready to be sliced\n" %nameT)  
    else: self.logger.AppendText('No STL selected, No gcode to generate')

#Gcode
    if self.cbGcode.GetValue() and not self.cbSTL.GetValue():
      runcommand2 = 'cura -i timelabEL.ini -s %s/TMBkey%s.stl -o %s/TMBkey%s.gcode  '
      runcommand2 %= directory,nameT,directory,nameT
      runcommand2=runcommand2.encode('utf-8')
      os.system(runcommand2)
      message = 'TMB-Key %s is Sliced and ready to print.\nGreetings Xiao Shi Zi & Wim de Bonte,\nPro members of Timelab Gent Belgium ;-)\nReady to produce the next TMB-Key!\n'
      message %= nameT
      print message
      self.logger.AppendText("TMB-Key %s is Sliced and ready to print.\nUnder directory ./out/TMBkey*.gcode you'll find the .gcode file\nCopy to the SD card and happy printing.\nGreetings Xiao Shi Zi & Wim de Bonte,\nPro members of Timelab Gent Belgium ;-)\nReady to produce the next TMB-Key!\n" %nameT)
    else:
      runcommand = 'openscad -o %s/TMBkey%s.stl TMBKeychainV0.27.scad'
      runcommand %= directory,nameT
      runcommand=runcommand.encode('utf-8')
      os.system(runcommand)
      message = 'TMB-Key %s.stl is ready to be sliced'
      message %= nameT
      print message
      self.logger.AppendText("TMB-Key %s.stl is ready to be sliced\n" %nameT)
      runcommand2 = 'cura -i timelabEL.ini -s %s/TMBkey%s.stl -o %s/TMBkey%s.gcode  '
      runcommand2 %= directory,nameT,directory,nameT
      runcommand2=runcommand2.encode('utf-8')
      os.system(runcommand2)
      message = 'TMB-Key %s is Sliced and ready to print.\nGreetings Xiao Shi Zi & Wim de Bonte,\nPro members of Timelab Gent Belgium ;-)\nReady to produce the next TMB-Key!\n'
      message %= nameT
      print message
      self.logger.AppendText("TMB-Key %s is Sliced and ready to print.\nUnder directory ./out/TMBkey*.gcode you'll find the .gcode file\nCopy to the SD card and happy printing.\nGreetings Xiao Shi Zi & Wim de Bonte,\nPro members of Timelab Gent Belgium ;-)\nReady to produce the next TMB-Key!\n" %nameT)

    if not self.cbGcode.GetValue(): 
      self.logger.AppendText=("No Gcode Generated\n")

    self.g2.Hide()

#Img Y/N
    if self.cbPNG.GetValue():
      imageFile=('out/TMB%s.png' %nameT)
      png = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
      wx.StaticBitmap(self, -1, png, (0, 550), (png.GetWidth(), png.GetHeight()))
    else: self.logger.AppendText('No img selected.\n')


#  self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
#        self.frame = frame
#        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground2)
#  self.bitmap=wx.Bitmap('out/TMB%s.png' %nameT)
#  self.bitmap=wx.Bitmap('TMB%s.png' %nameT)
#  dc = wx.PaintDC(self)
#  dc.DrawBitmap(self.bitmap, 160, 200)
#  self.OnEraseBackground2()

  #runcommand4 = './bitmap.py'
        #runcommand4 
#        os.system(runcommand4)
#  dc = self.GetDC()
#        if not dc:
#            dc = wx.ClientDC(self)
#            rect = self.GetUpdateRegion().GetBox()
#            dc.SetClippingRect(rect)
#        dc.Clear()

#  self.BgChangBmp="1"
#  self.Bind(self.OnEraseBackground)
#bmp=wx.Bitmap("out/eos%s.png" %name)
#        dc.DrawBitmap("out/TMB%s.png", 120, 200 %name)

#  self.onView()


    #----------------------------------------------------------------------
  def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("timelabEL.png")
        dc.DrawBitmap(bmp, 1, 1)

    #----------------------------------------------------------------------
#    def OnEraseBackground2(self,evt):
#        """
#        Add a picture to the background
#        """
#        # yanked from ColourDB.py
#        dc = evt.GetDC()
#
#        if not dc:
#            dc = wx.ClientDC(self)
#            rect = self.GetUpdateRegion().GetBox()
#            self.SetClippingRect(rect)
#        self.Clear()
#        bmp = wx.Bitmap('TMB%s.png' %nameT)
#        self.DrawBitmap(bmp, 1, 1)


#--xample to change bitmap on top of button------------------
#def create(self,event):
#    self.textinput = wx.TextCtrl(self.panel, pos=(100,20))
#    self.picture = wx.Image("pics\\default.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
#    self.picturebutton = wx.BitmapButton(self.panel,-1,self.picture,pos=(100,50))
#    self.textinput.Bind(wx.EVT_TEXT, self.changepic)
#
#def changepic(self,event):
#    if event.String = 'test':
#        self.picture = wx.Image("pics\\new.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
#        self.picturebutton.SetBitmap(self.picture)
#        self.Refresh()
#    event.Skip()
#



#
    #----------------------------------------------------------------------
#    def OnEraseBackground(self, evt):
#        """
#        Add a picture to the background
#        """
#  # yanked from ColourDB.py
#        dc = evt.GetDC()
#  if BgChangBmp =='':
#    BgChangBmp=" "
#  
#
#        if not dc:
#            dc = wx.ClientDC(self)
#            rect = self.GetUpdateRegion().GetBox()
#            dc.SetClippingRect(rect)
#        dc.Clear()

#  message5= BgChangBmp
#  print message5
#  if BgChangBmp == '0':
#    bmp = wx.Bitmap("roses.jpg")
#  else:
#    bmp = wx.Bitmap("eosT.png")

#        dc.DrawBitmap(bmp, 120, 200)

#png
#       def onView(self):
#        filepath = self.photoTxt.GetValue('./eosT.png')
#        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
#        # scale the image, preserving the aspect ratio
#        W = img.GetWidth()
#        H = img.GetHeight()
#        if W > H:
#            NewW = self.PhotoMaxSize
#            NewH = self.PhotoMaxSize * H / W
#        else:
#            NewH = self.PhotoMaxSize
#            NewW = self.PhotoMaxSize * W / H
#        img = img.Scale(NewW,NewH)
# 
#        self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
#        self.panel.Refresh()
#

app = wx.App(False)
frame = wx.Frame(None,title=title,size=(827,755))
panel = timelabELPanel(frame)
frame.Show()
app.MainLoop()
