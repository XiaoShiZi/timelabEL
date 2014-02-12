#!/usr/bin/python
# -*- coding: utf-8 -*-
import wx
import sys
import getopt
import os
import thread
import gettext
from gettext import gettext as _
#gettext.install('3NT','./po',unicode=False)

#one line for each language
#presLan_en = gettext.translation("3NT", os.path.join(get_bundle_path(),'./po'), languages=['en'])
#presLan_nl = gettext.translation("3NT",'./po'), languages=['nl'])
 
#only install one language - add program logic later
#presLan_en.install()
#presLan_nl.install()

#iso-8859-15

# 3NT.py
# 3 Name Tag keychain creator.
# 02/02/2014
# This is to create an image, STL and the Gcode for an ULtimaker.
# by use of OpenScad, Cura and this Python script.
# made by 小狮子 & Wim, Pro members of timelab Gent.
# website : timelab.org
# Original concept was using only one name. as found on
# Thingiverse.
# Write is used in the OpenScad with the limmitation of only using 128 characters.
# So still no names with ñ or ç à etc. are possible :(
# Enjoy

class M3NT(wx.Frame):
    def __init__(self, parent, id, title):
      wx.Frame.__init__(self, parent, id, title, size=(1200,655), pos=(125,150))

      panel = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
#      self.cb = wx.CheckBox(panel, -1, 'Show Title', (10, 10))
#      self.cb1 = wx.CheckBox(panel, -1, 'Hide Title', (10, 30))
#      self.cb.SetValue(True)
#      self.cb1.SetValue(False)

      font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
      font1 = wx.Font(10, wx.NORMAL, wx.ITALIC, wx.NORMAL)
      font2 = wx.Font(10, wx.ROMAN, wx.NORMAL, wx.NORMAL)
      font3 = wx.Font(12, wx.MODERN, wx.NORMAL, wx.BOLD)

#Name
        # the edit control - one line version. 
  #Top
      self.lblnameT = wx.StaticText(panel, label=_("Uw naam :"), pos=(20,20))
      self.lblnameT.SetFont(font3)
      self.editnameT = wx.TextCtrl(panel, pos=(20, 45), size=(160,-1))
        # Checklist Font controlled by the amount of dxf files if possible
  #Top
      self.sampleListT = ['','orbitron', 'letters', 'knewave', 'braille', 'blackrose']
      self.lblhearT = wx.StaticText(panel, label=_("Font:"), pos=(190, 20))
      self.lblhearT.SetFont(font3)
      self.edithearT = wx.ComboBox(panel, pos=(190, 45), size=(105, -1), choices=self.sampleListT, style=wx.CB_DROPDOWN)
      self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxT, self.edithearT)
#fontSize
      self.sampleListTF = ['','5','6', '8', '10', '12', '14']
      self.lblhearTF = wx.StaticText(panel, label=_("Size:"), pos=(310, 20))
      self.lblhearTF.SetFont(font3)
      self.edithearTF = wx.ComboBox(panel, pos=(310, 45), size=(105, -1), choices=self.sampleListTF, style=wx.CB_DROPDOWN)
      self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxTF, self.edithearTF)
#Top position X
      self.lblnameTPX = wx.StaticText(panel, label=_("Horizontaal :"), pos=(430,20))
      self.lblnameTPX.SetFont(font3)
      self.editnameTPX = wx.SpinCtrl(panel, -1, '30', min=-666, max=666, size=(56, -1),pos=(430,45)) #To be changed by choices of font and user...
      self.lblnameTPx=wx.StaticText(panel,label="*0.1mm",pos=(490,50))
#Top position Y
      self.lblnameTPY = wx.StaticText(panel, label=_("Vertikaal :"), pos=(610,20))
      self.lblnameTPY.SetFont(font3)
      self.editnameTPY = wx.SpinCtrl(panel, -1, '-15', min=-666, max=666, size=(56, -1),pos=(610,45))#To be changed by choices of font and user...
      self.lblnameTPy=wx.StaticText(panel,label="*0.1mm",pos=(680,50))
