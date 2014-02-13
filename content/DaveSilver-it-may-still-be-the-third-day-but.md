Title: It may still be the third day but...
Date: 2010-06-09T11:40:00
Slug: DaveSilver-it-may-still-be-the-third-day-but
Author: DaveSilver
Tags: legacy, foss@rit
Category: legacy
URL: articles/DaveSilver/it-may-still-be-the-third-day-but.html
save_as: articles/DaveSilver/it-may-still-be-the-third-day-but.html
Summary: So it is still the third day but I thought the blog deserved an update for what's going on right now. Basically JT and I have run into a problem with our testing. Our original plan for testing was to have an image on the screen that was moving across the screen in a specific pattern and was constantly cycling between a set of images. Then once the test program was up and running we would then use the terminal program, 'htop' to record the CPU cycles and memory use. The goal here was to determine ... 

So it is still the third day but I thought the blog deserved an update for
what's going on right now. Basically JT and I have run into a problem with our
testing. Our original plan for testing was to have an image on the screen that
was moving across the screen in a specific pattern and was constantly cycling
between a set of images. Then once the test program was up and running we
would then use the terminal program, 'htop' to record the CPU cycles and
memory use. The goal here was to determine how much memory was being used with
each different file format. In theory some file formats would have used more
memory then others and we would have been able to tell which is ideal simply
from this test. In reality when we used 'htop' we found that every test, no
matter what the file sizes were for the different images, said we were using
100% of the CPU cycles. On top of that, we also found that larger files would
show up as using less memory. Obviously this method of recording data was not
going to suffice.

To solve our problem we are now retooling the program so that it prints out
the frames per second on screen. Our goal here is to create a system of data
recording that will be accurate enough to give us some idea of what's going
on. Hopefully this will work, but we will keep the blog updated on how things
progress.

