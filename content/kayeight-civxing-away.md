Title: CIVX-ing away
Date: 2010-07-19T07:44:00
Slug: kayeight-civxing-away
Author: kayeight
Tags: legacy, foss@rit
Category: legacy
URL: articles/kayeight/civxing-away.html
save_as: articles/kayeight/civxing-away.html
Summary: Lately we have been trying to both put a swanky new theme on the CIVX website as well as wrap up the person dashboard. While Rebecca has been doing an amazing job on the former, I have been working on the latter. I ran into a few snags earlier last week when I experienced the results of not pulling from the repository often enough (note to self: don't do that again) and had problems merging my code with the large amount that had been committed since I last pulled.  With that lesson learned, I go ... 

Lately we have been trying to both put a swanky new theme on the CIVX website
as well as wrap up the person dashboard. While Rebecca has been doing an
amazing job on the former, I have been working on the latter. I ran into a few
snags earlier last week when I experienced the results of not pulling from the
repository often enough (note to self: don't do that again) and had problems
merging my code with the large amount that had been committed since I last
pulled.

With that lesson learned, I got back to trying to get all the tabs
dynamically. With bills and actions working properly, my next target is
contact information. I was able to scrape most of the senator's addresses
using the world's most hideous regular expression and BeautifulSoup. That's
about when I hit another issue, in that the NY senate's website HTML is so
inconsistent that not even a 300 character regex could capture every senator's
info.

The ideal solution to this is an improvement to the Open Legislation API so
using BeautifulSoup isn't necessary, and I've submitted a request, but for now
this is the best I can manage. This week I will hopefully find a workaround to
save me from having to pull an ever greater regex hack.