#Top position rotation
      self.lblnameTR = wx.StaticText(panel, label=_("Rotatie :"), pos=(780,20))
      self.lblnameTR.SetFont(font3)
      self.editnameTR = wx.SpinCtrl(panel, -1, '66', min=-66, max=66, size=(56, -1),pos=(780,45)) #To be changed by choices of font and user...
      self.lblnameTR=wx.StaticText(panel,label="*0.1°",pos=(850,50))
#Middle
      self.lblnameM = wx.StaticText(panel, label=_("Uw merk :"), pos=(20,85))
      self.lblnameM.SetFont(font3)
      self.editnameM = wx.TextCtrl(panel, pos=(20, 110), size=(160,-1))
        # Checklist Font controlled by the amount of dxf files if possible
  #Middle
      self.sampleListM = ['','orbitron', 'letters', 'knewave', 'braille', 'blackrose', 'eos']
      self.lblhearM = wx.StaticText(panel, label=_("Font:"), pos=(190, 85))
      self.lblhearM.SetFont(font3)
      self.edithearM = wx.ComboBox(panel, pos=(190, 110), size=(105, -1), choices=self.sampleListM, style=wx.CB_DROPDOWN)
      self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxM, self.edithearM)
#fontSize
      self.sampleListMF = ['','6', '8', '10', '12', '14']
      self.lblhearMF = wx.StaticText(panel, label=_("Size:"), pos=(310, 85))
      self.lblhearMF.SetFont(font3)
      self.edithearMF = wx.ComboBox(panel, pos=(310, 110), size=(105, -1), choices=self.sampleListMF, style=wx.CB_DROPDOWN)
      self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxMF, self.edithearMF)
#Middle position X
      self.lblnameMPX = wx.StaticText(panel, label=_("Horizontaal :"), pos=(430,85))
      self.lblnameMPX.SetFont(font3)
      self.editnameMPX = wx.SpinCtrl(panel, -1, '30', min=-666, max=666, size=(56, -1),pos=(430,110))
#To be changed by choices of font and user...
      self.lblnameMPx=wx.StaticText(panel,label="*0.1mm",pos=(490,115))
#Middle position Y
      self.lblnameMPY = wx.StaticText(panel, label=_("Vertikaal :"), pos=(610,85))
      self.lblnameMPY.SetFont(font3)
      self.editnameMPY = wx.SpinCtrl(panel, -1, '0', min=-666, max=666, size=(56, -1),pos=(610,110))#To be changed by choices of font and user...
      self.lblnameMPy=wx.StaticText(panel,label="*0.1mm",pos=(680,115))
#Middle position rotation
      self.lblnameMR = wx.StaticText(panel, label=_("Rotatie :"), pos=(780,85))
      self.lblnameMR.SetFont(font3)
      self.editnameMR = wx.SpinCtrl(panel, -1, '-66', min=-66, max=66, size=(56, -1),pos=(780,110)) #To be changed by choices of font and user...
      self.lblnameMR=wx.StaticText(panel,label="*0.1°",pos=(850,115))
#Bottom
      self.lblnameB = wx.StaticText(panel, label=_("Uw site :"), pos=(20,140))
      self.lblnameB.SetFont(font3)
      self.editnameB = wx.TextCtrl(panel, value="timelab.org", pos=(20, 165), size=(160,-1))
#Bottom
      self.sampleListB = ['','orbitron', 'letters', 'knewave', 'braille', 'blackrose']
      self.lblhearB = wx.StaticText(panel, label=_("Font:"), pos=(190, 140))
      self.lblhearB.SetFont(font3)
      self.edithearB = wx.ComboBox(panel, pos=(190, 165), size=(105, -1), choices=self.sampleListB, style=wx.CB_DROPDOWN)
      self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxB, self.edithearB)
#fontSize
      self.sampleListBF = ['','5','6', '8', '10', '12', '14']
      self.lblhearBF = wx.StaticText(panel, label=_("Size:"), pos=(310, 140))
      self.lblhearBF.SetFont(font3)
      self.edithearBF = wx.ComboBox(panel, pos=(310, 165), size=(105, -1), choices=self.sampleListBF, style=wx.CB_DROPDOWN)
      self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxBF, self.edithearBF)
