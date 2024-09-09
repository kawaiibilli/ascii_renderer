import numpy as np
import cv2
import os
import sys

def render(ascii_img, char_size):
    out_frame = np.zeros((len(ascii_img)*char_size, len(ascii_img[0])*char_size), dtype=np.uint8)
    for col in range(len(ascii_img)):
        for row in range(len(ascii_img[0])):
            out_frame = cv2.putText(out_frame, ascii_img[col][row], org=(col*char_size, row*char_size+char_size-1), font=cv2.FONT_HERSHEY_SIMPLEX, fontScale=char_size, color=(255,255,255), thickness=2)
    cv2.imwrite("ascii_output.jpg", out_frame)

def convert(img_name, char_size=8):
    img = cv2.imread(img_name)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    smol_img = cv2.resize(img, (img.shape[1]//char_size, img.shape[0]//char_size))
    ascii_img = [[' ']*smol_img.shape[1]]*smol_img.shape[0]
    print("smol_img shape : ", smol_img.shape)
    print("ascii_img shape : ", len(ascii_img), ", ", len(ascii_img[0]))
    ascii_lumi_map = [' ', '.', ':', 'c', 'o', 'P', '0', '?', '@', '█']
    
    for col in range(smol_img.shape[0]):
        for row in range(smol_img.shape[1]):
            val = int(smol_img[row][col]*len(ascii_lumi_map))//len(ascii_lumi_map)
            ascii_img[col][row] = ascii_lumi_map[val]
    render(ascii_img, char_size)
if __name__ == "__main__":
    img_name = sys.argv[1]
    char_size = int(sys.argv[2])
    convert(img_name, char_size)
