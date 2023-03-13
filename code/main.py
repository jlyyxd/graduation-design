# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

import cv2

root_path = "D:\\szu\\GraduationDesign\\data\\data\\HCMS\\train\\label"

def get_color(type):
    if type == 0:
        a, b, c = 0, 0, 0
    elif type == 1:
        a, b, c = 139, 0, 0
    elif type == 2:
        a, b, c = 255, 255, 0
    elif type == 3:
        a, b, c = 0, 139, 139
    elif type == 4:
        a, b, c = 255, 0, 0
    elif type == 5:
        a, b, c = 0, 0, 205
    elif type == 6:
        a, b, c = 0, 255, 0
    elif type == 7:
        a, b, c = 148, 0, 211
    elif type == 8:
        a, b, c = 255, 165, 0
    return a, b, c

def decode(file_path):
    new_file = file_path.split(".")
    new_file[0] = new_file[0] + "_color."
    new_file_path = new_file[0] + new_file[1]
    print(new_file_path)
    img = cv2.imread(file_path)
    for items in img:
        for item in items:
            a, b, c = get_color(item[0])
            item[0] = a
            item[1] = b
            item[2] = c

    # for items in img:
    #     for item in items:
    #         if item[0] > 8 or item[1] > 8 or item[2] >8:
    #             print("yes!!!!")
    #             break
    cv2.imwrite(new_file_path,img)
    return img

def decode_all(dir_path):
    list = os.listdir(dir_path)
    for item in list:
        item_path = os.path.join(dir_path, item)
        decode(item_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    decode_all(root_path)
    # file = "D:\\szu\\GraduationDesign\\data\\data\\HCMS\\train\\label\\hc10_spectralis_macula_v1_s1_R_1_1.png"
    # file = "D:\\szu\\GraduationDesign\\data\\data\\HCMS\\train\\label\\hc10_spectralis_macula_v1_s1_R_1_0.png"
    # img = decode(file)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