#Bottom position X
      self.lblnameBPX = wx.StaticText(panel, label=_("Horizontaal :"), pos=(430,140))
      self.lblnameBPX.SetFont(font3)
      self.editnameBPX = wx.SpinCtrl(panel, -1, '15', min=-666, max=666, size=(56, -1),pos=(430,165))#To be changed by choices of font and user...
      self.lblnameBPx=wx.StaticText(panel,label="*0.1mm",pos=(490,170))
#Bottom position Y
      self.lblnameBPY = wx.StaticText(panel, label=_("Vertikaal :"), pos=(610,140))
      self.lblnameBPY.SetFont(font3)
      self.editnameBPY = wx.SpinCtrl(panel, -1, '22', min=-666, max=666, size=(56, -1),pos=(610,165))#To be changed by choices of font and user...
      self.lblnameBPy=wx.StaticText(panel,label="*0.1mm",pos=(680,170))
#Bottom position rotation
      self.lblnameBR = wx.StaticText(panel, label=_("Rotatie :"), pos=(780,140))
      self.lblnameBR.SetFont(font3)
      self.editnameBR = wx.SpinCtrl(panel, -1, '0', min=-66, max=66, size=(56, -1),pos=(780,165)) #To be changed by choices of font and user...
      self.lblnameBR=wx.StaticText(panel,label="*0.1°",pos=(850,170))


# A button
#        self.button =wx.Button(self, label="Maak sleutelhanger", pos=(260, 210))
      imageFile="LogoBut1.png"
      image=wx.Image(imageFile,wx.BITMAP_TYPE_ANY).ConvertToBitmap()
      self.button =wx.BitmapButton(panel,bitmap=image, pos=(260, 210))
#      self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
#
      wx.Button(panel, 10, _('Close'), (20, 220))
      self.Bind(wx.EVT_BUTTON, self.OnClose, id=10)
# A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it      
      self.logger = wx.TextCtrl(panel, pos=(40,290), size=(360,222), style=wx.TE_MULTILINE | wx.TE_READONLY)
      self.count = 0
#CheckBox
      self.cbPNG = wx.CheckBox(panel, -1, _('Show Img (Only supported from OpenScad Version 2013.06)'), (450, 210))
      self.cbSTL = wx.CheckBox(panel, -1, _('Create STL'), (450,230))
      self.cbGcode = wx.CheckBox(panel,-1, _('Create Gcode'), (450,250))
      self.cbPNG.SetValue(False)
      self.cbSTL.SetValue(True)
      self.cbGcode.SetValue(True)

#      wx.EVT_CHECKBOX(self, self.cb.GetId(), self.ShowTitle)
#      wx.EVT_CHECKBOX(self, self.cb1.GetId(), self.HideTitle)
#      wx.EVT_BUTTON(self.OnClick,self.button)
      self.button.Bind(wx.EVT_LEFT_DCLICK, self.OnClick)
#      self.button.Bind(wx.EVT_ONCLICK, self.OnClick)
      wx.EVT_CHECKBOX(self, self.cbPNG.GetId(), self.ShowImage)

      self.Show()
      self.Centre()
      
# Img
#      self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
#      self.frame = panel
#      self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

#create a gauge
      self.g2 = wx.Gauge(self, -1, 80, (110, 510), (550, 25))
      self.Bind(wx.EVT_TIMER, self.TimerHandler)
      self.timer = wx.Timer(self)
      self.timer.Start(100)
      self.g2.Hide()

#    def ShowTitle(self, event):
#        if self.cb.GetValue():
#            self.SetTitle('checkbox.py')
#	    self.cb1.SetValue(False)
#	    self.logger.AppendText('ShowTitle selected.\n' )
#        else:
#          self.SetTitle('')
#	  self.logger.AppendText('ShowTitle deselected.\n' )

    def __del__(self):
      self.timer.Stop()

    def OnClose(self, event):
      self.Close()

    def TimerHandler(self, event):
      self.count = self.count + 1
      if self.count >= 50:
        self.count = 0
      # self.g1.SetValue(self.count)

      self.g2.Pulse()


