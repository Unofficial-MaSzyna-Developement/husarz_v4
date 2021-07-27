#encoding: UTF-8

from PIL import ImageDraw, ImageFont, Image
from random import random
from datetime import datetime, timedelta, date
from time import gmtime, strftime
from sys import maxint
import time

def byteSumToBools(toconv):
	toconv-=1
	subract=128
	booltable=[False,False,False,False,False,False,False,False]
	for i in range(8):
		if((int(toconv)/int(subract))>=1):
			booltable[i]=True
			toconv-=subract
		subract/=2
	return booltable


#draw.ellipse(((2193,1595),(2226,1630)), fill=ref_red) #przód prawy
#draw.ellipse(((2251,1594),(2284,1629)), fill=ref_red) #przód lewy
#draw.ellipse(((2223,1561),(2256,1596)), fill=ref_red) #przód górny
#draw.ellipse(((2193,1673),(2226,1708)), fill=ref_red) # tył prawy
#draw.ellipse(((2251,1673),(2284,1708)), fill=ref_red) # tył lewy
#draw.ellipse(((2223,1641),(2256,1674)), fill=ref_red) #tył górny
def byteSumToDraw(toconv, side, draw): #side == 0 - przód side == 1 - tył 
	if(toconv / 256 >= 1):
		if(side==0):
			draw.ellipse(((2193,1595),(2226,1630)), fill=ref_white)
		if(side==1):
			draw.ellipse(((2193,1673),(2226,1708)), fill=ref_white)
		toconv -= ((toconv/256)*256) # odejmujemy od sumy
	if(toconv / 128 >= 1):
		if(side==0):
			draw.ellipse(((2251,1594),(2284,1629)), fill=ref_white)
		if(side==1):
			draw.ellipse(((2251,1673),(2284,1708)), fill=ref_white)
		toconv -= ((toconv/128)*128)
	if(toconv / 32 >= 1):
		if(side==0):
			draw.ellipse(((2193,1595),(2226,1630)), fill=ref_red)
		if(side==1):
			draw.ellipse(((2193,1673),(2226,1708)), fill=ref_red)
		toconv -= ((toconv/32)*32)
	if(toconv / 16 >= 1):
		if(side==0):
			draw.ellipse(((2193,1595),(2226,1630)), fill=ref_white)
		if(side==1):
			draw.ellipse(((2193,1673),(2226,1708)), fill=ref_white)
		toconv -= ((toconv/16)*16)
	if(toconv / 4 >= 1):
		if(side==0):
			draw.ellipse(((2223,1561),(2256,1596)), fill=ref_white)
		if(side==1):
			draw.ellipse(((2223,1641),(2256,1674)), fill=ref_white)
		toconv -= ((toconv/4)*4)
	if(toconv / 2 >= 1):
		if(side==0):
			draw.ellipse(((2251,1594),(2284,1629)), fill=ref_red)
		if(side==1):
			draw.ellipse(((2251,1673),(2284,1708)), fill=ref_red)
		toconv -= ((toconv/2)*2)
	if(toconv / 1 >= 1):
		if(side==0):
			draw.ellipse(((2251,1594),(2284,1629)), fill=ref_white)
		if(side==1):
			draw.ellipse(((2251,1673),(2284,1708)), fill=ref_white)
		toconv -= ((toconv/1)*1)
	if(toconv==0):
		print("ok")
	if(toconv==1):
		print("nie ok")


# definicje kolorow
czarny = (0,0,0)
czarny_gsmr = (25,25,25)
czarny2_gsmr = (10,10,10)
szary_gsmr = (200,200,200)
czarny_diag = (0,0,0)
bialy =(255,255,255)
bialy_diag =(255,255,255)
jszary =(220,220,220)
niebieski =(0,0,255)
niebieski_diag =(0,0,255)
ed = (255,254,2)
jasnoniebieski_diag = (133,128,255)
zolty_diag = (255,254,2)
fiolet = (255, 0, 255)
ref_white = (255, 255, 0)
ref_red = (255, 0, 0)

