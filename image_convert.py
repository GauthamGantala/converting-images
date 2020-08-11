#!/usr/bin/python3

from PIL import Image
import os
import argparse
from sys import exit

def image_convert(image,output,inputpth,angel,height,width):
	try:
		inputfile = inputpth + "/" + image
		outputfile = output + "/" + image
		pic = Image.open(inputfile)
		#rotating the iamge resizing it and also converting into jpeg format
		pic.rotate(angel).resize((height, width)).convert('RGB').save(outputfile, 'JPEG')
		print("\t" + str(image) + " "*(40-len(image)) + " [ Success ]")
	except OSError:
		print("\t" + str(image) + " "*(40-len(image)) + " [ Failed  ]")
		pass

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-s', '--single', default=None,  help='Convert Single Image File')
	parser.add_argument('-m', '--multiple', default=None, nargs='+', help='Convert Multiple Image Files')
	parser.add_argument('-a', '--all', default=False, action='store_true', help='Convert All Image Files in the directory')
	parser.add_argument('-o', '--output', default='imgcvrt', help='Output File Path')
	parser.add_argument('-i', '--input', default=None, help='Input File Path')
	args = parser.parse_args()
	sfile = args.single
	mfiles = args.multiple
	allfiles = args.all
	output = args.output
	if args.input == None:
		inputpth = os.getcwd()
	else:
		inputpth = args.input
	if sfile != None:
		try:
			os.mkdir("imgcvrt")
		except FileExistsError:
			pass
			
	try:
		if sfile != None:
			file = [sfile]
		elif mfiles != None:
			file = args.multiple
		elif allfiles != False:
			file = os.listdir(inputpth)
		else:
			exit(1)
		print("Savile File/s to : " + output)
		print("Converting Image Files :")
		#for rotating the image
		try:
			rot = int(input("Enter the Angle To Rotate the images : "))
			if rot < 361 and rot > -361:
				rotagl = rot
			else:
				rotagl = 0
		except:
			rotagl = 0
		#for resizing the image to a particular height and width
		try:
			height = int(input("Enter the Height the images : "))
			width = int(input("Enter the Width the images : "))
			if height > 0 and width > 0:
				ht = height
				wt = width
			else:
				ht = wt = 128
		except:
			ht = wt = 128
		#Now calling the image_convert function
		for image in file:
			image_convert(image,output,inputpth,rotagl,ht,wt)

	except FileNotFoundError:
		print("Path Does Not Exist")
