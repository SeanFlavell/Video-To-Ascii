import cv2
import numpy as np
import time
ASCII_CHARACTERS = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]



# Lowers the resolution of the frame and changes it to grayscale.
# The brightness of the frames pixels are used to select a character and put it into the full frame.
def convert_frame(frame):

    frame_resized = cv2.resize(frame, (0, 0), fx = .12, fy = .12)
    frame_grayscale = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)

    frame_ascii = ""
    for row in frame_grayscale:
        for pixel_value in row:
            #print(pixel_value)
            asciiCharIndex = int(pixel_value / (256 / len(ASCII_CHARACTERS)))
            frame_ascii += ASCII_CHARACTERS[asciiCharIndex]
        frame_ascii += "\n"

    return frame_ascii
            
# Plays the video on the command line
def play_video():

    video = cv2.VideoCapture(r".\videofile.mp4")
    if not video.isOpened():
        print("video didnt open")
        return

    while True:
        success, frame = video.read()
        if not success:
            break
        asciiFrame = convert_frame(frame)
        print("\033[H" + asciiFrame)
        time.sleep(0.01667)
    

play_video()
        