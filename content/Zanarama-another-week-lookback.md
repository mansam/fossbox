Title: Another Week Lookback
Date: 2013-07-15T08:37:00
Slug: Zanarama-another-week-lookback
Author: Zanarama
Tags: legacy, foss@rit
Category: legacy
URL: articles/Zanarama/another-week-lookback.html
save_as: articles/Zanarama/another-week-lookback.html
Summary: This week Gourciferous paper GUI Templates were mocked up, I contacted Upstream about presenting them to the Gource community, began working on short videos to send to Red Hat as examples, and I updated avatar_generator to work without log_generator.  Currently, there are two different paper mock ups for Gourciferous. One takes a the approach of a few tabs with lots of options and the other takes the approach of a lot of tabs with few options in each. I am not sure which one will be used, howeve ... 

This week Gourciferous paper GUI Templates were mocked up, I contacted
Upstream about presenting them to the Gource community, began working on short
videos to send to Red Hat as examples, and I updated avatar_generator to work
without log_generator.

Currently, there are two different paper mock ups for Gourciferous. One takes
a the approach of a few tabs with lots of options and the other takes the
approach of a lot of tabs with few options in each. I am not sure which one
will be used, however right now I am working on porting them into Glade.

I have contacted Andrew Caudwell about getting some feedback on Gourciferous.
I would really like to reach out to the Gource community but I couldn't find a
good way to do it. Hopefully I will hear back soon.

I would like to send Red Hat a set of short (30 or so seconds) Gource videos
so they can get an idea of options. Right now getting a project to fit that is
becoming challenging. Everything I have tried to make that short seems very
rushed. I am working on a better option now.

Finally, I realized that avatar_generator had never been completely finished
or pushed to Github. I completely removed any avatar generating from
log_generator and moved it completely to avatar_generator. Now,
avatar_generator parsing through the git repositories and uses a bash
formatted log to obtain the author names and email. It is pretty quick and I
think is cleaner to separate the two.

