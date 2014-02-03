Title: Navigating Glade
Date: 2013-06-18T16:59:00
Slug: Zanarama-navigating-glade
Author: Zanarama
Tags: legacy, foss@rit
Category: legacy
Summary: A large goal of the Gourciferous project is to create a GUI that will make processing GIT logs and rendering Gource videos a lot easier. For the past few days I have been working on creating some mock-ups for the GUI in Glade. The benefit of using Glade is that the mock-up can easily become a functional GUI by adding a Python program to create functionality. However, using Glade hasn't been a picnic.  Originally the software seemed incredibly intuitive. The buttons are simple, and it truly on ta ... 

A large goal of the Gourciferous project is to create a GUI that will make
processing GIT logs and rendering Gource videos a lot easier. For the past few
days I have been working on creating some mock-ups for the GUI in Glade. The
benefit of using Glade is that the mock-up can easily become a functional GUI
by adding a Python program to create functionality. However, using Glade
hasn't been a picnic.

Originally the software seemed incredibly intuitive. The buttons are simple,
and it truly on takes a few minutes of tinkering to start creating a GUI that
looks pretty nice. After I started though, designing the GUI became much more
difficult. One of my biggest challenges was the lack of a tutorial that was
really all-encompassing of Glade. There were some fine tutorials that walked
you through a project and gave you some code to add functionality, but a lot
of them lacked guide to building your own GUI, including what all the many
options Glade has actually do! One of the most helpful tutorials was by [Micah
Carrick](http://www.micahcarrick.com/gtk-glade-tutorial-part-1.html). His
guides were a great resource to understand GTK+, some Glade configurations,
and the difference between using C and Python with Glade.

By far, the most frustrating aspect of my brief stint with Glade was its buggy
nature. On my laptop, which is running Fedora 18, would consistently segfault
while I was working. Most commonly, it seemed to happen while I was adding and
deleting widgets. I was unfamiliar with all of the tools available and would
often try an option, only to decide I didn't like it and try to remove it.
Then the program would freeze and crash. I submitted a bug report with all the
info from my segfaults. I'm not sure if this is a problem isolated to my
laptop but no matter what, it was frustrating.

For now we are moving past the GUI to focus on creating rendered videos for
Red Hat. Our most important goal is getting some great videos created to
visualize the contributions of the amazing Red Hat community. Hopefully once
we get these done we can put some more time into making Gource more
accessible.

