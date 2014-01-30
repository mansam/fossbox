Title: Templates & Turtle
Date: 2013-07-01T03:32:00
Slug: Zanarama-templates--turtle
Author: Zanarama
Tags: legacy, foss@rit
Category: legacy
Summary: This week I had a couple of big success. First, I solved my (most) of my ... 

This week I had a couple of big success. First, I solved my (most) of my
problems with avatar file generating. I also created a handful of templates
that I think should fit a variety of projects. Finally, I introduced an old
project that I had been working on with Python Turtle and will hopefully get
some help working on it.

My two main problems with the avatar generating were Unicode characters in
usernames and difficulty handling all of the command line options we were
having in log_generator and avatar_gen. To solve the problem with Unicode
characters I used the function to_unicode() from a package called
[Kitchen](https://pypi.python.org/pypi/kitchen) to encode every log entry I
read in from a file to Unicode before I began parsing it. This prevented an
ASCII/Unicode mix that threw an error.

To solve my command-line arguments issue I utilized a module called
[argparse](http://docs.python.org/dev/library/argparse.html) to process my
arguments. The [argparse
tutorial](http://docs.python.org/2/howto/argparse.html) from the Python docs
was really informative and thorough. Using the tutorial I was able to
implement argparse in both log_generator and avatar_gen in a way that is much
cleaner than the logic we were using before. Another great feature of this
change is that all options for log_generator are now optional. I have defaults
set so that custom logs can be generated without any arguments, which is nice
in my opinion. Command line options are still required for avatar generator,
which needs a list of names and email hosts, and a list of email hosts with an
image file path to run. Overall, I think it is a great improvement though.

The custom templates are pretty self explanatory. I have a feeling as we
generate videos they will be edited a lot, but for now they are a strong
starting point. This week will be a little crazy with the 4th of July. Perhaps
over that time I will try to actually render videos to work on these settings.

Finally, I have created a repository for
[AmazingTurtle](https://github.com/Zanarama/AmazingTurtle). Right now it is in
a very basic stage but the point of the project is to be an introductory
lesson to programming for Middle school aged students through the Python
Turtle. The lessons will consist of navigating the turtle through various
puzzles, gathering stars and avoiding obstacles. I have actually taught using
this method to 6th and 8th grade students for two years now in my mother's
classroom. It has been highly rewarding and students have responded positively
to the lessons. It is something that I have really enjoyed teaching and I
think will be a great educational tool. As my exact project goals with that
become more clear, I may share more updates.

