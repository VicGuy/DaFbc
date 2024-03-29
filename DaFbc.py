#!/usr/bin/env python3

'''
    DaFbc background image conversion tool for Mo Young / Da Fit
    binary files.

    Author: Vic <vicpt[at]protonmail.com>
    Copyright (C) 2024 Vic

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from PIL import Image
import numpy as np
import sys
import os

imgfile = None
binfile = None

''' Convert an image to rgb565 in bin'''
def convertImg2bin(w, h):
    #Open image
    image = Image.open(imgfile) 
    image = image.resize((w,h))

    #Convert to RGB565
    image_rgb565 = np.array(image, dtype=np.uint16)
    image_rgb565 = ((image_rgb565[..., 0] >> 3) << 11) | ((image_rgb565[..., 1] >> 2) << 5) | (image_rgb565[..., 2] >> 3)

    return image_rgb565

''' Swipes bytes from a file '''
def bytesSwapper (filename):
	bytes_array = bytearray(filename)
	
	for x in range(0, len(bytes_array) - 2, 2):
		tmp = bytes_array[x]
		bytes_array[x] = bytes_array[x + 1]
		bytes_array[x + 1] = tmp

	return bytes_array

''' Save binary file '''
def saveFile(bfile):
    try:
        f=open(binfile, 'wb')
        f.write(bfile)
        f.close()
    except Exception:
        print ("[ERROR] Writing file.")

''' Main method '''
def main():
    if (len(sys.argv) < 3):
        print ("Usage:  DaFbc.py IMGNAME OUTPUTFILE")
        return
    
    if not (os.path.exists(sys.argv[1])):
        print ("[ERROR] Can't open the image file.")
        return
    
    global imgfile
    global binfile
    imgfile = sys.argv[1]
    binfile = sys.argv[2]
    
    background = convertImg2bin(240, 296)
    preview = convertImg2bin(140, 163)

    mfile = background.tobytes() + preview.tobytes()
    mfile = bytesSwapper(mfile)
    
    saveFile(mfile)
    
    print ("Done.")
    

if __name__ == "__main__":
    main()