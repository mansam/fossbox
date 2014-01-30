Title: Day 7.5
Date: 2013-06-06T09:41:00
Slug: fortnight-day-75
Author: fortnight
Tags: legacy, foss@rit
Category: legacy
Summary: ##  Threebean and Fornight in the caves of Sugar ... 

##  Threebean and Fornight in the caves of Sugar

Maybe it was because I had just read [this
article](http://seriouslyforreal.com/seriously-for-real/heracleion-photos-
lost-egyptian-city-revealed-after-1200-years-under-sea/), but I felt like I
was doing Archaeology. It turns out that although the Sugar desktop
environment download was all in the package I downloaded, it was in a several
different folders haphazardly mixed with all other python programs installed
on my "box." Veteran Python coder [Threebean](http://threebean.org/blog/)
taught me some great methods of searching through the folders in linux. For
example:

All python installations are installed in the linux folder: /usr/lib/python2.7
/site-packages/

To case-insensitively search for a term in all the texts of a folder and in
sub-directories enter the following command in the terminal: "grep -inr **
SEARCH_TERM ** * | less"

"grep" is a searching tool that searches for whatever you enter as
SEARCH_TERM, -i makes it case insensitive, the * includes through all files in
the current directory in the search, the -r recursively adds subdirectories to
the search, the -n adds the line number of where the SEARCH_TERM shows up in
the file, and lastly, we pipe the command into "less" which allows us to
scroll through the results with the arrow keys.

After panning through the results, we looked into the sourcecode that
contained words like "schoolserver" and "journal", finding many necessary
files in folders like
["telepathy"](http://th04.deviantart.net/fs71/PRE/f/2012/328/a/6
/professor_charles_xavier_by_fredackerman-d5m2eij.jpg) and ["jarabe."](http://
4.bp.blogspot.com/-ioWA6bEsTnI/TWXxcwHqCFI/AAAAAAAAAGc/rMw6rbqr7A4/s1600/JARAB
E+SABOR+NATURAL+GARRAFA+4+L.jpg) Scanning the python code within those folders
felt like trying to understand hieroglyphs on the walls of ancient temples.
One can also use a "/" to search down in a vim, and a "?" to search upwards in
vim. Threebean also showed me that most programs have accounts on the
computer, and we logged into one to see if it had code that uploaded regularly
to a schoolserver, but to no avail. It felt like trying to commune with the
spirit of some [ancient high priest](http://images1.wikia.nocookie.net/__cb200
80309142857/timesplitters/images/7/72/Enemy2_pic.jpg), but we did the ritual
incorrectly. He fears that the code we're looking for might never have been
implemented, that the Ancient civilization was wiped out before they achieved
spiritual resonance in their religion. I, however, still have hope, and will
spend my next day deciphering these ancient texts to dive deeper into these
mysteries.

P.S. apparently the Hackathon only counted as one day, but
[bear](http://images.nationalgeographic.com/wpf/media-
live/photos/000/005/cache/grizzly-bear_566_600x450.jpg) with me

