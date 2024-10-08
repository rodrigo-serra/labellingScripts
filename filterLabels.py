#!/usr/bin/env python3

from PIL import Image
import cv2
import os, json, sys, shutil
import numpy as np
from scipy.spatial import ConvexHull


def fileExists(path, error_phrase):
    if not os.path.exists(path):
        print(error_phrase)
        exit(1)



def findFilesInDir(path_to_dir, extension):
    files = []
    for file in os.listdir(path_to_dir):
        if file.endswith(extension):
            files.append(file)

    return files


def main():
    if len(sys.argv) < 4:
        print("There are missing input arguments!")
        exit(1)

    path_to_labels = sys.argv[1]
    filtered_imgs_path = sys.argv[2]
    num_of_imgs_to_copy = int(sys.argv[3])
    
    fileExists(path_to_labels, 'The path to the labels is not correct!')
    fileExists(filtered_imgs_path, 'The path to the new filtered imgs is not correct!')

    rgb_imgs = findFilesInDir(path_to_labels, '.jpg')
    labels = findFilesInDir(path_to_labels, '.json')

    new_filtered_imgs_dir = filtered_imgs_path + '/filtered_imgs/'
    if not os.path.exists(new_filtered_imgs_dir):
        os.makedirs(new_filtered_imgs_dir)

    for img in rgb_imgs:
        img_name = img.split(".")[0]
        img_num = int(img_name.split("_")[1])
        if img_num < num_of_imgs_to_copy:
            shutil.copyfile(path_to_labels + "/" + img, new_filtered_imgs_dir + "/" + img)
            shutil.copyfile(path_to_labels + "/" + img_name + ".json", new_filtered_imgs_dir + "/" + img_name + ".json")

    

if __name__ == "__main__":
    main()