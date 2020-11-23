from PIL import Image
import argparse
import os

BASE_PATH = 'test'


class ImageHandler():
	""" """

	def __init__(self, imagename):
		self.imgname = imagename
		self.img = Image.open(imagename)

	def flip(self):
		img = self.img.transpose(Image.FLIP_LEFT_RIGHT)
		new_name = self.imgname.split('.')[-2] + '_flipped.' + self.imgname.split('.')[-1]
		print(new_name)
		self.write_image(img, new_name)

		#raise saturation and value
		#color jittering
		#potentially random crops

	def write_image(self, img, name):
		img.save(name)


def run_images(path):
	for file in os.listdir(path):
		i = ImageHandler(path+'/'+file)
		i.flip()



if __name__ == "__main__":
	run_images(BASE_PATH)