class eu44_render(abstractscreenrenderer):



	def __init__(self, lookup_path):
		self.podklad = self.openimage(lookup_path + "int/screen")
		lookup_path = lookup_path + "screen/"
		self.ertms = Image.open(lookup_path + "ertms.png")
		self.diag = Image.open(lookup_path + "diagnostyczny.png")
		self.sredni_arial = ImageFont.truetype('./fonts/arialbd.ttf', 80)
		self.maly_arial = ImageFont.truetype('./fonts/arialbd.ttf', 60)
		self.bmaly_arial = ImageFont.truetype('./fonts/arialbd.ttf', 40)
		self.gsmr1 = ImageFont.truetype('./fonts/myriadpro-regular.otf', 22)
		self.gsmr2 = ImageFont.truetype('./fonts/myriadpro-regular.otf', 14)
		self.gsmr3 = ImageFont.truetype('./fonts/myriadpro-regular.otf', 18)
		self.gsmr4 = ImageFont.truetype('./fonts/myriadpro-regular.otf', 80)
		self.maska = Image.open(lookup_path + "maska.png")
		self.sifa = Image.open(lookup_path + "sifa.png").convert("RGBA")
		self.shp = Image.open(lookup_path + "shp.png").convert("RGBA")
		self.panto_nmozna = Image.open(lookup_path + "panto_nmozna.png")
		self.panto_mozna = Image.open(lookup_path + "panto_mozna.png")
		self.ws_initized = Image.open(lookup_path + "ws_initized.png")
		self.ws_ninitized = Image.open(lookup_path + "ws_ninitized.png")
		self.brak_jazdy = Image.open(lookup_path + "brak_jazdy.png")

		self.engine1off = Image.open(lookup_path + "engine_1_off.png")
		self.engine2off = Image.open(lookup_path + "engine_2_off.png")
		self.engine3off = Image.open(lookup_path + "engine_3_off.png")
		self.engine4off = Image.open(lookup_path + "engine_4_off.png")
		self.engine1on = Image.open(lookup_path + "engine_1_on.png")
		self.engine2on = Image.open(lookup_path + "engine_2_on.png")
		self.engine3on = Image.open(lookup_path + "engine_3_on.png")
		self.engine4on = Image.open(lookup_path + "engine_4_on.png")
		self.loading = Image.open(lookup_path + "loading.png")

		self.kilometry = (random()*300000)+5000
		self.last_time_update = 0
		self.dzis = datetime.now().timetuple().tm_yday
		self.rok = datetime.now().year
		self.last_hour = 10
		self.temp = (random()*15) + 20
		self.last_time_update = 0
		self.aktyw = 0
		self.pobranyprad = 0
		self.oddanyprad = 0
		
	def _render(self, state):
		obrazek = self.podklad.copy()
		seconds = state['seconds']	
		if state['battery'] or state['converter']:
			
			dt = 0

			draw = ImageDraw.Draw(obrazek)

			if seconds != self.last_time_update:
				dt = seconds - self.last_time_update
				if dt < 0:
					dt+=60
				self.last_time_update = seconds

			self.aktyw += dt
			if self.aktyw<5:
				war_prawy = False
				war_tacho = False
			else:
				war_prawy = True
				war_tacho = True

			if (war_tacho == False):
				# Loading screen
				if state['battery'] or state['converter']:
					obrazek.paste(self.loading, (136, 2157), self.diag) # ekran ERTMS
					obrazek.paste(self.loading, (136, 101), self.diag) # ekran diagnostyczny

					# Pasek ladowania
					if self.aktyw >= 0:
						draw.rectangle(((3, 1670), (109, 1851)), fill=niebieski)
					if self.aktyw >= 0:
						draw.rectangle(((3, 1670), (109, 1851)), fill=niebieski)


			else:
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
				datab = data.strftime("%d.%m.%y")
				data = data.strftime("%d.%m.%Y")
				DayL = ['Pn','Wt',u'Śr','Cz','Pt','So','Ni']
				zmienna_kanalu = str(state['radio_channel'])

				speed = state['velocity']

				if speed > 240:
					speed = 240

				if state['battery'] or state['converter']:
					obrazek.paste(self.ertms, (136, 2157), self.ertms) # podklad pod ekran srodek
					obrazek.paste(self.diag, (136, 101), self.diag) # ekran diagnostyczny

					#ERTMS prędkościomierz

					rotate = speed * 300 / 240 + 30
					rad =  radians(rotate)
					srodek_tacho = (876, 2685)
					point = (-10,0)
					p1 = (point[0]*cos(rad)-point[1]*sin(rad) + srodek_tacho[0],point[0]*sin(rad)+point[1]*cos(rad) + srodek_tacho[1])
					point = (-10,300)
					p2 = (point[0]*cos(rad)-point[1]*sin(rad) + srodek_tacho[0],point[0]*sin(rad)+point[1]*cos(rad) + srodek_tacho[1])
					point = (-2,325)
					p3 = (point[0]*cos(rad)-point[1]*sin(rad) + srodek_tacho[0],point[0]*sin(rad)+point[1]*cos(rad) + srodek_tacho[1])
					point = (-2,400)
					p4 = (point[0]*cos(rad)-point[1]*sin(rad) + srodek_tacho[0],point[0]*sin(rad)+point[1]*cos(rad) + srodek_tacho[1])
					point = (10,0)
					p8 = (point[0]*cos(rad)-point[1]*sin(rad) + srodek_tacho[0],point[0]*sin(rad)+point[1]*cos(rad) + srodek_tacho[1])
					point = (10,300)
					p7 = (point[0]*cos(rad)-point[1]*sin(rad) + srodek_tacho[0],point[0]*sin(rad)+point[1]*cos(rad) + srodek_tacho[1])
					point = (2,325)
					p6 = (point[0]*cos(rad)-point[1]*sin(rad) + srodek_tacho[0],point[0]*sin(rad)+point[1]*cos(rad) + srodek_tacho[1])
					point = (2,400)
					p5 = (point[0]*cos(rad)-point[1]*sin(rad) + srodek_tacho[0],point[0]*sin(rad)+point[1]*cos(rad) + srodek_tacho[1])
					draw.polygon([p1,p2,p3,p4,p5,p6,p7,p8],fill=jszary)
					self.print_center(draw, '%d' % speed, 876, 2685, self.sredni_arial, czarny) # Wyświetlanie cyferki
					
					# Tempomat
					tempomat = state['new_speed'] * 5
					if tempomat > 0:
						rotate = tempomat * 300 / 240 + 30 - 180
						rad =  radians(rotate)
						srodek = (876, 2675)
						point = (0,-418)
						p1 = (srodek[0]+point[0]*cos(rad)-point[1]*sin(rad),srodek[1]+point[1]*cos(rad)+point[0]*sin(rad))
						point = (-12,-430)
						p2 = (srodek[0]+point[0]*cos(rad)-point[1]*sin(rad),srodek[1]+point[1]*cos(rad)+point[0]*sin(rad))
						point = (0,-442)
						p3 = (srodek[0]+point[0]*cos(rad)-point[1]*sin(rad),srodek[1]+point[1]*cos(rad)+point[0]*sin(rad))
						point = (12,-430)
						p4 = (srodek[0]+point[0]*cos(rad)-point[1]*sin(rad),srodek[1]+point[1]*cos(rad)+point[0]*sin(rad))
						draw.polygon([p1,p2,p3,p4],fill=zolty_diag)


					# Cisnienie w PG

					pg_pressure = state['eimp_pn1_bp']
					if (pg_pressure > 8):
						pg_pressure = 8

					height = 1366 - (1087 / 8 * pg_pressure)
					if (pg_pressure > 4.70):
						# x, y, x + szerokosc, y - wysokosc
						draw.rectangle(((1805, 1366), (1805 + 77, height)), fill=niebieski)
					else:
						draw.rectangle(((1805, 1366), (1805 + 77, height)), fill=zolty_diag)

					

					# Napiecie w sieci
					voltage = state['traction_voltage'] / 1000 - 2.0
					print(voltage)
					if (voltage > 2.5):
						voltage = 2.5

					if (voltage < 0.0):
						voltage = 0.0

					height = 1162 - (971 / 2.5 * voltage) # pozycja bezwzgledna lewego rogu Y, wysokosc / zakres * wartosc

					draw.rectangle(((335, 1162), (335 + 36, height)), fill=niebieski) # X, Y, X + szer, wysokosc


					# Cylindry hamulcowe

					ch_pressure = float(state['eimp_pn1_bc'])
					#self.print_center(draw, '%d' % ch_pressure, 876, 2685, self.sredni_arial, czarny) # Wyświetlanie cyferki
					if (ch_pressure > 5):
						ch_pressure = 5


					draw.rectangle(((2150, 1088),(2150 + (452 / 5 * ch_pressure), 1088 + 74)), fill=zolty_diag)

					draw.rectangle(((2150, 1288),(2150 + (452 / 5 * ch_pressure), 1288 + 74)), fill=zolty_diag)

					#cisnienie w ZG

					zg_pressure = state['eimp_pn1_sp']

					if zg_pressure > 12:
						zg_pressure = 12

					height = 280 + 695 - (695 / 12 * zg_pressure) # pozycja bezwzgledna lewego rogu Y, wysokosc / zakres * wartosc

					draw.rectangle(((2163, 280+695), (2163 + 74, height)), fill=zolty_diag) # X, Y, X + szer, wysokosc

					
					# SIŁY

					force = state['eimp_c1_fr'] / 4
					if (force > 90):
						force = 90
					if (force < -90):
						force = -90
					if (force > 0):
						height = 1246 - (1055 / 90 * force) # pozycja bezwzgledna lewego rogu Y, wysokosc / zakres * wartosc
						draw.rectangle(((914, 1246), (914 + 99, height)), fill=niebieski) # X, Y, X + szer, wysokosc
						draw.rectangle(((1133, 1246), (1133 + 99, height)), fill=niebieski) # X, Y, X + szer, wysokosc
						draw.rectangle(((1353, 1246), (1353 + 99, height)), fill=niebieski) # X, Y, X + szer, wysokosc
						draw.rectangle(((1572, 1246), (1572 + 99, height)), fill=niebieski) # X, Y, X + szer, wysokosc

					if (force < 0):
						force = force * -1
						height = 1246 - (1055 / 90 * force) # pozycja bezwzgledna lewego rogu Y, wysokosc / zakres * wartosc
						draw.rectangle(((914, 1246), (914 + 99, height)), fill=zolty_diag) # X, Y, X + szer, wysokosc
						draw.rectangle(((1133, 1246), (1133 + 99, height)), fill=zolty_diag) # X, Y, X + szer, wysokosc
						draw.rectangle(((1353, 1246), (1353 + 99, height)), fill=zolty_diag) # X, Y, X + szer, wysokosc
						draw.rectangle(((1572, 1246), (1572 + 99, height)), fill=zolty_diag) # X, Y, X + szer, wysokosc

					# Ampery
					current = state['eimp_c1_ihv']
					if (current > 3000):
						current = 3000
					if (current < 0):
						current = current * -1
					height = 1244 - (float(float(1051) / float(3000)) * current) # pozycja bezwzgledna lewego rogu Y, wysokosc / zakres * wartosc
					draw.rectangle(((624, 1244), (624 + 32, height)), fill=niebieski) # X, Y, X + szer, wysokosc

					# Siła realizowana
					frt = (state['eimp_c1_frt'])
					if not -maxint-1 <= frt <= maxint:
						frt = (frt + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
					end = int(frt / 2 - 90)
					draw.pieslice((1528,2246,2375, 3026), -90, end, fill=niebieski)

					#siła hamowania
					frb = (state['eimp_c1_frb'])
					if not -maxint-1 <= frb <= maxint:
						frb = (frb + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
					end = int(-frb - 90)
					draw.pieslice((1528,2246,2375, 3076), end, -90 , fill=ed)
					obrazek.paste(self.maska,(1528,2246),self.maska)

					# Procent siły
					force_precetange = int(state['eimp_c1_pr'] * 100)
					self.print_right(draw, '%d' % force_precetange, 2000, 2946, self.sredni_arial, czarny) # Wyświetlanie cyferki

					# Kontrolki
					# Czuwak/SIFA
					if (state['ca']):
						obrazek.paste(self.sifa, (2212, 3321), self.sifa)

					# SHP
					if (state['shp']):
						obrazek.paste(self.shp, (333, 3318), self.shp)

					# Moc kN diagnostyczy
					force_full = state['eimp_t_fd']
					if (force_full >= 0):
						self.print_right(draw, '%d' % force_full, 2000, 1584, self.maly_arial, niebieski) # Wyświetlanie cyferki
					else:
						self.print_right(draw, '%d' % force_full * -1, 2000, 1584, self.maly_arial, zolty_diag) # Wyświetlanie cyferki

					# Status WS
					pantpressure = state['pantpress']
					if pantpressure < 3.5 and state['traction_voltage'] < 500:
						obrazek.paste(self.panto_nmozna, (616, 1536), self.panto_nmozna)
					if pantpressure >= 3.5 and state['traction_voltage'] < 500:
						obrazek.paste(self.panto_mozna, (616, 1536), self.panto_mozna)
					if pantpressure >= 3.5 and state['traction_voltage'] > 2500 and state["main_init"] == True and state['linebreaker'] == False:
						obrazek.paste(self.ws_ninitized, (616, 1536), self.ws_ninitized)
					if pantpressure >= 3.5 and state['traction_voltage'] > 2500 and state["main_init"] == False and state['linebreaker'] == False:
						obrazek.paste(self.ws_initized, (616, 1536), self.ws_initized)

					# Brak jazdy
					if (state['linebreaker'] == False or state['eimp_pn1_bc'] > 0.2 or state['brakes_1_spring_active'] == True):
						obrazek.paste(self.brak_jazdy, (1079, 1536), self.brak_jazdy)
						

					# Diag time
					draw.text((2330,345), godz +":"+ min +":"+ sec, fill=czarny, font=self.maly_arial) # Godzina
					draw.text((2300,164), DayL[dzien] + " " + datab, fill=czarny, font=self.maly_arial) # Godzina

					# Silniki status

					if (state['linebreaker']):
						obrazek.paste(self.engine1on, (817, 1279), self.engine1on)
						obrazek.paste(self.engine2on, (1057, 1279), self.engine2on)
						obrazek.paste(self.engine3on, (1296, 1279), self.engine3on)
						obrazek.paste(self.engine4on, (1535, 1279), self.engine4on)
					else:
						obrazek.paste(self.engine1off, (817, 1279), self.engine1off)
						obrazek.paste(self.engine2off, (1057, 1279), self.engine2off)
						obrazek.paste(self.engine3off, (1296, 1279), self.engine3off)
						obrazek.paste(self.engine4off, (1535, 1279), self.engine4off)

					# Ref status
					ref_a = state['lights_front']
					ref_b = state['lights_rear']
					#Reflektory
					byteSumToDraw(ref_a, 0, draw)
					byteSumToDraw(ref_b, 1, draw)
					#Pobierany/oddawany prąd (w kWh) baniel zweryfikuje
					voltage = state['traction_voltage']
					current = state['eimp_c1_ihv']
					if (current > 0):
						self.pobranyprad+=float((current*voltage)/12047935.8)
					if (current < 0):
						current*=-1
						self.oddanyprad+=float((current*voltage)/11673469.4)
					draw.text((2322,746), str(int(floor(self.pobranyprad))), fill=niebieski, font=self.maly_arial)
					draw.text((2322,923), str(int(floor(self.oddanyprad))), fill=zolty_diag, font=self.maly_arial)



		else:
			self.aktyw = 0

		return obrazek
