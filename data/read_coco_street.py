import glob
import os


folders = [
    'custom/labels/train2014',
    #'coco_street/labels/val2014',
]

for folder in folders:
    for path in glob.glob(folder + '/*'):
        with open(path, 'rb') as r:
            lines = r.read()
            print(lines)
        