Title: Every time you fix one problem, another crops up...
Date: 2010-07-29T11:46:00
Slug: DaveSilver-every-time-you-fix-one-problem-another-crops-up
Author: DaveSilver
Tags: legacy, foss@rit
Category: legacy
Summary: As you may be able to guess from my blog title I have been running into more ... 

As you may be able to guess from my blog title I have been running into more
issues while trying to integrate my stuff into Jlew and Blitzkev's engine.
Mainly we are having issues getting things to display because the entire
engine has not yet been ported over to the new system. This means that some
things are using our sprite and sprite group system while other things are
using the old blit and flip method. For some reason this is causing the stuff
to not display the same way every time we test and thus makes it very hard for
us to pin down the exact issues we are having.

On top of this we are also running into issues where the sprites and sprite
groups are slightly more complex than we originally believed. Because of this
we do not know exactly how some of it is working which is making it harder to
debug stuff.

Thankfully I can say that not everything is going badly. JT is in the process
of finishing the Complete Test and we are currently cleaning up a lot of the
code for the Drawable Objects and stuff. Because of the way we developed and
how we would add functionality as we needed it, we ended up having a lot of
old outdated code, and a lot of code that is not as efficient as it could be,
in our classes. This means that now we are going back and looking at all the
stuff we have made so far and figuring out what could be running more
efficiently or what needs to be removed entirely now.

Finally we are also starting our paper soon. Today I am writing the abstract
for the paper and hopefully by next week we will be a decent way through the
paper as a whole. It might take a little while to write but it should be the
easiest part of the project as a whole.

Well I have rambled for a while so I will go now. Have a good day.

