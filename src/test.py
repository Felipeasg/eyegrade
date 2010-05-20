import pygame
import Image
from pygame.locals import *
import sys

import opencv
#this is important for capturing/displaying images
from opencv import highgui 
import imageproc

camera = imageproc.init_camera(1)

def get_image():
    im_raw = imageproc.capture(camera, True)
    im_proc = imageproc.pre_process(im_raw)
    return im_raw, im_proc

def save_image(im):
    highgui.cvSaveImage("/tmp/test.png", im)

fps = 8.0
pygame.init()
window = pygame.display.set_mode((640,480))
pygame.display.set_caption("WebCam Demo")
screen = pygame.display.get_surface()

while True:
    im_raw, im_proc = get_image()
#    im = imageproc.gray_ipl_to_rgb_pil(im_proc)
    imageproc.draw_lines(im_raw, im_proc, [[4,10],[4,10]], True)
#    imageproc.detect_lines(im_proc)
    im = opencv.adaptors.Ipl2PIL(im_raw)

    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            sys.exit(0)
        elif event.type == KEYDOWN:
            save_image(im_proc)
    pg_img = pygame.image.frombuffer(im.tostring(), im.size, im.mode)
    screen.blit(pg_img, (0,0))
    pygame.display.flip()
    pygame.time.delay(int(1000 * 1.0/fps))
