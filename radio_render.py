#encoding: UTF-8

from PIL import ImageDraw, ImageFont, Image
from random import random
from datetime import datetime, timedelta, date
from time import gmtime, strftime
from sys import maxint


# definicje kolorow
czarny = (0,0,0)
czarny_gsmr = (25,25,25)
czarny2_gsmr = (10,10,10)
szary_gsmr = (200,200,200)
czarny_diag = (0,0,0)
bialy =(255,255,255)
bialy_diag =(255,255,255)
jszary =(218,218,218)
niebieski =(0,0,255)
niebieski_diag =(0,0,255)
ed = (157,145,95)
jasnoniebieski_diag = (133,128,255)
zolty_diag = (255,254,2)


class radio_render(abstractscreenrenderer):



	def __init__(self, lookup_path):
		self.podklad = self.openimage(lookup_path + "ek1")
		lookup_path = lookup_path + "screen/"
		self.ertms = Image.open(lookup_path + "ertms.png")
		
		self.sredni_arial = ImageFont.truetype('./fonts/arialbd.ttf', 34)
		self.maly_arial = ImageFont.truetype('./fonts/arialbd.ttf', 26)
		self.bmaly_arial = ImageFont.truetype('./fonts/arialbd.ttf', 16)
		self.gsmr1 = ImageFont.truetype('./fonts/myriadpro-regular.otf', 22)
		self.gsmr2 = ImageFont.truetype('./fonts/myriadpro-regular.otf', 14)
		self.gsmr3 = ImageFont.truetype('./fonts/myriadpro-regular.otf', 18)
		self.gsmr4 = ImageFont.truetype('./fonts/myriadpro-regular.otf', 80)
		
		self.kilometry = (random()*300000)+5000
		self.last_time_update = 0
		self.dzis = datetime.now().timetuple().tm_yday
		self.rok = datetime.now().year
		self.last_hour = 10
		self.temp = (random()*15) + 20
	def _render(self, state):

		obrazek = self.podklad.copy()
		draw = ImageDraw.Draw(obrazek)
		#czas
		if state['seconds'] != self.last_time_update:
			dt = state['seconds'] - self.last_time_update
			if dt < 0:
				dt+=60
			self.last_time_update = state['seconds']
		if state['hours']<10:
			godz = "0" + str(state['hours'])
		else:
			godz = str(state['hours'])
		if state['minutes']<10:
			min = "0" + str(state['minutes'])
		else:
			min = str(state['minutes'])
		if state['seconds']<10:
			sec = "0" +str(state['seconds'])
		else:
			sec = str(state['seconds'])
