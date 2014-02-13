Title: Journal in OLPC
Date: 2013-06-21T15:56:00
Slug: ramstush-journal-in-olpc
Author: ramstush
Tags: legacy, foss@rit
Category: legacy
URL: articles/ramstush/journal-in-olpc.html
save_as: articles/ramstush/journal-in-olpc.html
Summary: FINALLY A BREAKTHROUGH!!!! Today was our second work from home Friday. This time I was working from Cortland New York, about 2 hour away from RIT and the FOSSbox. My main mission continued throughout the week trying to get the Lemonade Stand Activity to create a journal entry. Previously, I had emailed a former surf member for some tips on how he worked with OLPC during his time with the FOSSbox. I was directed to his [Open Source Blog](http://blog.jlewopensource.com/) to research what he did wi ... 

FINALLY A BREAKTHROUGH!!!! Today was our second work from home Friday. This
time I was working from Cortland New York, about 2 hour away from RIT and the
FOSSbox. My main mission continued throughout the week trying to get the
Lemonade Stand Activity to create a journal entry. Previously, I had emailed a
former surf member for some tips on how he worked with OLPC during his time
with the FOSSbox. I was directed to his [Open Source
Blog](http://blog.jlewopensource.com/) to research what he did with Lemonade
Stand and Fortune Hunter.

This morning, I received an email in response telling me that the reason
Lemonade stand wasn't writing to the journal was because in the class param's
within Lemonade stand's activity.py file, create_object was set to false. I
seriously thought that there was no way this could be the only thing keeping
the activity from writing to the journal. Turns out it was. After I changed
that boolean to True, there was a beautiful journal entry sitting before my
eyes.

Next step for me is to play around with datastore more to determine how to
store the specific information we need for badges. Stay tuned from the epic
week recap later to come!

