Title: Arg, A Mishap...
Date: 2012-05-01T01:08:00
Slug: imnotlistening-arg-a-mishap
Author: imnotlistening
Tags: legacy, foss@rit
Category: legacy
Summary: I have been using my laptop for a while now for development on Empathy. Since my laptop is running Fedora 16, there is less libraries that need compiling in order to run the latest git empathy. But like any project dependencies are updated on occasion. It just so happens that the GTK+ dependency for Emapthy got updated fairly recently, so when I pulled the latest code, my GTK+ library needed recompiling. Eh, didn't seem like a big deal, compiled fine 1 minor version ago, so I figured it would be ... 

I have been using my laptop for a while now for development on Empathy. Since
my laptop is running Fedora 16, there is less libraries that need compiling in
order to run the latest git empathy. But like any project dependencies are
updated on occasion. It just so happens that the GTK+ dependency for Emapthy
got updated fairly recently, so when I pulled the latest code, my GTK+ library
needed recompiling. Eh, didn't seem like a big deal, compiled fine 1 minor
version ago, so I figured it would be easy peasy to recompile the next
version. Well, I was wrong.

Like many a library, I had to recompile some other libraries to get GTK+ to
compile. It just so happened that the glib dependency had to be recompiled
(and, of course, the requirements are far ahead of the libraries in the Fedora
repos, so recompile from source is really the only option). In GLib is a
library called gobject. GObject provides a faux OO feel to C. Very
frustrating, IMO, since it adds an absurd amount of complexity to any project,
but oh well, just gotta deal. So recompile, recompile, recompile, GLib seems
OK, installed to /usr/local, everything seems dandy. Go to reconfigure GTK+,
still seems OK, go to compile... and hmm, interesting error.

For some reason the compile is failing during a link for which a symbol in
libgobject is missing. Maybe the problem is the linker flags, so 'export
LDFLAGS=-lgobject-2.0' since /usr/local/lib is already specified in the build
command. Still no go, same issue as before, missing symbol in gobject. Hmm,
maybe the system libgobject is getting read first and causing the failure. If
I put the -lgobject-2.0 before any other linker flags, maybe it will be linked
against. So I try and put the same flag into CFLAGS. Configure isn't sthat
stupid, (sadly), it keeps the CFLAGS separate from the link despite the fact
that it uses gcc. Eh, oh well. Maybe copying my new gobject library into the
system gobject library (/lib64/libgobject-2.0.so.0.3000) will fix my issue.
Simple enough, su, then issue a copy command, then the screen goes blank.

Oh. Right. Anything that uses GTK+ (99% of GUI apps in Fedora using a Gnome
based UI) is going to be using GObject. I try and restart X, since I do still
have access to my emulated terminals. No, go. XFCE can't start, just so
happens the new gobject library is missing a symbol: g_get_strbytes() or
something, I can't remember. Something that must have been deprecated and
finally removed. Luckily I have a copy of the system gobject in /lib (no idea
why). Try an 'export LD_LIBRARY_PATH=/lib', rerun X, and whoo, it starts, even
brings up a UI, but it is rather flimsy. A lot of stuff still doesn't seem to
work. Anything linking against the GTK+ libraries. Even 'su' doesn't work,
though I have no clue how that has anything to do with GObject, and I can't
debug it since as a 'suid' program, it won't actually run under my username,
it runs as root. Bleh. I try to restart my system and fix the issues, but no
go, I no longer can boot. Good game computer.

One thing I could have done, but completely forgot to do, is simply log into
one of the terminals as root, no need for 'su' in that case. Oh well, gonna
have to try and fix the system some other way, but until then, I am gonna have
to put this development on hold. For what it is worth, I am now working on
setting up the DBUs interface for Empathy to receive commands from Sugar.
Those DBUs calls are listed on the Low Level Sugar activity API page. In any
event, I can always go back to my VM, but that's so slow. Not really something
I want to do but if I have to, I will.