#data
		if self.last_hour == 23 and state['hours'] == 0:
			self.dzis = self.dzis+1 # wlasnie wybila polnoc
		self.last_hour = state['hours']
		data = datetime(self.rok, 1, 1) + timedelta(self.dzis - 1)
		dzien = datetime.weekday(data)
		data = data.strftime("%d.%m.%Y")
		DayL = ['Pn','Wt',u'Śr','Cz','Pt','So','Nd']
		zmienna_kanalu = str(state['radio_channel'])
		if state['battery']:
	#GSMR------------------------------------------------------------------------------------------------------------------------------------------------------------------------
			#tlo
			draw.rectangle(((1287,15),(1756,304)), fill=czarny2_gsmr)
			draw.rectangle(((1290,25),(1751,298)), fill=szary_gsmr)
			#ikonka trojkat rog
			draw.polygon([1293,69,1325,69,1325,42],fill=czarny_gsmr)
			
			#ikonka jasnosc ekranu?
			draw.polygon([1720,165,1745,165,1745,225],outline=czarny_gsmr)
			draw.line((1725,176, 1745, 176), fill=czarny_gsmr, width=2)
			draw.line((1730,187, 1745, 187), fill=czarny_gsmr, width=2)		
			draw.line((1735,198, 1745, 198), fill=czarny_gsmr, width=2)	
			draw.polygon([1740,210,1745,210,1745,225],fill=czarny_gsmr)
			
			#ikonka nad sloneczniekim
			draw.ellipse([1294,98,1326,151],outline=czarny_gsmr)
			draw.pieslice([1294,98,1326,151],-90, 90, fill=czarny_gsmr)
			
			#ikonka sloneczka
			draw.ellipse([1298,170,1322,214],outline=czarny_gsmr)
			draw.line((1310,164, 1310, 170), fill=czarny_gsmr, width=1)
			draw.line((1324,167, 1320, 176), fill=czarny_gsmr, width=1)
			draw.line((1327,192, 1322, 192), fill=czarny_gsmr, width=1)
			draw.line((1324,215, 1319, 207), fill=czarny_gsmr, width=1)		
			draw.line((1310,220, 1310, 214), fill=czarny_gsmr, width=1)	
			draw.line((1297,215, 1302, 206), fill=czarny_gsmr, width=1)	
			draw.line((1293,192, 1298, 192), fill=czarny_gsmr, width=1)	
			draw.line((1296,168, 1302, 177), fill=czarny_gsmr, width=1)	
			

			#placek po srodku
			draw.rectangle(((1482,76),(1571,197)), fill=czarny_gsmr)
			draw.rectangle(((1488,69),(1563,75)), fill=czarny_gsmr)
			draw.rectangle(((1488,190),(1563,204)), fill=czarny_gsmr)
			draw.pieslice([1482,190,1499,204],90, 180, fill=czarny_gsmr)
			draw.pieslice([1555,190,1571,204],0, 90, fill=czarny_gsmr)
			draw.pieslice([1482,69,1499,83],180, 270, fill=czarny_gsmr)
			draw.pieslice([1555,69,1571,83],270, 0, fill=czarny_gsmr)
			
			#ikonka glosnosci
			draw.line((1675,195, 1675, 224), fill=czarny_gsmr, width=2)
			draw.line((1670,215, 1675, 224), fill=czarny_gsmr, width=2)
			draw.line((1670,215, 1666, 215), fill=czarny_gsmr, width=2)
			draw.line((1666,204, 1666, 215), fill=czarny_gsmr, width=2)
			draw.line((1666,204, 1670, 204), fill=czarny_gsmr, width=2)
			draw.line((1675,195, 1670, 204), fill=czarny_gsmr, width=2)
			
			#linie
			draw.line((1330,25, 1330, 299), fill=czarny_gsmr, width=1)
			draw.line((1628,25, 1628, 299), fill=czarny_gsmr, width=1)
			draw.line((1330,57, 1750, 57), fill=czarny_gsmr, width=1)
			draw.line((1342,228, 1750, 228), fill=czarny_gsmr, width=1)		
			draw.line((1291,91, 1330, 91), fill=czarny_gsmr, width=1)	
			draw.line((1291,159, 1330, 159), fill=czarny_gsmr, width=1)	
			draw.line((1291,227, 1330, 227), fill=czarny_gsmr, width=1)	
			draw.line((1628,89, 1750, 89), fill=czarny_gsmr, width=1)	
			draw.line((1628,123, 1750, 123), fill=czarny_gsmr, width=1)	
			draw.line((1628,158, 1750, 158), fill=czarny_gsmr, width=1)	
			draw.line((1342,298, 1342, 228), fill=czarny_gsmr, width=1)	
			draw.line((1382,298, 1382, 228), fill=czarny_gsmr, width=1)			
			draw.line((1422,298, 1422, 228), fill=czarny_gsmr, width=1)			
			draw.line((1462,298, 1462, 228), fill=czarny_gsmr, width=1)			
			draw.line((1504,298, 1504, 228), fill=czarny_gsmr, width=1)			
			draw.line((1546,298, 1546, 228), fill=czarny_gsmr, width=1)	
			draw.line((1586,298, 1586, 228), fill=czarny_gsmr, width=1)							
			draw.line((1668,298, 1668, 228), fill=czarny_gsmr, width=1)			
			draw.line((1710,298, 1710, 228), fill=czarny_gsmr, width=1)	
			draw.line((1432,57, 1432, 25), fill=czarny_gsmr, width=1)		
			
			#napisy
			if state['radio_channel'] < 10:
					draw.text((1340,56), "K " + zmienna_kanalu, font=self.gsmr4, fill=czarny_gsmr)
			if (state['radio_channel']==10):
					draw.text((1340,56), "K" + zmienna_kanalu, font=self.gsmr4, fill=czarny_gsmr)		
					
			draw.text((1340,138), u'Gruppenruf 3', fill=czarny_gsmr, font=self.gsmr1)	
			draw.text((1340,163), u'Zew 3', fill=czarny_gsmr, font=self.gsmr1)		
			draw.text((1489,128), u'ZEW 3', fill=szary_gsmr, font=self.maly_arial)	
			draw.text((1344,32), godz +":"+ min +":"+ sec, fill=czarny_gsmr, font=self.gsmr1)
			draw.text((1456,32), u'analog     (PKP)', fill=czarny_gsmr, font=self.gsmr1)
			draw.text((1291,257), u'KASUJ', fill=czarny_gsmr, font=self.gsmr2)
			draw.text((1346,240), u'ZEW', fill=czarny_gsmr, font=self.gsmr3)
			draw.text((1356,270), u'1', fill=czarny_gsmr, font=self.gsmr1)
			draw.text((1386,240), u'ZEW', fill=czarny_gsmr, font=self.gsmr3)
			draw.text((1396,270), u'2', fill=czarny_gsmr, font=self.gsmr1)
			draw.text((1426,240), u'ZEW', fill=czarny_gsmr, font=self.gsmr3)
			draw.text((1436,270), u'3', fill=czarny_gsmr, font=self.gsmr1)
			draw.text((1466,255), u'RStp', fill=czarny_gsmr, font=self.gsmr3)
			draw.text((1512,255), u'SQL', fill=czarny_gsmr, font=self.gsmr3)
			draw.text((1547,255), u'MON', fill=czarny_gsmr, font=self.gsmr3)
			draw.text((1587,255), u'Kanal', fill=czarny_gsmr, font=self.gsmr3)
			draw.text((1632,251), u'SYS', fill=czarny_gsmr, font=self.gsmr1)
			draw.text((1670,255), u'CZAS', fill=czarny_gsmr, font=self.gsmr3)		
		return obrazek
