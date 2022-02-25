from gpiozero import MotionSensor
import time
from time import sleep
from Adafruit_IO import Client, Feed, RequestError

ADAFRUIT_IO_KEY = 'aio_dNRN90iTs1EQ0M5lFwg6gVyXuR8L'
ADAFRUIT_IO_USERNAME = 'FinnurGauti'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try:
    digital = aio.feeds('digital')

except RequestError:
    feed = Feed(name="digital")
    digital = aio.create_feed(feed)

pir = MotionSensor(4)
motion_current = 0


print("Starting up..")
while True:

    if not pir.value:
        motion_current = 0

    else:
        motion_current = 1

    print('Motion -> ', motion_current)
    aio.send(digital.key, motion_current)
    time.sleep(1)
    motion_current = 0
