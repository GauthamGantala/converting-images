#!/usr/bin/env python3

from PIL import Image
import os

def image_convert(image):
  try:
    out = "/opt/icons/" + image
    inp = os.getcwd() + "/images/" + image
    pic = Image.open(inp)
    #rotating the iamge resizing it and also converting into jpeg format
    pic.rotate(90).resize((128, 128)).convert('RGB').save(out, 'JPEG')
  except OSError:
    #OSError serves as the error class for the os module
    #and is raised when an error comes back from an os-specific function.
    pass

if __name__ == "__main__":
  file = os.listdir(os.getcwd() + "/images/")
  for image in file:
    image_convert(image)