#    def HideTitle(self, event):
#        if self.cb1.GetValue():
#            self.SetTitle('')
#	    self.cb.SetValue(False)
#	    self.logger.AppendText('HideTitle selected.\n' )
#        else:
#	    self.SetTitle('checkbox.py')
#	    self.logger.AppendText('HideTitle deselected.\n' )

    def ShowImage(self, event):
      if self.cbPNG.GetValue():
        self.logger.AppendText(_("Show Image %s.\n")% self.cbPNG.GetValue())
      else:
        self.logger.AppendText(_('No Image \n'))

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
      self.logger.AppendText(_('Selected font Top: %s\n') % event.GetString())
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

      self.logger.AppendText(_('Selected font Top Size: %s\n') % event.GetString())
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

      self.logger.AppendText(_('Selected font Midden: %s\n') % event.GetString())
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

      self.logger.AppendText(_('Selected font Midden Size: %s\n') % event.GetString())
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

      self.logger.AppendText(_('Selected font Bottom: %s\n') % event.GetString())
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

      self.logger.AppendText(_('Selected font Bottom Size: %s\n') % event.GetString())
      self.g2.Hide()

    def OnClick(self,event):
      self.g2.Show()
#      image=self.cbPNG.GetValue()
      self.logger.Clear()
      self.logger.AppendText(_('Image state %s.\n')% self.cbPNG.GetValue())
      self.logger.AppendText(_('STL state %s.\n')% self.cbSTL.GetValue())
      self.logger.AppendText(_('Gcode state %s.\n')% self.cbGcode.GetValue())
      thread.start_new_thread(self.longRunning, ())

#Van Hier

    def longRunning(self):
      global nameT
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
      makePNG=self.cbPNG.GetValue()
      makeSTL=self.cbSTL.GetValue()
      makeGcode=self.cbGcode.GetValue()
      if makePNG:
        makePNGf=(1)
      else:
        makePNGf=(0)
      if makeSTL:
        makeSTLf=(10)
      else:
        makeSTLf=(0)
      if makeGcode:
        if makeSTLf==(0):
          makeSTLf=(10)
          makeGcodef=(100)
        makeGcodef=(100)
      else:
        makeGcodef=(0)
      makeISG=makeGcodef+makeSTLf+makePNGf
      print makeISG
      self.logger.AppendText("make param %s\n" % makeISG)
#  self.logger.AppendText("\n\n\n\n\n\n\n\n\n\n\n\n") self.logger.Clear()
      self.logger.AppendText("Making key for %s\n" % nameT)
#  self.logger.AppendText("TPX %s\n" %editnameTPX)
      self.g2.Pulse()
      fo = open("varTMB.scad","w")
      writelineT = 'messageT="%s";\n'
      writelineT %= nameT
      writelineT=writelineT.encode('utf-8')
      fo.write(writelineT)
      fo.close()
      fo = open ("varTMB.scad","a")
      writeline2T=("font_sizeT=%s;\n" %fontsizeTSF)
      fo.write(writeline2T)
      fo.write(fontvarTF)
      positY='Posit= %s;\n'
      positY %=editnameTPY
      fo.write(positY)
# fo.write(posit)
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
      global directory
      directory = 'out'
    #Check version of OpenSad > 2013.06 
    #  wx.EVT_CHECKBOX(self, self.cbPNG.GetId(), self.ShowTitle)
    #    global nameTop=nameT
#Check if to make something
      if makePNGf==(1):
        self.createPNG()
      else:
#      if not self.cbPNG.GetValue(): 
        self.logger.AppendText(_('No img selected.\n'))
    #stl

      if makeSTLf==(0):
#      if not self.cbSTL.GetValue():
        self.logger.AppendText(_('No STL selected'))
#    self.logger.AppendText('passed 1')
      else:
#      if self.cbSTL.GetValue():
        self.createSTL()
#        self.logger.AppendText('STL to be generated\n')
#        runcommand = 'openscad -o %s/TMBkey%s.stl TMBKeychainV0.27.scad'
#        runcommand %= directory,nameT
#        runcommand=runcommand.encode('utf-8')
#        os.system(runcommand)
#        message = 'TMB-Key%s.stl is ready.'
#        message %= nameT
#        print message
#        self.logger.AppendText('TMB-key %s.stl is ready.\n' %nameT)  
      #Gcode
      if makeGcodef==(100):
        self.createGcode()
