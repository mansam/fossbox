Title: Future Direction
Date: 2012-03-24T17:19:00
Slug: imnotlistening-future-direction
Author: imnotlistening
Tags: legacy, foss@rit
Category: legacy
Summary: # Whats Going On?  There have been more than a few attempts at making a Sugar compatible video chat application. As it stands right now there are at least 4 or 5 that work to varying degrees. Empathy is probably the most functional app that I am aware of, however, Empathy is not Sugarized (as far as I know). So after signing up for a bunch of different mailing lists and asking a bunch of questions here is what I have learned.   Build a Completely New Program  After talking to the development lo ... 

# Whats Going On?

There have been more than a few attempts at making a Sugar compatible video
chat application. As it stands right now there are at least 4 or 5 that work
to varying degrees. Empathy is probably the most functional app that I am
aware of, however, Empathy is not Sugarized (as far as I know). So after
signing up for a bunch of different mailing lists and asking a bunch of
questions here is what I have learned.

# Build a Completely New Program

After talking to the development lost for sugar, it seems possible to build an
app in entirely C code that can interface with sugar through DBUS. DBUS is a
IPC messaging system that many Linux systems use. If an application implements
certain DBUS interfaces then it can be "sugarized". So how hard would it be to
implement a DBUS interface in C? Well according to the API docs, pretty hard: 
[http://dbus.freedesktop.org/doc/api/html/index.html](http://dbus.freedesktop.
org/doc/api/html/index.html). Apparently you would be in for a world of pain.
Thats not terribly surprising given the nature of C coding and the type of
functionality that DBUS exposes. Thats just one part of the project.

Next there is Telepathy. Interfacing with telepathy doesn't look too bad. The
docs appear to be somewhat here and there, however, which could lead to some
pain. However, the telepathy-devel mailing list is responsive and hopefully
willing to help if any telepathy interfacing needs to be done. And last but
not least: gstreamer. Interfacing with a telepathy client would require some
gstreamer code (I think). I am not completely sure how much back end stuff is
handled by telepathy at the moment. Certainly implementing an RTP/RTCP stream
with session control would be a major pain and time commitment. Especially
since at the moment it is certainly in the pipeline to implement both audio
and video streaming (a natural expectation for a video chat service).

# Maybe There Is An Easier Way...

Since Empathy does by default run on the XO platform it should be possible to
Sugarize the Empathy client. First some pros to this idea: all the low level
mess regarding RTP and video streaming would be handled by Empathy/telepathy,
account management would be handled by empathy, basically everything would be
handled by Empathy (how nice), and it would be (I think) relatively easy to
integrate a Sugarized Empathy client into the Empathy RPM package for the XOs.
Now the cons: the Empathy code base is not easy to dive into. After briefly
looking at the code, it would seem that there is just so much stuff going on.
Native GTK in C is not exactly the most concise of GUI code (but I am sure its
very fast). Thus learning the code base and actually adding the required DBUS
interfaces for Empathy to interact with Sugar would be in all likelihood
rather difficult. But not impossible.

# What To Do?

Well, those are my options. Either way I am going to need to really understand
DBUS in order to implement the required DBUS interface for Sugar. The question
is do the pros in making an Empathy based client out weight making a new
client from scratch. Time wise, will learning the Empathy code base be
feasible? So... In the next week I am going to commit to one of the paths once
I have some more insight from the respective mailing lists and people involved
in Empathy/telepathy and Sugar.

