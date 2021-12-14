import time
import Adafruit_LSM303
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
lsm303 = Adafruit_LSM303.LSM303()
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# First define some constants to allow easy resizing of shapes.
padding = 2
top = padding
bottom = height-padding
x = padding
# Move left to right keeping track of the current x position for drawing shx = padding

while True:
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    
    font = ImageFont.load_default()
    
    print(f"Accel X={accel_x}, Accel Y={accel_y}, Accel Z={accel_z}, Mag X={mag_x}, Mag Y={mag_y}, Mag Z={mag_z}")
    draw.text((x, top),  f"ACCEL DATA:", font=font, fill=255)
    draw.text((x, top+15), f"Accel X={accel_x}", font=font, fill=255)
    draw.text((x, top+30), f"Accel Y={accel_y}", font=font, fill=255)
    draw.text((x, top+45), f"Accel Z={accel_z}", font=font, fill=255)
    
    # Wait half a second and repeat.
    time.sleep(0.5)
