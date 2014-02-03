Title: Thurs time's the charm...
Date: 2010-07-22T13:40:00
Slug: DaveSilver-thurs-times-the-charm
Author: DaveSilver
Tags: legacy, foss@rit
Category: legacy
Summary: So today we worked on getting our system working so that we would not have to refresh everything on screen every single frame. We were pretty successful.  The problem we were having the past few days was essentially that, since we were using images, there was no built in functionality for having things move in layers. This meant that if you have an object moving on screen and a background image under it, the image will slowly start overwriting the background image until you re-write all of the b ... 

So today we worked on getting our system working so that we would not have to
refresh everything on screen every single frame. We were pretty successful.

The problem we were having the past few days was essentially that, since we
were using images, there was no built in functionality for having things move
in layers. This meant that if you have an object moving on screen and a
background image under it, the image will slowly start overwriting the
background image until you re-write all of the background image's data to the
screen yourself. So we had to find a way to prevent the background image from
being overwritten like that.

To solve the problem we started using Sprites. Sprites have a built in feature
called groups which allow you to do layering and more complex image
manipulation and such. This means that once we figured out how to use Sprites
and groups we would not have to worry about this problem anymore. So now all
we have to do is take all of the existing functionality we created for
Drawable Objects and adapt it to work with Sprites. I guess I will talk to you
next time. See ya.

