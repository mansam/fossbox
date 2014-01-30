Title: Week 2: Bug Fixes
Date: 2011-12-07T15:00:00
Slug: decause-week-2-bug-fixes
Author: decause
Tags: legacy, foss@rit
Category: legacy
Summary: So, after spending some time pouring over some of the high-profile python ... 

So, after spending some time pouring over some of the high-profile python
projects on [GitHub](http://github.com), I found a handful of populars and
forked to look for bugs. It was successful!

I have 3 open pull requests in [Bottle.py](https://github.com/defnull/bottle),
[twython](https://github.com/ryanmcgrath/twython), and [foursquare-
python](https://github.com/wiseman/foursquare-python). Bottle.py is a dead-
simple micro-framework for python web applications, and one I've played with
before. Twython is a pure-python wrapper for the Twitter API. Foursquare-
python is a python module for interfacing with the Foursquare API. For twython
and foursquare-python, I felt even my humble style-fixes would be welcome to
such well-travelled codebases that are likely being used by many app
developers. Bottle.py is one of those projects that really demonstrates the
simplicity and elegance of python, while doing some powerful stuff under the
hood. Having commits in bottle.py _just feels good_.

As I am not exactly a leetz0r, I chose some relatively low-hanging fruit in
the realm of python style guide compliance, as per [Python Enhancement
Proposal #0008](http://www.python.org/dev/peps/pep-0008/). Thanks to the power
of a nifty utility called [pep8](https://github.com/jcrocholl/pep8) (available
via easy_install, apt, and yum!) I was able to comb through large codebases to
cherrypick the offending lines in each of these projects. Though these are not
necessarily _functional_ bugs, things like removing tabs from a file may avert
future bugs, particularly in an example file. If someone were to copy and
paste code from an example file with tab spacing in it, and then add their own
code below and indent it properly using the standard 4-spaces, there would be
errors.

Here are the Pull Requests I have that are still Open:

  * [foursqaure-python](https://github.com/wiseman/foursquare-python/pull/1)
  * [Twython](https://github.com/ryanmcgrath/twython/pull/52)

I had one other pull request in Bottle.py, but the upstream considers PEP8
"Just a guide" so closed it. Here is the [bottle.py
thread](https://github.com/defnull/bottle/pull/260).

My good deed for the day is done, and so is my homework! I'll likely be
experimenting with a bottle.py deployment on
[PythonAnywhere.com](http://pythonanywhere.com), on which I just got my
private beta activation code today! Check me out soon at
[http://decause.pythonanywhere.com](http://decause.pythonanywhere.com)

