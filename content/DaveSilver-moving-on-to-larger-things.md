Title: Moving On to Larger Things...
Date: 2010-07-20T13:50:00
Slug: DaveSilver-moving-on-to-larger-things
Author: DaveSilver
Tags: legacy, foss@rit
Category: legacy
URL: articles/DaveSilver/moving-on-to-larger-things.html
save_as: articles/DaveSilver/moving-on-to-larger-things.html
Summary: So yesterday we finally implemented rotation correctly and it looks great. Once we had that down we also implemented Rendered Transparency so that users could make more complex looking images, and the convert function so that images can be optimized more easily. After we got that working we moved on to determining how we would implement the animation classes into the larger Game Engine.  We determined that it would be easiest to take the needed functionality of the Scene class and just make it p ... 

So yesterday we finally implemented rotation correctly and it looks great.
Once we had that down we also implemented Rendered Transparency so that users
could make more complex looking images, and the convert function so that
images can be optimized more easily. After we got that working we moved on to
determining how we would implement the animation classes into the larger Game
Engine.

We determined that it would be easiest to take the needed functionality of the
Scene class and just make it part of the engine, rather than making it an
entirely separate class. Then we would also take DO and DDO and integrate them
into all of the other classes that use animated functionality. That's what
we've been doing today and will be doing for the next couple days.

So far things have been going pretty smoothly and hopefully they stay that
way. Other than that not much is going on except that tomorrow we have to work
in the Faux-Box rather than the FOSS-BOX. Well I will talk to you next time,
have a good day.

