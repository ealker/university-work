import cv2
import numpy as np 
import matplotlib.pyplot as plt 

print("Worksheet 01")

def black_image():
    black_img = np.zeros((40,50))
    cv2.imwrite("black.png", black_img)
    
def white_image(): 
    white_img = 255 * np.ones((40,50))
    cv2.imwrite("white.png", white_img)

def rgb_gray_image():
    gray_img = 127 * np.ones((40,50,3))
    cv2.imwrite("grey.png", gray_img)

def yellow_image():
    r = 255 * np.ones((40,50))
    g = 255 * np.ones((40,50))
    b = np.zeros((40,50 ))
    i = cv2.merge((b,g,r))
    cv2.imwrite("yellow.png", i)
    
def save_red(): 
    img = cv2.imread("cam.png")
    b,g,r = cv2.split (img) 
    cv2.imwrite("cam_red.png", r)
    
def color_to_grayscale():
    img = cv2.imread("cam.png") 
    b, g, r = cv2.split(img)
    
    new_b = 0.114 * b 
    new_g = 0.587 * g 
    new_r = 0.299 * r 
    
    blue = new_b.astype(np.uint8)
    green = new_g.astype(np.uint8)
    red = new_r.astype(np.uint8)
    
    img2 = cv2.merge((blue, green, red))
    
    gray_img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("test", gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    mB, mG, mR, mA = cv2.mean(gray_img)
    print("Average for image: ", mB, mG, mR, mA)
    
def show_with_plt(): 
    img = cv2.imread("cam.png", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("Cam Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    img_for_plt = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB) 
    cv2.imshow("Image for PLT",  img_for_plt)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    plt.imshow(img_for_plt)

def merge_two_in_one(): 
    img = cv2.imread("cam.png")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    merged_img = np.hstack((img, gray_img))
    
    cv2.imwrite("both.png", merged_img)
    
#black_image()
#white_image()
#rgb_gray_image()
#yellow_image()
#save_red()
#color_to_grayscale()
#show_with_plt()
#merge_two_in_one()
#https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
