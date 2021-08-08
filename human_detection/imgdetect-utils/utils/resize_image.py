import sys
import os
import shutil
import cv2
import argparse

# By Hyungjae Kim
def resize_image(img_dir):
    img_extensions = {'jpg', 'jpeg', 'png', 'bmp'}
    images = sorted([os.path.join(img_dir, f)
        for f in os.listdir(img_dir)
        if os.path.isfile(os.path.join(img_dir, f)) and 
        f.lower().split('.')[-1] in img_extensions])

    for imgfile in images:
        img = cv2.imread(imgfile)
        img_name = os.path.basename(imgfile)

        size = (24, 32)
        img = cv2.resize(img, size)

        cv2.imwrite(os.path.join(img_dir, img_name), img)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image-dir', '-d', dest='dir', required=True,
            help='Directory that contains the images to be processed ' +
            '(supported formats: jpg, png, tiff, bmp)')

    opts, args = parser.parse_known_args(sys.argv[1:])
    resize_image(img_dir=opts.dir)


if __name__ == '__main__':
    main()