Title: Rotation Problems...
Date: 2010-07-12T13:21:00
Slug: DaveSilver-rotation-problems
Author: DaveSilver
Tags: legacy, foss@rit
Category: legacy
Summary: Today has been pretty successful but there has been one big issue. So basically I have been working on getting all of the basic functionality of our animated objects in place so testing can be run to make sure they work. I finished that up, started testing, and found a huge problem with the way I have been rotating images. So basically when an image is rotated by a number of degrees that is not divisible by 90, such as 10 or 15 or 45, you are creating an image that is not a square or a rectangle ... 

Today has been pretty successful but there has been one big issue. So
basically I have been working on getting all of the basic functionality of our
animated objects in place so testing can be run to make sure they work. I
finished that up, started testing, and found a huge problem with the way I
have been rotating images. So basically when an image is rotated by a number
of degrees that is not divisible by 90, such as 10 or 15 or 45, you are
creating an image that is not a square or a rectangle. To account for this,
the image editing program you are using or, in this case, the code itself,
will pad the image with white-space to make them completely square or
rectangle.
([This](http://farm5.static.flickr.com/4114/4787023853_81604d66b5_t.jpg)
represents an image before it is rotated at all.
[This](http://farm5.static.flickr.com/4074/4787023883_093dedb928_m.jpg) image
represents an image after a 45 degree rotation with the Green part being the
original and the Black part being the part that was added to make the image
square.) Now this situation is annoying at first but becomes incredibly
problematic if you are in a situation where an image is being rotated a small
amount over and over like you might have in a game.
([This](http://farm5.static.flickr.com/4081/4787654864_052367ce26_m.jpg) image
represents this situation. We started with a the green image and then rotated
it 9 times by 10 degrees each time. Each different color area represents a new
rotation and the space that was added to the image each time. The lighter the
color is, the earlier the rotation was. You can see that an image can quickly
become humongous from just a few rotations.)

The solution to this problem is actually pretty simple. This problem, as I
said earlier, really only comes up if you take the same image and repeatedly
rotate it over and over and over. So instead we will have two image arrays
associated with each animated object. the first image array is the original
array that keeps the original images at their original sizes and rotations for
reference. Then we have the display array which has copies of the images at
the sizes and rotations they are currently needed. Every time the images are
scaled or rotated or both, the system remakes the display array by re-rotating
the images and rescaling them. This is the best solution we could come up with
and is probably the one we will stick with if we do not find any major
slowdown comes about from using it.

Talk to you guys next time and have a great day.

