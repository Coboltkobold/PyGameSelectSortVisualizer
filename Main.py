import sys
import pygame as pg
import random as rd
from PIL import Image

speed = 20

pg.init()
width,height = 1236,264

screen = pg.display.set_mode((width,height))
clock = pg.time.Clock()
pg.display.set_caption('Selection Sort Visualization')

class Bar:
	#class for creating and showing bars
	def __init__(self,x,y,height,color):
		self.x = x 
		self.y = y 
		self.height = height
		self.color = color

	def draw(self,surface):
		pg.draw.rect(surface,self.color,(self.x,self.y,20,self.height))

class Pointer:
	#class for storing pointer variables and location
	def __init__(self,x,y,color,shortest,numBars):
		self.x = x 
		self.y = y 
		self.color = color
		self.shortest = shortest
		self.shortI = 0
		self.pointer = 0
		self.index = 0
		self.numBars = numBars

	def draw(self,surface):
		pg.draw.rect(surface,self.color,(self.x,self.y,20,20))

	def compare(self,array):
		if self.index == self.numBars -1:
			#stops when sorting is done.
			return True
		elif self.pointer < self.numBars:
			#iterates through comparing heights and storing the shortest bar if the pointer is not at the end of the list.
			self.x = array[self.pointer].x
			if array[self.pointer].height < self.shortest.height:
				self.shortest = array[self.pointer]
				self.shortI = self.pointer
				self.color = array[self.pointer].color
			self.pointer += 1
		else:
			#if pointer is at end of list swaps shortest bar with current index bar and resets the pointer to the next index.
			array[self.index].x,array[self.shortI].x = array[self.shortI].x,array[self.index].x
			array[self.index],array[self.shortI] = array[self.shortI],array[self.index]
			self.index += 1
			self.shortI = self.index
			self.pointer = self.index
			self.shortest = array[self.index]
			self.color = array[self.index].color
			self.x = array[self.index].x
		return False

def shuffle(array):
	#goes through each element of array and swaps it with a random other element
	for i in range(len(array)):
		pointer = rd.randrange(len(array))
		array[i].x,array[pointer].x = array[pointer].x,array[i].x
		array[i],array[pointer] = array[pointer],array[i]

#creates bars in asending order
bars = []
numBars = 50
for i in range(1,numBars+1):
	inverse = numBars - i
	bar = Bar(i * 20 + (4 * (i-1)),220 - (i*2), i * 2,(200 / numBars * inverse,0,200 / numBars * i))
	bars.append(bar)

#shuffles bars
shuffle(bars)

#creates pointer
pointer = Pointer(10,224,bars[0].color,bars[0],numBars)

finished = False
frames = []
cnt = 0
while True:
	dt = clock.tick(speed)
	for event in pg.event.get():
		if event.type == pg.QUIT: sys.exit()
	screen.fill((10,10,10))

	for i in bars:
		i.draw(screen)
	if not finished:
		finished = pointer.compare(bars)
	pointer.draw(screen)

	pg.display.update()
	if not finished:
#		pg.image.save(screen,f"images/frame{cnt}.jpg")
		cnt += 1
	else:
		break
#pg.image.save(screen,f"images/frame{cnt}.jpg")