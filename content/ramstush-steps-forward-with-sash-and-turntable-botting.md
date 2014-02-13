Title: Steps forward with Sash and turntable botting
Date: 2013-07-18T11:14:00
Slug: ramstush-steps-forward-with-sash-and-turntable-botting
Author: ramstush
Tags: legacy, foss@rit
Category: legacy
URL: articles/ramstush/steps-forward-with-sash-and-turntable-botting.html
save_as: articles/ramstush/steps-forward-with-sash-and-turntable-botting.html
Summary: Yesterday was a slow day of research and development. As usual, it took most of the day to finally get to the interesting bits. SO, lets start where the fun begins. First, a small revelation regarding sugar activities. If you're programming a prospective activity, write the program first in python (so that it works on you're PC, box, etc..). AFTER your activity works just the way you want it to work on your machine, port it over to sugar by importing your sugar library and placing all of your co ... 

Yesterday was a slow day of research and development. As usual, it took most
of the day to finally get to the interesting bits. SO, lets start where the
fun begins. First, a small revelation regarding sugar activities. If you're
programming a prospective activity, write the program first in python (so that
it works on you're PC, box, etc..). AFTER your activity works just the way you
want it to work on your machine, port it over to sugar by importing your sugar
library and placing all of your code within a class that is defined within
your activity.info file. I made a sugar activity quick start that has an
extremely detailed tutorial of how to make a sugar activity. You can find that
repository [SAQS github repository](https://github.com/FOSSRIT/SAQS-sugar-
activity-quick-start-). Second on the list of cool happenings is the
continuation of a python based Turntable.fm bot that helps the owner and mods
of a turntable.fm room control tracks, queues, awesomes, etc.. If you don't
know what Turntable is, just search Turntable.fm and you should be able to
find it! Its a free online social music player that encourages social
interaction through community music collaboration. Check it out!!! Currently,
Decause and I are going to jump into bot land and see if we can make a
feature-full tt_bot to play around with! Keep tuned for the github release!

