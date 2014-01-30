Title: Integration of drawable objects and fortune hunter
Date: 2010-07-30T15:10:00
Slug: Blitzkev-integration-of-drawable-objects-and-fortune-hunter
Author: Blitzkev
Tags: legacy, foss@rit
Category: legacy
Summary: After finishing produce puzzle on Monday (the activity can be found here: ... 

After finishing produce puzzle on Monday (the activity can be found here:
[http://activities.sugarlabs.org/en-
US/sugar/addon/4322](http://activities.sugarlabs.org/en-US/sugar/addon/4322))
I have been working hard with Dave to get fortune hunter completely changed
over to using his drawable object and scene classes instead of the old surface
blits. Our 50+ git commits can be found here [http://git.fedorahosted.org/git/
?p=fortune_hunter.git;a=shortlog;h=refs/...](http://git.fedorahosted.org/git/?
p=fortune_hunter.git;a=shortlog;h=refs/heads/animationrework) . One bug we
had, where sometimes text would be hidden, was solved when we realized that
Dave was drawing everything in random order instead of the order it gets added
to the scene. Once he implements that correctly we should be set to continue
integrating fortune hunter. Another day or two of hard work and hopefully
we'll see a new version of the game engine that incorporates the animation
teams research!

