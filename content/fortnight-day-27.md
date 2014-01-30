Title: Day 27
Date: 2013-07-05T12:44:00
Slug: fortnight-day-27
Author: fortnight
Tags: legacy, foss@rit
Category: legacy
Summary: # Breakthroughs and Revelations ... 

# Breakthroughs and Revelations

Day two of [El Puesto de Limonada](http://www.plazasesamo.com/documents/plaza-
sesamo/Sesame%20Images/400x300_PlazaGames_Thumb_Limonada/400x300_PlazaGames_Th
umb_Limonada.jpg/Original/400x300_PlazaGames_Thumb_Limonada.jpg)(pic related).

Previously on Fortnight's FOSS...

-> The internet gave me this  
-> [Qalthos](http://github.com/Qalthos) explained the part about genpot and that I had to translate [this file, Lemonade.pot.](http://paste.fedoraproject.org/23281/13730405/)  
-> [FMD](http://github.com/decause) showed me the [python side of things](http://docs.python.org/2/library/gettext.html) and I messed around with the gettext.py commands.  
-> Fedora linux has a series of "*.mo" files in the "/usr/share/locale/es/LC_MESSAGES/" directory  
-> [ Brian's gone to Los Angeles to find himself?](http://familyguy.wikia.com/wiki/Brian_Does_Hollywood)

Just before Lunch, it all clicked together. One had to use msgfmt.py create a
.mo file from the .pot file acquired from genpot, with it as a parameter(`$
msgfmt.py Lemonade.mo`). After scanning through the gettext.py source code I
saw the correct parameters for the "translations" function; until then I
thought I had to give it the path to the Lemonade.mo file that I had placed in
my locale directory, but gettext needed to run its "find" function, which is
embedded in its translation function. The working lines of code go as follows:

`import gettext

lang = gettext.translation('Lemonade', '/usr/share/locale/', languages =
['es'])

_ = lang.ugettext`

This should get things done, so long as one places a copy of their ".mo" in
their LC_MESSAGES directory.

Now I just have to solve the problem that arise from all the accent marks.

[My feelings for the day](http://meme5.net/#i=meme-illhaveyouknow;t=I~27ll_hav
e_you_know_I_got_gettext_working_on_my_teams_python_project;b=And_I_only_wante
d_to_punch_through_my_laptop_screen_twelve_times;)

