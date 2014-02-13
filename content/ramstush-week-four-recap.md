Title: Week Four Recap!!!!
Date: 2013-06-24T10:34:00
Slug: ramstush-week-four-recap
Author: ramstush
Tags: legacy, foss@rit
Category: legacy
URL: articles/ramstush/week-four-recap.html
save_as: articles/ramstush/week-four-recap.html
Summary: This week was another long haul on the road to research. My goal for the whole week was to figure out how to get our activity, Lemonade Stand, to create a journal entry. Since I did know anything regarding the journal, I spent the majority of the week learning how the OLPC journal worked and what I needed to change or implement into our activity that would make it work.  I started by using my most valuable resource, #sugar , and learned that the journal uses datastore to make its entries. [This  ... 

This week was another long haul on the road to research. My goal for the whole
week was to figure out how to get our activity, Lemonade Stand, to create a
journal entry. Since I did know anything regarding the journal, I spent the
majority of the week learning how the OLPC journal worked and what I needed to
change or implement into our activity that would make it work.

I started by using my most valuable resource, #sugar , and learned that the
journal uses datastore to make its entries. [This
website](http://wiki.laptop.org/go/Sugar.datastore.datastore) helped me
understand what a datastore is in a nutshell. A datastore, in my
understanding, is simply a place where datastore objects are stored. Its a
database. The way the process works, is that an activity makes a datastore
object with some information. This object is then sent to the sugar datastore
where it rests. The journal then grabs that object, takes the information it
needs and creates the entry.

After some more powwowing with #sugar, I found out that the activity doesn't
need to implicitly create a datastore object because the journal can make
entries with just metadata it shaves off of the activity that was run. This
information saved me a ton of trouble.

I tested this theory with the activity that I made in my Humanitarian Free and
Open Source Software and found that the journal did indeed make an entry. I
then tested Lemonade Stand, and found that it didn't make an entry. Over the
next three day's I committed myself to finding out why SkyTime worked and
Lemonade Stand didn't.

Finally I came in contact with previous surf member who designed the Fortune
Engine (the game engine that Lemonade Stand runs on) and shot him an email,
[Jlew's Open Source blog](http://blog.jlewopensource.com/). He wrote back
within the day and told me that there was an argument in the class params that
set create_jobject = FALSE. I went in, found the agruement, changed it to
TRUE, and it automagically worked. I believe it's astounding that something so
simple was so hard to find because of my lack of information regarding a
certain topic. THANK GOODNESS FOR KIND PEOPLE! If anyone who reads this blog
is having trouble with OLPC or the XO's or anything SugarLabs related, I urge
you to go to [webchat at freenode.net](http://webchat.freenode.net/) make a
nickname, join the room #sugar, and ask to your hearts content.

