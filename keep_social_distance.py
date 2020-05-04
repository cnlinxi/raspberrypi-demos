import time
import RPi.GPIO as GPIO
import pigpio

pi = pigpio.pi()
GPIO.setmode(GPIO.BOARD)
trig = 16
echo = 18
light = 15
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(light, GPIO.OUT)


def calc_distance():
    GPIO.output(trig, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(trig, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig, GPIO.LOW)

    start = time.time()
    stop = time.time()

    while GPIO.input(echo) == 0:
        start = time.time()

    while GPIO.input(echo) == 1:
        stop = time.time()

    duration = stop - start

    distance = 34300 / 2 * duration

    # if distance < 3400:
    # print("Distance = %.2f" % distance)
    return distance


print('The system calibrating...')
i = 0
val = 0
while i < 20:
    val = val + calc_distance()
    i = i + 1
    # print(i)
val = val / 20.
print('Average value: %.2f' % val)

try:
    while True:
        dist = calc_distance()
        print('distance: {} cm'.format(dist))
        if dist < 100:
            GPIO.output(light, True)
        else:
            GPIO.output(light, False)
        time.sleep(2)
finally:
    GPIO.cleanup()
