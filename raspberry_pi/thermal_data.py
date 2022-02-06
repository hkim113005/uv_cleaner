import time,board,busio
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt
import tensorflow as tf
import glob
import cv2
from scipy import ndimage
from PIL import Image
from datetime import datetime

i2c = busio.I2C(board.SCL, board.SDA, frequency=1000000) # setup I2C

mlx_1 = adafruit_mlx90640.MLX90640(i2c, address=0x32) # begin MLX90640 with I2C comm
mlx_1.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_32_HZ # set refresh rate
mlx_2 = adafruit_mlx90640.MLX90640(i2c, address=0x33)
mlx_2.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_32_HZ

mlx_shape = (24,32) # mlx90640 shape

#model = tf.keras.models.load_model('//home/pi/models/people_detect')
frame_1 = np.zeros(mlx_shape[0]*mlx_shape[1]) # 768 pts
frame_2 = np.zeros(mlx_shape[0]*mlx_shape[1])

model = tf.keras.models.load_model('//home/pi/models/')

cnt = 0

def predict(idx):
    mlx_1.getFrame(frame_1)
    new_frame_1 = np.rot90(np.fliplr(np.reshape(frame_1,(24,32))))
    new_frame_1 = np.reshape(new_frame_1, (1,32,24,1))
    predicted_1 = list(model.predict(new_frame_1))
    
    mlx_2.getFrame(frame_2)
    new_frame_2 = np.rot90(np.fliplr(np.reshape(frame_2,(24,32))))
    new_frame_2 = np.reshape(new_frame_2, (1,32,24,1))
    predicted_2 = list(model.predict(new_frame_2))
    
    print(predicted_1, predicted_2)
    
    if predicted_1[0][0] < predicted_1[0][1] or predicted_2[0][0] < predicted_2[0][1]:
        print(f'{idx}: positive')
    else:
        print(f'{idx}: negative')

def capture():
    while True:
        mlx_1.getFrame(frame_1)
        new_frame = np.rot90(np.fliplr(np.reshape(frame_1,(24,32))))
        text_filename = datetime.now().strftime('//home/pi/datasets/texts/%Y-%m-%d_%H-%M-%S_0.txt')
        image_filename = datetime.now().strftime('//home/pi/datasets/images/%Y-%m-%d_%H-%M-%S_0.png')
        
        np.savetxt(text_filename, new_frame, delimiter=',')

        new_frame = (((new_frame - new_frame.min()) / (new_frame.max() - new_frame.min())) * 255.9).astype(np.uint8)
        img = Image.fromarray(new_frame)
        img.save(image_filename)
        
        cnt = cnt + 1
        print(cnt)
        
        time.sleep(30)
            
idx = 0
while True:
    try:
        start = time.time()
        predict(idx)
        idx += 1
        end = time.time()
        fps = 1 / (end-start)
        print(fps)
    except:
        print("error!")