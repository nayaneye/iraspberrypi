import picamera
from time import sleep

def takePic():
    camera = picamera.PiCamera()
    try:
        camera.start_preview()
        sleep(5)
        camera.capture('image.jpg')
        camera.stop_preview()
    finally:
        camera.close()

if __name__ == '__main__':
    takePic()