#      if self.cbGcode.GetValue():
#        self.logger.AppendText('Gcode Generate')
#        if not self.cbSTL.GetValue():
#          self.logger.AppendText=("Gcode Selected, STL not. Stl to be genarated to produce Gcode.\n")
#          runcommand2 = 'cura -i keymaker.ini -s %s/TMBkey%s.stl -o %s/TMBkey%s.gcode  '
#          runcommand2 %= directory,nameT,directory,nameT
#          runcommand2=runcommand2.encode('utf-8')
#          os.system(runcommand2)
#          message = 'TMB-Key %s is Sliced and ready to print.\nGreetings Xiao Shi Zi & Wim de Bonte,\nPro members of Timelab Gent Belgium ;-)\nReady to produce the next TMB-Key!\n'
#          message %= nameT
#          print message
#          self.logger.AppendText(message)
#          self.logger.AppendText("TMB-Key %s is Sliced and ready to print.\nUnder directory ./out/TMBkey*.gcode you'll find the .gcode file\nCopy to the SD card and happy printing.\nGreetings Xiao Shi Zi & Wim de Bonte,\nPro members of Timelab Gent Belgium ;-)\nReady to produce the next TMB-Key!\n" %nameT)
 #
 #     if self.cbGcode.GetValue():
        self.logger.AppendText=(_("Gcode to be generated\n"))
        runcommand = 'openscad -o %s/TMBkey%s.stl TMBKeychainV0.27.scad'
        runcommand %= directory,nameT
        runcommand=runcommand.encode('utf-8')
        os.system(runcommand)
        message = _('TMB-Key %s.stl is being sliced')
        message %= nameT
        print message
#      self.logger.AppendText("TMB-Key s.stl is ready to be sliced\n")# %nameT)
        runcommand2 = 'cura -i keymaker.ini -s %s/TMBkey%s.stl -o %s/TMBkey%s.gcode  '
        runcommand2 %= directory,nameT,directory,nameT
        runcommand2=runcommand2.encode('utf-8')
        os.system(runcommand2)
        message = _('TMB-Key %s is Sliced and ready to print.\nGreetings Xiao Shi Zi & Wim de Bonte,\nPro members of Timelab Gent Belgium ;-)\nReady to produce the next TMB-Key!\n')
        message %= nameT
        print message
#      self.logger.AppendText("TMB-Key %s is Sliced and ready to print.\nUnder directory ./out/TMBkey*.gcode you'll find the .gcode file\nCopy to the SD card and happy printing.\nGreetings Xiao Shi Zi & Wim de Bonte,\nPro members of Timelab Gent Belgium ;-)\nReady to produce the next TMB-Key!\n" %nameT)
      else: 
#      if not self.cbGcode.GetValue(): 
        self.logger.AppendText=(_("No Gcode Generated\n"))
#      self.g2.Hide()
#Img Y/N
      if makePNGf==(1):
#      if self.cbPNG.GetValue():
        self.logger.AppendText=(_("Display Image \n"))
        imageFile=('out/TMB%s.png' %nameT)
        png = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, png, (0, 550), (png.GetWidth(), png.GetHeight()))
#      else: self.logger.AppendText('No img selected.\n')
      self.g2.Hide()
#Tot Hier

    def createPNG(self):
