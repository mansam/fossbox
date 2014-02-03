Title: Things Keep Getting Complicated...
Date: 2010-07-21T08:15:00
Slug: DaveSilver-things-keep-getting-complicated
Author: DaveSilver
Tags: legacy, foss@rit
Category: legacy
Summary: So yesterday was primarily successful however towards the end of the end we started running into some problems. Basically as we got to the end of the day we found that some of the methods we were using, or planning on using, were not going to be as successful as we thought. You see, we intended to use a "dirty" update method. This means that instead of updating the whole screen every frame, it only updates the areas covered by objects that actually need to be updated. To do this, we would simply ... 

So yesterday was primarily successful however towards the end of the end we
started running into some problems. Basically as we got to the end of the day
we found that some of the methods we were using, or planning on using, were
not going to be as successful as we thought. You see, we intended to use a
"dirty" update method. This means that instead of updating the whole screen
every frame, it only updates the areas covered by objects that actually need
to be updated. To do this, we would simply create a list of the rectangle
objects associated with what needs to be updated. The problem, however, comes
up when you have overlapping rectangles. This means that if you send in two
rectangles that have overlapping areas, it will update that area twice.
Normally this is not too big of a deal however it can become a big deal when
you have situations where one object is fully enclosed inside another and both
are being updated, or when there is a large amount of overlap between two
objects. Today we are going to attempt to create a viable solution for this
problem. Hopefully we will be able to. Talk to you next time.

