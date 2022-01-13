import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    print("running")
    time.sleep(2)
    camera.capture('newphoto.jpg')
    print("photo complete")
