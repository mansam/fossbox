Title: Yay, now working on Empathy patch
Date: 2012-04-16T18:40:00
Slug: imnotlistening-yay-now-working-on-empathy-patch
Author: imnotlistening
Tags: legacy, foss@rit
Category: legacy
URL: articles/imnotlistening/yay-now-working-on-empathy-patch.html
save_as: articles/imnotlistening/yay-now-working-on-empathy-patch.html
Summary: # A patch for Empathy  Its been a while since I have had time to post a blog entry with any real substance - Mid terms and projects can be brutal on your time. But that's essentially over now so I thought I would describe my current set up for playing with sugar and Empathy. Obviously development of software on an XO would be quite painful. The developers over at Sugar Labs were awesome enough to make Sugar run on essentially any Linux platform with X. So, now that [VM](http://foss.rit.edu/node/ ... 

# A patch for Empathy

Its been a while since I have had time to post a blog entry with any real
substance - Mid terms and projects can be brutal on your time. But that's
essentially over now so I thought I would describe my current set up for
playing with sugar and Empathy. Obviously development of software on an XO
would be quite painful. The developers over at Sugar Labs were awesome enough
to make Sugar run on essentially any Linux platform with X. So, now that
[VM](http://foss.rit.edu/node/348) I made has yet another use, outside of
cross compiling code for the XO. I am running a Sugar window manager on that
VM which lets me test the DBus functionality of my Empathy patch without
having to copy the code to an XO every time.

Here is how I set up the Sugar WM:

`

$ git clone git://git.sugarlabs.org/sugar-jhbuild/mainline.git sugar-jhbuild

$ ./sugar-jhbuild update

$ ./sugar-jhbuild depscheck

$ ./sugar-jhbuild build

`

The depscheck command produced quite a few, maybe 20ish packages that were
missing. Thankfully it was as easy as copying the output of deps check to a
yum install. Very simple, ended up being about 30 MBytes of required space.

After building the code I can run sugar as my WM from the login prompt for my
account on the VM. I can either use my good old gnome-shell or the terminal
app that comes with sugar. From their I can manually run Empathy with my
changes.

Cool stuff. More to come soon.

