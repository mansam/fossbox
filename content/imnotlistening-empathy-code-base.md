Title: Empathy code base
Date: 2012-04-23T00:53:00
Slug: imnotlistening-empathy-code-base
Author: imnotlistening
Tags: legacy, foss@rit
Category: legacy
URL: articles/imnotlistening/empathy-code-base.html
save_as: articles/imnotlistening/empathy-code-base.html
Summary: So, now that I have been hacking away, here is what I am working on.  The first aspect of setting up a Sugar App is parsing some command line arguments. The arguments help configure the app so that the Sugar Framework can properly interface between the App and the X server. Or something like that. These arguments are:  `  -b, --bundle-id   Identifier of the activity bundle. Must be made available as window property.  -a, --activity-id   Unique identifier of the activity instance. Must be made av ... 

So, now that I have been hacking away, here is what I am working on.

The first aspect of setting up a Sugar App is parsing some command line
arguments. The arguments help configure the app so that the Sugar Framework
can properly interface between the App and the X server. Or something like
that. These arguments are:

`

-b, --bundle-id  
Identifier of the activity bundle. Must be made available as window property.

-a, --activity-id  
Unique identifier of the activity instance. Must be made available as window
property, and is used to create the D-Bus service.

`

(See the rest here: [http://wiki.sugarlabs.org/go/Development_Team/Low-
level_Activity_API#Com...](http://wiki.sugarlabs.org/go/Development_Team/Low-
level_Activity_API#Command_Line_Arguments))

These two arguments, the only two that are relevant to Empathy - though the
data store arg will have to not crash Empathy - are passed to any sugar app to
set up DBus and X. My patch hooks into the argument parsing code in Empathy so
that when these arguments are passed, the following environment variables are
set to the passed argument string: `_SUGAR_BUNDLE_ID` and
`_SUGAR_ACTIVITY_ID`.

Empathy is a pretty complex app, so it is no surprise that parsing arguments
is not as simple as a simple app would have it. Empathy uses a GApplication
framework; and has multiple different programs running simultaneously. As such
argument parsing has to be accomplished in a GApplication specific way. Mostly
it is a wrapper for the typical getopt(_long) style C argument parser but its
a little more in depth since these arguments are being parsed across multiple
processes. Also I am not sure how to handle the derivative programs, e.g: the
calling window program. They are independent programs but not really
independent apps; however, Suagr won't really understand that, I don't think.

But yeah, at least I am making some progress on this patch.

