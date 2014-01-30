Title: Updating Empathy
Date: 2012-04-04T00:59:00
Slug: imnotlistening-updating-empathy
Author: imnotlistening
Tags: legacy, foss@rit
Category: legacy
Summary: Looks like the best course of action is to add support to Empathy or Sugar to ... 

Looks like the best course of action is to add support to Empathy or Sugar to
properly interface a video chat app into sugar. How exactly this will be done
is not completely clear to me yet but here are the possibilities I have seen.

## Modify And Add To The Empathy Code Base

Sugar communicates with its activities via DBus. DBus is an IPC mechanism
which allows the SUgar shell to pass commands via remote method calls to a
running application. In order to make Empathy a proper sugar activity, it
would need the means to respond to the special requests passed by Sugar. The
exact interface for interfacing with sugar is described in all its gory detail
out here: [http://wiki.sugarlabs.org/go/Development_Team/Low-
level_Activity_API#Act...](http://wiki.sugarlabs.org/go/Development_Team/Low-
level_Activity_API#Activity_Instance). The required additions would be a few
environment variables being set, some command line argument parsing, and
several DBus method calls. This does not look like a particularly massive
amount of work. Not only that, but it can be run under a sugar UI running on a
normal Linux desktop (e.g Fedora 16 or what have you).

## Modifying Sugar

It was suggested to me that instead of modifying the Empathy code base, the
solution should be done entirely on the sugar side. Sugar already uses
telepathy for its communication framework but how exactly that translates to
Empathy support, I do not fully understand. If it is possible to simply add
some configuration options to Sugar to use Empathy as the default video chat
activity, that would be nice. However, I don't think it would be that easy
since the above sugar DBus calls would still have to be implemented (I would
think).Either way, maybe some more info from the mailing list will come my
way, and a clearer picture will be painted. In the mean time I think I will
start looking at the Empathy code more in depth and see how easy it would be
to add the Sugar DBus calls to the Empathy source.

