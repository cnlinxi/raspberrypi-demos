# raspberrypi-demos
Raspberry Pi: A computer for playing: https://www.raspberrypi.org/

## Resources

- Raspberry Pi 40 pins

![](https://raw.githubusercontent.com/cnlinxi/raspberrypi-demos/master/imgs/raspberry.png)
![](https://raw.githubusercontent.com/cnlinxi/raspberrypi-demos/master/imgs/rpi-pins-40-0.png)

- Raspberry Official Website: https://www.raspberrypi.org/

- Many Demos: https://www.hackster.io/

- Chinese Study Website: https://shumeipai.nxez.com/

## Project

- [send_ip_by_email](https://github.com/cnlinxi/raspberrypi-demos/blob/master/send_ip_by_email.py)

    This script can send the IP of raspberrypi by your E-mail. With this script, you can get the IP without screen.

- [keep_social_distance](https://github.com/cnlinxi/raspberrypi-demos/blob/master/keep_social_distance.py)

    You will get alarm if you keep too closer.

    - `sudo apt-get install python3-rpi.gpio`

    - `sudo pigpiod`

    the negetive pole of LED light -> GND

    the positive pole of LED light -> GPIO15
