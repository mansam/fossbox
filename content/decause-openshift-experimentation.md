Title: Openshift Experimentation
Date: 2012-01-11T02:21:00
Slug: decause-openshift-experimentation
Author: decause
Tags: legacy, foss@rit
Category: legacy
Summary: After **seven** tries at getting the foss@rit site migrated to openshift, I ... 

After **seven** tries at getting the foss@rit site migrated to openshift, I
must concede... for tonight.

Vanilla openshift quickstarter for drupal

    First attempt was editing by hand, and I installed modules and themes after bumbling around in the new (to me) drupal 7 interface.
    installed the backup and migrate module, and tried to restore from a mysqldump from this site... and hosed it
destroy the app, start fresh

    bumble around til I figured out how to enable phpmyadmin
    import the sql backup manually... and hose the site
destroy the app, start fresh

    enable phpmyadmin again, and try to just create a new empty database... and hose the site, again
rinse and repeat each of these approaches at least 2 times just incase...

I'm probably bringing this on myself, but all of the documentation is (seems
to be) tailored to folks *not* using the openshift quickstarter. I guess I can
try to use the web console command line next time, but even still... I have
(had) a successful openshift tweetstream app running, but now that seems to be
down too... #doingitwrong * 7 :(

**All that said, It is *really* awesome and extremely satisfying to be able to spin up a fresh drupal and get cranking within 180 seconds**. I got to look at some of the new html5 and 960gs themes, and will figure out how to actually tweak them tomorrow, where I'll be hopping into #openshift and getting to the bottom of this...

