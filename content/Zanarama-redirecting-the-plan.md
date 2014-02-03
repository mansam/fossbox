Title: Redirecting the Plan
Date: 2013-06-22T01:09:00
Slug: Zanarama-redirecting-the-plan
Author: Zanarama
Tags: legacy, foss@rit
Category: legacy
Summary: This week started off a little bumpy with a power outage that lasted a few hours and then a freak thunder/hail storm on Monday. On Wednesday the boat (a server the FOSSBox uses) went down Wednesday, slowing down everything and taking down FossBot. Finally, after a series of issues with Glade, we have shelved the GUI for now and have decided to instead work on producing some quality videos to send to Red Hat.  As a part of these videos I want to highlight the work of Red Hat employees by making t ... 

This week started off a little bumpy with a power outage that lasted a few
hours and then a freak thunder/hail storm on Monday. On Wednesday the boat (a
server the FOSSBox uses) went down Wednesday, slowing down everything and
taking down FossBot. Finally, after a series of issues with Glade, we have
shelved the GUI for now and have decided to instead work on producing some
quality videos to send to Red Hat.

As a part of these videos I want to highlight the work of Red Hat employees by
making there avatars different than all of the other contributors. However,
Gource handles custom avatars in a bit of a funky way. Each person that needs
a custom avatar must have a copy of the picture saved in a directory with
their full name, as it is in the logs, as the file name. I created a proof of
concept image by manually going through a log and creating a new file for each
user with a Red Hat email. A screen shot of that is attached, and I think it
looks pretty nice. However, that is a cumbersome process and isn't practical
for every project, especially as we get into projects with a lot of
contributors. This week I started creating a program that will parse a custom
log and create these files for every user with a particular email host in a
file. Right now I am running into some issues with Unicode characters in some
names, but I will get further into this when problems are solved.

Another exciting aspect of this week is that I (finally) got my Red Hat laptop
unlocked! Having it unlocked will mean that we can render videos on that
laptop while I am working on my own. It should save me from having down time
and should increase the number of videos we can render. This also means I can
now access my Red Hat email, which should save some communication headaches.

I have high hopes for the week to come. I am going to get the file creator
working and start rendering some videos!

AttachmentSize

[Gource Custom Avatars](http://foss.rit.edu/files/Screenshot from 2013-06-19
16:53:24.png)

285.91 KB

