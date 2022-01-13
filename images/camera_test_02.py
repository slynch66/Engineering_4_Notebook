import time
import picamera



with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768)
	camera.start_preview()
    	# Camera warm-up time
	print("running")
	camera.image_effect = 'oilpaint'
	time.sleep(2)
	camera.capture('imageeffect-oilpaint.jpg')
	print("oilpaint image complete")

	camera.start_preview()
	# Camera warm-up time
	print("running")
	camera.image_effect = 'gpen'
	time.sleep(2)
	camera.capture('imageeffect-gpen.jpg')
	print("gpen image complete")
	
	camera.start_preview()
	# Camera warm-up time
	print("running")
	camera.image_effect = 'negative'
	time.sleep(2)
	camera.capture('imageeffect-negative.jpg')
	print("negative image complete")

	camera.start_preview()
	# Camera warm-up time
	print("running")
	camera.image_effect = 'none'
	time.sleep(2)
	camera.capture('imageeffect-none.jpg')
	print("no-effect image complete")
	
	camera.start_preview()
	# Camera warm-up time
	print("running")
	camera.image_effect = 'saturation'
	time.sleep(2)
	camera.capture('imageeffect-saturation.jpg')
	print("saturation image complete - all images complete")
