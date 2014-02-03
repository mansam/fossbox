Title: Day 17
Date: 2013-06-21T16:02:00
Slug: fortnight-day-17
Author: fortnight
Tags: legacy, foss@rit
Category: legacy
Summary: # Workin' Hard or Hardly workin', eh MAC?  At the start of the day, I felt pretty positive. [Threebean](https://github.com/Ralphbean) was in the FOSSbox today, and I recalled our previous code diving experience. He told me that someone from ITS was worried about the routers and was a bit unsure as to why they were sending de-authenticating packets to someone network. I introduced myself to someone in the ##rc.rit channel and sent an email declaring that I was the victim/culprit of the network is ... 

# Workin' Hard or Hardly workin', eh MAC?

At the start of the day, I felt pretty positive.
[Threebean](https://github.com/Ralphbean) was in the FOSSbox today, and I
recalled our previous code diving experience. He told me that someone from ITS
was worried about the routers and was a bit unsure as to why they were sending
de-authenticating packets to someone network. I introduced myself to someone
in the ##rc.rit channel and sent an email declaring that I was the
victim/culprit of the network issue. He got back to me later in the day saying
that he'd look into it. I hope that was a promise to help and not a way of
saying it'll never get done, but I suppose if I keep trying then he'll keep
having to deal with the de-authentication problems...

In other news, when I told [FOSSmaster Decause](https://github.com/decause)
about it, he informed me that all the XOs used to be on the network whitelist,
and that if I get an in with ITS to give them a list of MAC address of all the
XOs. A list we didn't have. I then spent the Majority of the day going through
all 36 XOs we had, turning them on, and calling "ifconfig" in the terminal.
[Qalthos](https://github.com/Qalthos) taught me something very interesting
though. When one of the laptops didn't recognize the command "ifconfig" he
told me to call "/sbin/ifconfig" because apparently all the commands that the
Terminal can run were in either /bin/ or /sbin/. The computer didn't know it
was there though because it wasn't on the PATH that the computer sets to know
where to load commands and programs from. Apparently all commands are there as
binary files or runable scripts.

Also, Qalthos got a Schoolserver running on the same server that houses this
site and the bot that records our meetings, but the "boat" went down
yesterday, delaying schoolservers, my blog posts, and redemption.

[My Feelings for the day](http://www.quickmeme.com/meme/3uxwnc/)

