Title: BeagleBone Black and bb_pystepper + a Bugfix
Date: 2013-09-23T13:40:00
Slug: Zanarama-beaglebone-black-and-bbpystepper--a-bugfix
Author: Zanarama
Tags: legacy, foss@rit
Category: legacy
Summary: So during Software Freedom day I began hacking on the [BeagleBone Black](http://beagleboard.org/Products/BeagleBone%20Black) and a small stepper motor. Are only goal was to gain familiarity with the BeagleBone by controlling the stepper motor with Python code that is FOSS.  For the hardware setup I utilized the [28BYJ-48 Stepper Motor](http://robocraft.ru/files/datasheet/28BYJ-48.pdf), the [L293D Driver Chip](http://www.datasheets360.com/pdf/624709677179081801?comp=3509), a breadboard, some wire ... 

So during Software Freedom day I began hacking on the [BeagleBone
Black](http://beagleboard.org/Products/BeagleBone%20Black) and a small stepper
motor. Are only goal was to gain familiarity with the BeagleBone by
controlling the stepper motor with Python code that is FOSS.

For the hardware setup I utilized the [28BYJ-48 Stepper
Motor](http://robocraft.ru/files/datasheet/28BYJ-48.pdf), the [L293D Driver
Chip](http://www.datasheets360.com/pdf/624709677179081801?comp=3509), a
breadboard, some wires, and of course the BeagleBone Black. I had both the
chip and motor from a kit I bought from AdaFruit, so I used [her guide to
wiring the board](http://learn.adafruit.com/adafruit-arduino-lesson-16
-stepper-motors/breadboard-layout) as my breadboard setup.

When looking for code to run the stepper motor I came across [ this
blogpost](http://petebachant.me/stepper-motor-control-with-the-beaglebone-
black-and-python/) discussing almost exactly what I was trying to do.
Utilizing this code, [David](https://github.com/DaWacker) and I (but 99%
David) configured the BeagleBone so we could ssh in, and put the bb_pystepper
code on the BeagleBone, as well as the adafruit stepper library which was a
dependancy.

Unfortunately, when we attempted to run the code I discovered that motor only
vibrated, it didn't actual spin. We went to a lab and started testing outputs
with an o-scope and a mulitmeter to no avail. We even tried providing power
from another source to see if the BeagleBoard was having difficulty driving
enough current. Finally I started software debugging which is when I
discovered a little variable in the code called steps_per_rev.

This variable describes the number of steps the motor takes in a spin.
Currently, it was set to 2048.0, which was far too high for my motor.
Essentially, signals were being sent so quickly that the motor was able to
register the pulses. After a little bit of playing around we settled on 512
being a solid value. However, I was displeased that my testing required me to
actual change the hardcoded value. Instead, I moved the steps_per_rev as an
optional constructor argument, as well as moving the pins that drive the
motor. This is a sample of how the code runs now with my updates.

$ cd bb_pystepper

$ python

>>> from bb_pystepper import Stepper

>>> mystepper1 = Stepper() # Creates default stepper motor

>>> mystepper2 = Stepper(512.0) # Creates motor with 512 steps_per_rev

>>> mystepper3 = Stepper(256.0, ['P8_17', 'P8_18', 'P8_19', 'P8_20']) # Motor
with 256 steps per rev and different pin mappings

>>> mystepper1.rotate(180, 10) # Rotates stepper 1 180 degrees at 10 RPM

>>> # (will also rotate stepper2 because they are mapped to the same pin

>>> mystepper3.rotate(-180, 5) # Rotates stepper 3 back 180 degrees at 5 RPM

I am much happier with this version of the code because it allows for multiple
motors to be run independantly with different steps_per_rotation. It also
should make the selection of the correct steps_per_rotation a lot easier. I
still feel that the code could use some improvements for ease of use and
general configuring but I will go to that soon. The code also could use some
PEP8 fixes, but I am guessing that someone else in the class may want to
tackle that.

