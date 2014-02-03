Title: Success!
Date: 2010-06-09T15:11:00
Slug: DaveSilver-success
Author: DaveSilver
Tags: legacy, foss@rit
Category: legacy
Summary: So after a long and fruitless process we finally finished retooling the first animation test tool. The current version displays the average time it takes to display a frame which we can then use to determine how many frames are being displayed each second. Later tonight JT plans to continue refining the program so that it gives us this information directly and so that it works for all of the file formats. Ideally tomorrow morning we will have preliminary test results that will tell us how effect ... 

So after a long and fruitless process we finally finished retooling the first
animation test tool. The current version displays the average time it takes to
display a frame which we can then use to determine how many frames are being
displayed each second. Later tonight JT plans to continue refining the program
so that it gives us this information directly and so that it works for all of
the file formats. Ideally tomorrow morning we will have preliminary test
results that will tell us how effective each file format, excluding SVG, is
under minimal conditions. We will then begin expanding on the testing tool to
make the situations more and more stressful. Hopefully we will be able to gain
a good idea of how stressful a situation each file type can handle well.

As far as SVGs go, most of the info I am finding seems to point to the idea of
importing a preexisting library that does not come with python/pygame or
having to build one from scratch. On top of this it seems many of the
libraries that have been built by other people are geared towards SVG creation
through python, and not SVG integration with python which is what we need. As
far as I can tell there is no easy way to integrate SVGs into Python at this
time without bringing in at least one extra library beyond what the XOs
already include. Depending on how easy it is to integrate these libraries we
may not be able to use SVGs at all. This is especially true when we consider
the limits of the XO platform, and our goals of optimization. We plan to
continue our research into SVGs tomorrow and thus I will have more updates
when we are done. See you then.