#      self.logger.AppendText("TestPNG")
#      if self.cbPNG.GetValue():# and not self.cbSTL.GetValue() and not self.cbGcode.GetValue():
    #      self.logger.AppendText("only img selected.\n")
    #    OpenscadV='openscad --version > Openv.txt'
    #    os.system(OpenscadV)
    #png if OpenScad > 2013.06
      runcommand3 = 'openscad -o %s/TMB%s.png --camera=-35,-5,0,50,0,10,250 --imgsize=824,268 --projection=p TMBKeychainV0.27.scad'
      runcommand3 %= directory,nameT
      runcommand3=runcommand3.encode('utf-8')
      os.system(runcommand3)
      message3 = (_('TMB-Key %s.png is ready.')% nameT)#      message3 %= nameT
      print message3
      self.logger.AppendText(_('Img %s.png Selected.\n')% nameT)
      #      self.cb1.SetValue(False)

    def createSTL(self):
      self.logger.AppendText(_('STL to be generated\n'))
      runcommand = 'openscad -o %s/TMBkey%s.stl TMBKeychainV0.27.scad'
      runcommand %= directory,nameT
      runcommand=runcommand.encode('utf-8')
      os.system(runcommand)
      message = _('TMB-Key%s.stl is ready.')
      message %= nameT
      print message
      self.logger.AppendText(_('TMB-key %s.stl is ready.\n') %nameT)  

    def createGcode(self):
      self.logger.AppendText(_('Gcode Generate'))
#        if not self.cbSTL.GetValue():
#          self.logger.AppendText=("Gcode Selected, STL not. Stl to be genarated to produce Gcode.\n")
#          runcommand2 = 'cura -i keymaker.ini -s %s/TMBkey%s.stl -o %s/TMBkey%s.gcode  '
#          runcommand2 %= directory,nameT,directory,nameT
#          runcommand2=runcommand2.encode('utf-8')
#          os.system(runcommand2)
#          message = 'TMB-Key %s is Sliced and ready to print.\nGreetings Xiao Shi Zi & Wim de Bonte,\nPro members of Timelab Gent Belgium ;-)\nReady to produce the next TMB-Key!\n'
#          message %= nameT
#          print message
#          self.logger.AppendText(message)
#          self.logger.AppendText("TMB-Key %s is Sliced and ready to print.\nUnder directory ./out/TMBkey*.gcode you'll find the .gcode file\nCopy to the SD card and happy printing.\nGreetings Xiao Shi Zi & Wim de Bonte,\nPro members of Timelab Gent Belgium ;-)\nReady to produce the next TMB-Key!\n" %nameT)
 #
 #     if self.cbGcode.GetValue():
      self.logger.AppendText=(_("Gcode to be generated\n"))
      runcommand = 'openscad -o %s/TMBkey%s.stl TMBKeychainV0.27.scad'
      runcommand %= directory,nameT
      runcommand=runcommand.encode('utf-8')
      os.system(runcommand)
      message = _('TMB-Key %s.stl is being sliced')
      message %= nameT
      print message
#      self.logger.AppendText("TMB-Key s.stl is ready to be sliced\n")# %nameT)
      runcommand2 = 'cura -i keymaker.ini -s %s/TMBkey%s.stl -o %s/TMBkey%s.gcode  '
      runcommand2 %= directory,nameT,directory,nameT
      runcommand2=runcommand2.encode('utf-8')
      os.system(runcommand2)
      message = _('TMB-Key %s is Sliced and ready to print.\nGreetings Xiao Shi Zi & Wim de Bonte,\nPro members of Timelab Gent Belgium ;-)\nReady to produce the next TMB-Key!\n')
      message %= nameT
      print message
#      self.logger.AppendText("TMB-Key %s is Sliced and ready to print.\nUnder directory ./out/TMBkey*.gcode you'll find the .gcode file\nCopy to the SD card and happy printing.\nGreetings Xiao Shi Zi & Wim de Bonte,\nPro members of Timelab Gent Belgium ;-)\nReady to produce the next TMB-Key!\n" %nameT)




#    def OnEraseBackground(self, evt):
#      """
#      Add a picture to the background
#      """
#      self.logger.AppendText('EraseBackground')
#      # yanked from ColourDB.py
#      dc = evt.GetDC()
#      if not dc:
#        dc = wx.ClientDC(self)
#        rect = panel.GetUpdateRegion().GetBox()
#        dc.SetClippingRect(rect)
#      dc.Clear()
#      bmp = wx.Bitmap("logo.png")
#      dc.DrawBitmap(bmp, 1, 1)


app = wx.App(0)
M3NT(None, -1, '3NT-Key maker V0.01 by Timelab: 小狮子 & Wim ;-)')
app.MainLoop()
