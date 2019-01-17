import sys, getopt
from interval import Interval
from PIL import Image
from numpy import *

intervals = [Interval(181, 255), Interval(363, 436), Interval(544, 618)]
breakpoints = [0, 181, 363, 544]

def pic_stitch(image_arr_arr):
    re = zeros((800, 800, 3))
    for i in range(0, 4):
        for j in range(0, 4):
            im_arr = pad(image_arr_arr[i][j], ((0, 544), (0, 544), (0, 0)), 'constant')  #256*256*3
            im_arr = roll(im_arr, breakpoints[i], axis=1)
            im_arr = roll(im_arr, breakpoints[j], axis=0)
            re = re + im_arr
    for i in range(0, 800):
        for j in range(0, 800):
            t = 1
            if (i in intervals[0] or i in intervals[1] or i in intervals[2]) and (j in intervals[0] or j in intervals[1] or j in intervals[2]):
                t = 4
            elif (i in intervals[0] or i in intervals[1] or i in intervals[2]) and not (j in intervals[0] or j in intervals[1] or j in intervals[2]):
                t = 2
            elif not (i in intervals[0] or i in intervals[1] or i in intervals[2]) and (j in intervals[0] or j in intervals[1] or j in intervals[2]):
                t = 2
            else:
                t = 1
            re[i][j] = re[i][j] / t
    return re


def get_image_arr_arr(path, pic_name, suffix):
    return [[array(Image.open("%(path)s/%(pic_name)s_%(i)d_%(j)d%(suffix)s"
                              % {'path': path, 'pic_name': pic_name, 'i':i, 'j':j, 'suffix':suffix}))
             for j in range(0, 4)] for i in range(0, 4)]


def put_image(path, pic_name, image_arr):
    image_arr = array(image_arr, 'uint8')
    image = Image.fromarray(image_arr)
    image.save("%(path)s/%(pic_name)s" % {'path': path, 'pic_name': pic_name})


if __name__ == '__main__':
    print(sys.argv) #python pic_stitch.py -p ./trans_task -n 1
    try:
        options, args = getopt.getopt(sys.argv[1:], "p:n:s:", ["path=", "name=","suffix="])
    except getopt.GetoptError:
        sys.exit()

    print(options)
    path = ""
    pic_names = []
    suffixes = []
    for name, value in options:
        if name in ("-p", "--path"):
            path = value
        if name in ("-n", "--name"):
            pic_names = value.split(' ')
        if name in ("-s", "--suffix"):
            suffixes = value.split(' ')

    for pic_name in pic_names:
        for suffix in suffixes:
            print("start to stitch %(pic_name)s%(suffix)s"%{'pic_name':pic_name, 'suffix':suffix})
            image_arr_arr = get_image_arr_arr(path, pic_name, suffix)
            image_arr = pic_stitch(image_arr_arr)
            put_image('stitch_result', pic_name + suffix, image_arr)
