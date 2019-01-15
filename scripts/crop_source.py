from PIL import Image

base_dir = 'task/'
result_dir = 'trans_task/'
size = 200
coor_list = [0, 181, 363, 544]
for i in range(5):
    img = Image.open(base_dir + str(i) + '.jpg')
    for m in range(4):
        for n in range(4):
            left = coor_list[m]
            top = coor_list[n]
            right = left + size
            bottom = top + size
            crop_img = img.crop((left, top, right, bottom))
            crop_img.save(result_dir + str(i) + '_' + str(m) + '_' + str(n) + '.jpg')
