Title: from civx import magic
Date: 2010-07-11T19:02:00
Slug: decause-from-civx-import-magic
Author: decause
Tags: legacy, foss@rit
Category: legacy
URL: articles/decause/from-civx-import-magic.html
save_as: articles/decause/from-civx-import-magic.html
Summary: A Proper Hackfest.  Finally.  16 hour days.  At least 16.  Breaking only to eat and maybe grab a cig here and there.  Deep. Real deep.  Like, all the way down to the bottem of the stack. Opening up SQLAlchemy source, DBSessions, engines, metadata... super low-level Database/Datamodel hacking. Halfway through, Lewk and I looked at eachother and thought:  > Did we dive too deep?  Can we really build DynamicDataObjects on-the-fly?  Are the Polymorphic Tables really supposed to be (ab)used in this w ... 

A Proper Hackfest.

Finally.

16 hour days.

At least 16.

Breaking only to eat and maybe grab a cig here and there.

Deep. Real deep.

Like, all the way down to the bottem of the stack. Opening up SQLAlchemy
source, DBSessions, engines, metadata... super low-level Database/Datamodel
hacking. Halfway through, Lewk and I looked at eachother and thought:

> Did we dive too deep?

Can we really build DynamicDataObjects on-the-fly?

Are the Polymorphic Tables really supposed to be (ab)used in this way?

The answer all around was yes.

After going to sleep Friday night after being well into the dawn, frustrated
by blockers of various flavors and types from moksha all the way through our
low-level models to our high-level widgets, we were not sure whether our
beloved FactEntity Model could really do what we thought it could. Lewk said
to me,

> "I just need to accept this, and sleep on these problems."

I was awoken by the familiar rattle-tee-clickity-rattle-tee-clackity of the
old-skewl IBM keys. He said to me "I was dreaming all night about this code.
When I woke up, I had 2 ideas on how to solve the problem"

After a few hours of hacking on Saturday, lewk's ideas proved prescient. Our
doctests were finally behaving. We felt the stack falling in line, and
performing the way it was meant to.

We dove deeper.

By nightfall, we were dispatching polyscrapers, from a web-facing widget, to
the first hit for .csv files on data.gov.

Then the first 25.

Then the first 100.

In about 6 minutes.

By primetime hackery hours past midnight, we saw what 100 .csv files look like
in a Jit-Hyper-Adjacency-tree, and by the wee-hours, luke refactored our grid
search API to handle the newest jQgrid. By sun-up, we saw our first on-the-fly
generated PolyGrid, and by well into the morning, before we went to bed, the
column names were even auto-named correctly.

I've never seen all of the pieces of the civx stack being run at once from one
widget. We've basically, as far as a developer is concerned, captured the
lightning of dataset lifecycle in a bottle.

  * User Provides a url to our polyform widget
  * URL is passed to the MokshaHub via AMQP message
  * "Interesting" data is located, downloaded, and git committed
  * Entities get their facts populated (Magic is invoked)
  * DynamicModels are built on-the-fly and added to our postgres db
  * Scraped datasets get a hypertree widget, and dataset profile widget
  * Newest jQgrid is auto-populated with polyscraped data in real-time

After a good 38 hours or so of the last 48 spent neck-deep in the guts of
moksha and civx, PolyScrapers have hit our public dev repo. Currently we only
handle csv's, but we're going to make our way though the civx.utils and add
handlers for each of the "interesting" datatypes that we already scrape, and
someday, all the kinds of datatypes that python-magic knows about. Next on the
list is .xls files most likely, then xml/rss/atom/ical and the other live/feed
types. Then comes the hard stuff, pdf2txt, OCR type data, shapefiles, and
other fancier datasets.

It's kinda hard for me to believe it. When Lewk and I originally pondered the
implications of SQLAlchemy and python on Public Data, we knew "someday" CIVX
_could_ make it there. We didn't think that day was going to be today.

My mind swirls with the grandeur of the even more complex and capable corners
of the python realm that will make their way into civx "someday":

  * Neural Networks
  * Natural Language Parsing
  * Genetic Algorithms
  * Polimetrics and Live-Analytics
  * and whatever else is "interesting" on pypi, sourceforge, github, or wherever else FOSS happens

I am inspired. Witnessing the metaphysical come to life before my very eyes at
the ends of calloused and blistered fingertips. I can see further out onto the
horizon of possibility than ever before, and I know that we have only just
begun to scratch the surface.

Saving_The_World(Remyd):

