# VESM3-VERK8

# Verkefnalýsing

- Þetta verkefni snýst um að nota pir hreyfiskynjara tengdan raspberry pi nano til þess að senda gögn í skýið í gegnum Adafruit IO og taka svo þær upplýsingar og kveikja á USB myndavél og AUX hátalara tengd við raspberry pi 4. Svo er notað OpenCV andlitsgreiningu til að spila persónulega mp3 hljóðskrá þegar pir hreyfiskynjarinn skynjar að það sé hreyfing.


# Efnalisti

- Raspbarry Pi 4
- Raspberry Pi Zero
- T-Cobbler
- PIR Sensor
- 1080P Logitech Usb Light
- Female to Female Wires

# Kóði

- [PIR Sensor Kóðinn](https://github.com/Tiago-MiguelM/VESM3-VERK3/blob/main/PiNano/LokaVerkefni8%20Motion%20Sensor.py)
- [Pi 4 Camera Kóðinn](https://github.com/Tiago-MiguelM/VESM3-VERK3/blob/main/Pi4/Basics.py)

# Hönnunarteikningar, Rafrásateikningar og tenglar

![image](https://github.com/Tiago-MiguelM/VESM3-VERK3/blob/main/circuit.png)

# Dagbók

## Tími 1
-
## Tími 2
-
## Tími 3
-
## Tími 4
-
## Tími 5
-
## Tími 6
-

# Vandamál

- Upphaflega hugmyndin var að nota microsoft azure en það kom upp vandamál að keyra azure þar sem við þurftum að breyta source code til að fá að virka.
- Við skiptum yfir í opencv þar sem við vorum að fá villur með að hlaða niður library sem heitir, opencv-python og dlib.
- Eftir að við náðum að download-a opencv-python var vesen að runna setup.py sem fylgir opencv sem hjálpar því að tengja cmake


# Heimildir

Hér eru nokkrar og bestar heimildir sem við fundum og notuðum til þess að reyna fá þetta til að virka enn því miður fengum við það ekki til að virka 

- https://www.youtube.com/watch?v=sz25xxF_AVE&t=312s
- https://www.youtube.com/watch?v=5yPeKQzCPdI
- https://www.geeksforgeeks.org/face-detection-using-python-and-opencv-with-webcam/
- https://docs.opencv.org/3.4/d6/d00/tutorial_py_root.html
