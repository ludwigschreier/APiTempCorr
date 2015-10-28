'''
Astro Pi Temperature Sensor Reading 
Raw import from https://www.raspberrypi.org/forums/viewtopic.php?t=111457&p=769672
Refer also to https://en.wikipedia.org/wiki/Relative_humidity
'''

from sense_hat import SenseHat
import time

sense = SenseHat()

while True :
    pressure = sense.get_pressure()
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    calctemp = 0.0071*temp*temp+0.86*temp-10.0
    calchum=humidity*(2.5-0.029*temp)
    print '%.0f %.1f %.0f' % (pressure, calctemp, calchum)
    time.sleep(5)
