Title: Day 26
Date: 2013-07-02T21:05:00
Slug: fortnight-day-26
Author: fortnight
Tags: legacy, foss@rit
Category: legacy
Summary: # Midterm Powows ... 

# Midterm Powows

Today I started the ticket of creating a Spanish version of Lemonade Stand.
[Yesterday](http://foss.rit.edu/node/550) I called it El Puesto de Limonada,
after [this picture](http://ecx.images-
amazon.com/images/I/51MHzc%2B6XML._SY300_.jpg).

So I started off by googling "XO Laptop GetText" and hitting up [the first
result](http://wiki.laptop.org/go/Gettext). As it instructed, I went through
the code for Lemonade Stand and made each message script be convertible, like
so: "This is a string" became _("This is a string"), and at the top of the
code, with the imports I would have added the line "from gettext import
gettext as _", but my teammate DAWacker beat me to it. I felt like I didn't
have enough information yet though, so I clicked [the link at the bottom of
the wiki.](http://www.gnu.org/software/gettext/) The GNU project it linked to,
though factual and thorough, was mainly about C. I asked
[FMD](https://github.com/decause) (FOSSmaster Decause, hereby abbreviated),
about a python equivalent, and he linked me to
[this.](http://docs.python.org/2/library/gettext.html) As I read that, I tried
the section "22.1.3.3. Changing languages on the fly" out, because I didn't
currently have a [translated file to work
with](http://liology.files.wordpress.com/2010/01/rosetta-stone.jpeg). However,
it didn't work. I then [peru](https://en.wikipedia.org/wiki/Peru)sed in
"/usr/share/locale/es", where my computer stored it's spanish translations of
programs in .mo files. The day ended with my completion of a translating the
message template gotten from running "./setup.py genpot" in the Lemonade-Stand
repository, a thing that [Qalthos](https://github.com/qalthos) showed me.

Lastly, I had a midterm powow with [FMD](https://github.com/decause) and
[SURFcaptain SJ](http://igm.rit.edu/node/978) about how I felt the summer was
going. Overall I am enjoying the experience, environment, and energy of the
FOSSsummer.

[My Feelings for the day](http://meme5.net/#t=Assigned_something_you~27re_capa
ble_of~3F;b=Do_that_shit!;i=meme-couragewolf;)

