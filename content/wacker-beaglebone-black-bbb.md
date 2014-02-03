Title: BeagleBone Black (BBB)
Date: 2013-09-21T21:28:00
Slug: wacker-beaglebone-black-bbb
Author: wacker
Tags: legacy, foss@rit
Category: legacy
Summary: Today was [Software Freedom Day](http://softwarefreedomday.org/) and there was a lot of amazing talks and hacking going on! The project that I began with a fellow hacker and friend, Suzanne Reed, was a bot that will be used for dispensing beverages via SMS message to a BBB connected to some motors. I do not know much about the mechanical process, but I know I will be writing most of the software portion.  Our goal for today was to try and get some sort of response from a motor that we hocked up  ... 

Today was [Software Freedom Day](http://softwarefreedomday.org/) and there was
a lot of amazing talks and hacking going on! The project that I began with a
fellow hacker and friend, Suzanne Reed, was a bot that will be used for
dispensing beverages via SMS message to a BBB connected to some motors. I do
not know much about the mechanical process, but I know I will be writing most
of the software portion.

Our goal for today was to try and get some sort of response from a motor that
we hocked up to the BBB via basic motor controls using some simple python
code, but were unsuccessful. That's not to say that our entire day was
unsuccessful because it sure wasn't. I personally had no experience prior with
a BBB or anything similar like a [Raspberry Pi](http://www.raspberrypi.org/).
Regardless of my background with this kind of software, I was able to
successfully ssh into the BBB and install some packages that are required to
even being testing the motors required to dispense the beverages.

After a long period of searching how to simply ssh into the BBB, I had found
the answer! Assuming you already have the BBB plugged into your laptop or
desktop, you can ssh into the BBB by typing this command:

_ssh root@beaglebone.local_

You will then be prompted for a password, but you might ask, "How is there
already a password?" Funny thing, there isn't. You can simply bypass this by
hitting the enter key. You have now successfully ssh-ed into your BBB!

From here we installed some dependency packages that we needed to run the code
to control the motor. These commands include:

_su_

_opkg update_

_opkg install python python-modules python-pyserial python-numpy python-
setuptools python-misc python-pip python-distutils git_

_git clone git://github.com/adafruit/adafruit-beaglebone-io-python.git_

_/usr/bin/ntpdate -b -s -u pool.ntp.org_

_cd adafruit-beaglebone-io-python_

_python setup.py install_

_git clone git://github.com/petebachant/bb_pystepper.git_

_cd bb_pystepper_

Now that you have installed the correct packages and are in the
[bb_pystepper](https://github.com/petebachant/bb_pystepper) directory, it is
time to begin testing some code! You can run a simple test by entering these
commands:

_python_

_>>> from bb_pystepper import Stepper_

_>>> mystepper = Stepper()_

_>>> mystepper.rotate(180, 10)_

_>>> mystepper.angle_

_0.0_

This just shows that the stepper was properly loaded and adjusts the angle of
the motor properly as well. This was just step one to get our bot up and
running and there will be more posts later on as our progress continues!

