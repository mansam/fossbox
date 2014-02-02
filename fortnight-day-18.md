Title: Day 18
Date: 2013-06-24T01:15:00
Slug: fortnight-day-18
Author: fortnight
Tags: legacy, foss@rit
Category: legacy
Summary: #  More Code/Cave diving ... 

#  More Code/Cave diving

Sadly no Threebean to help me search. However, I have not forgotten the most
valuable command line call he has taught me so far: "grep -inr SEARCH_TERM * |
less." For information on how that works, click...
[HERE](http://foss.rit.edu/node/471). It's a previous blog post, from day 7.5,
the day [I lost count](http://www.christian-
revolution.net/images/david/11-lostCount1.jpg).

So, as you recall from my post of day 17 I spoke a grand revelation about all
unix commands being in the folder /bin/ or /sbin/. The day before yesterday I
spoke of instructions like "Either run 'xs-setup-network' or do everything
yourself." Well I tried running xs-setup-network, and it didn't do anything.
So I tried looking at the manual page for the command (which you can do for
any command in /bin/ or /sbin/, like 'man ssh') but unfortunately, the command
xs-setup-network had no man page. Regardless I was not ready to give up hope
and figured that the command must have a file somewhere on the computer that
is a script prepared to actually run the command. I changed my directory to:
'/' which is the root directory, but will henceforth be called 'atlantis.'
Once on the shores of atlantis I ran the command: "grep -inr xs-setup * |
less" which would take awhile because it would have to recursively search
through all the files in all the folders of my computer for any line that
includes the phrase "xs-setup", case insensitive. I then went to a workshop
for the McNair Scholars program.

Upon my return I had a hearty list of programs to search through and began
taking notes.

[My feelings for the day](http://meme5.net/#t=ONE_DOES_NOT_SIMPLY;b=TAKE_NOTES
_ON_CODE_WHOSE_WRITERS_DIDN~27T_CREATE_A_MAN_PAGE;i=meme-onedoesnotsimply;)

