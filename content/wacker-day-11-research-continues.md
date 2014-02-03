Title: Day 11: Research Continues
Date: 2013-06-13T10:11:00
Slug: wacker-day-11-research-continues
Author: wacker
Tags: legacy, foss@rit
Category: legacy
Summary: We did a lot more research into Open Badges, School Servers, and the XO journal. We cracked a lot more unanswer questions about the journal and how [Lemonade Stand](http://wiki.sugarlabs.org/go/Lemonade_Stand) can write and talk to the journal.  On the side, I worked on implementing Lemonade Stand into the new version of the XO. It may have taken me almost all day, but it was a huge success! With Lemonade Stand working on the XO, we are now able to start hacking away at the game and see how it l ... 

We did a lot more research into Open Badges, School Servers, and the XO
journal. We cracked a lot more unanswer questions about the journal and how
[Lemonade Stand](http://wiki.sugarlabs.org/go/Lemonade_Stand) can write and
talk to the journal.

On the side, I worked on implementing Lemonade Stand into the new version of
the XO. It may have taken me almost all day, but it was a huge success! With
Lemonade Stand working on the XO, we are now able to start hacking away at the
game and see how it looks on the XO rather than my laptop. I also figured out
how to implement and use new fonts on the XO because I had an issue where the
fonts would not display on the XO but would on my laptop.

**Solution for getting Lemonade Stand on the version of sugar:** It turns out that in the _activity.info_ file, service_name is deprecated and should now use _bundle_id_ instead.

**Code:** _bundle_id = org.laptop.community.lemonade_

**Solution for getting new fonts in Lemonade Stand:** When the game starts, it takes command arguments from the _activity.py_ file. In the command line arguments, this is where you add the font name and sizes to be initialized wihtin the game.

**Code:** _argv=['/bin/sh','-c', 'python %s/LemonadeStand.py --width=1200 --height=875 --font=36 --shopFont=52 --shopNumFont=72' % bundle_path]_

