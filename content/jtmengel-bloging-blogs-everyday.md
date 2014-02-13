Title: Bloging blogs, everyday
Date: 2010-07-21T14:33:00
Slug: jtmengel-bloging-blogs-everyday
Author: jtmengel
Tags: legacy, foss@rit
Category: legacy
URL: articles/jtmengel/bloging-blogs-everyday.html
save_as: articles/jtmengel/bloging-blogs-everyday.html
Summary: Design was previously thought to be complete and implementation could begin, but wait! There's more!  We had previously moved on from dirty blitting content that we fully understood the subtleties therein, full of bravado and confidence that, as you will soon learn why, quickly evaporated. As our plans were attacked by rabid weasels.  I carefully chose this metaphor to perfectly illustrate where we are, or course.  So today was spent reviewing tutorials on Sprites; sprites are, in essence, surfa ... 

Design was previously thought to be complete and implementation could begin,
but wait! There's more!

We had previously moved on from dirty blitting content that we fully
understood the subtleties therein, full of bravado and confidence that, as you
will soon learn why, quickly evaporated. As our plans were attacked by rabid
weasels.

I carefully chose this metaphor to perfectly illustrate where we are, or
course.

So today was spent reviewing tutorials on Sprites; sprites are, in essence,
surfaces combined with their rectangles and other information, depending on
you the programmer since Sprite itself is pretty useless until you make your
own object which inherits Sprite.

What would we like to inherit Sprite, one might ask? Why, our Drawable Object
class (which conveniently already does inherit Sprite to support our animated
objects)!

So at this point we're getting comfortable inheriting and mutating Sprite into
something ideal for our environment, with our goals being:

Avoiding unnecessary calculations from drawing a pixel multiple times a draw
cycle due to overlapping 'dirty' images.

Changing Drawable Object and Dynamic Drawable Object to act as Sprites instead
of lists of images (simple surfaces are good to a point, but we decided that
we were reinventing the wheel where animation was concerned)

Do all of this with minimal changes to the preexisting game engine; we want to
add to the engine, not rethink the whole engine (but what can't be avoided,
can't be avoided)

The tutorial I followed for my initial "aha" moments can be found below!

[piman's Sprite Tutorial](http://www.sacredchao.net/~piman/writing/sprite-
tutorial.shtml)

Edit: Naturally minutes after I make a blog post, something I should mention
happens...

After creeping around #pygame I actually got to speak with piman a little
regarding which libraries are helpful for implementing rendered SVG's into my
master test class. It's a small series of tubes, after all...

(Oh and it seems that my options for SVG rendering are a 'Squirtle' Pygame
extension, 'Cairo' a library for python (that is undesirable for animating, I
hear) and other options I would have to google intensively just to understand
well enough to describe to my fine audience).

Until next time!

