Title: Knowing the Unknowns
Date: 2013-06-20T11:25:00
Slug: ramstush-knowing-the-unknowns
Author: ramstush
Tags: legacy, foss@rit
Category: legacy
Summary: CODE SPELUNKING!!! Yesterday was a very dirty day digging through code. The ... 

CODE SPELUNKING!!! Yesterday was a very dirty day digging through code. The
entire day I was looking at two sugar activities.
[SkyTime](http://activities.sugarlabs.org/en-US/sugar/addon/4670) and
[Lemonade Stand](http://activities.sugarlabs.org/en-US/sugar/addon/4321).

The ticket assigned to me was to get Lemonade Stand to make an entry into the
journal. I used SkyTime as a parallel test case to see if something was
blocking the journal from accessing the activity or if I needed to add some
functionality to the activities to allow the journal to access the activities.

My journey began by pinging #sugar again to get some insight into what wasn't
working in our activities. They pointed me towards [The Sugar Datastore wiki p
age](http://wiki.sugarlabs.org/go/Development_Team/Almanac/sugar.datastore.dat
astore) which explains how the journal accesses the activity information and
makes an entry. After talking with the sugar team, they informed me that the
code which was in the wiki page manually made a datastore object for the
journal to access, but the journal doesn't need an actual file to make a
journal entry. The journal should be able to automatically make an entry just
by grabbing some metadata from the activity that has been running most
recently. Also, i learned that the journal doesn't make a new entry for each
time the activity is opened, it just updates a previous entry that has been
made in the journal. To make a completely new entry, you need to select "Start
New" under the palette after you hover over the activity. After learning this
valuable information, I decided to test each of the SkyTime and Lemonade Stand
activities on a sugar XO to see if the journal did, in fact, make automatic
entries. When I made a new Skytime entry, the journal lived up to it's
reputation and made an entry flawlessly. When I tried Lemonade Stand, it still
didn't work. After some digging, The FOSSbox suggested that I try a difference
activity that used the Fortune Game Engine as well. This activity was called
[Fortune Hunter ](http://activities.sugarlabs.org/en-US/sugar/addon/4272).
After testing this game and getting the same results as I did from lemonade
stand, I have concluded that Fortune Engine has something to do with the
erroneous journal entries. Today I will endeavor to dig through fortune engine
and add/delete the code that will make journal entries.

