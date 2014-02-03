Title: CapitolCamp ReCap
Date: 2010-08-30T19:10:00
Slug: decause-capitolcamp-recap
Author: decause
Tags: legacy, foss@rit
Category: legacy
Summary: Out across the empire plaza, a man in a white hat and three piece strides along between the reflecting pools toward The Egg. In train, a sharply clad trio of women, each toting their satchels full to the brim with equipment, computers and ambition. Amongst the towers, amphitheatres, and marble goliaths, their eyes were wide with experiencing the Capitol for the first time, but in too much of a hurry to take much in.  ![](http://foss.rit.edu/files/emplazacrop.png)  After a meet and greet with the ... 

Out across the empire plaza, a man in a white hat and three piece strides
along between the reflecting pools toward The Egg. In train, a sharply clad
trio of women, each toting their satchels full to the brim with equipment,
computers and ambition. Amongst the towers, amphitheatres, and marble
goliaths, their eyes were wide with experiencing the Capitol for the first
time, but in too much of a hurry to take much in.

![](http://foss.rit.edu/files/emplazacrop.png)

After a meet and greet with the contingent from Sunlight Labs the team made
their way into to the Legislative Office Building (Affectionately known around
SmAlbany as the LOB).

After a march through the detector archways, the group hurriedly scrawled
names across their standard issue adhesive nametags, and filed into a row near
the back of the chamber (from last I recognized the room as where, as a
legislative associate, I covered the convening of the Spitzer Administration's
budgetary "Mothership" during my (and his) short time in Albany.)

I took note of the industry folks on the right and tucked in the back of the
room, the pols and organizers in the front, and the smattering of agency
staffers throughout the crowd. We sat with the
[Sunlighters](http://sunlightlabs.com); the
[OpenPlanners](http://openplans.org) and NYC OpenGovers sat mostly near the
front left. Then there were the developers. Web 2.0 startups, open data
providers, Internal IT staffers, and other students and interns from RPI's
FOSS Contingent, [The Rensselaer Center for Open Source](http://rcos.rpi.edu).

We were welcomed to our seats by a thoughtful mention by the MC, Noel "Noneck"
Hidalgo, of FOSS@RIT's inspiration in suggesting a development focused day of
geekdom and revelling in some of the particulars of Politechs. From then on, I
was too engrossed within the subject of my story to give a proper objective
account. The experience was enthralling for a career Hacktivist, To actually
be walking some serious talk while surrounded by mostly .gov digital natives,
and other process participants who "get it," but I will do my best to
reconstruct the bits.

The developer day was filled with conversations with wielders of open data of
various flavors; [Crowd Sourcerers](http://seeclickfix.com), API Prospectors,
GIS and Transit Wonks, and some good ol' fashioned IT Staffers. Many I had
seen on the [Barcamp](http://barcamp.org) or [Tech
Pres](http://personaldemocracy.com) Circuit, even a few who's code was being
leveraged by our stack. After a bit of welcome and housekeeping,the thing that
really stuck with me, even some days later, was the Standard Unconference
Crowd Introduction; Name, Affiliation, and 3 words. As the Microphone Snaked
it's way through the rows, each member self identified. The thing that struck
me, was hearing the words each person--hacker or not--chose as their 3.

Of all the choices, the top 2 answers I heard were "Collaboration", and
surprisingly "Opensource." This, to me, was rather unexpected, as I in my
limited research, please link me if I missed anyone, had yet to hear of many
other departments or administrations other than the NYSSCIO team leveraging
real Opensource apps or CMS's* (*disclaimer for all the folks out there
rocking apache or other "under the hood" open tools for the purposes of
sysadminery.) There were some folks who chose words like "fun", one triathlete
type with "Peddle-paddle-swim", a few "creatives", but also a large amount of
"Accountability", "Security", and "Reliability" as well. (This author chose
"from python import *" on the first day (even though it was in fact 4 words)
and developer-driven, code-centric, hacktivism on the second). The mention of
Opensource or collaboration, in conjunction with any of the other terms
though, was most notable, as introductions last year were not indicative of
this year's trend of new-found adoption.

Each project, once identified either through the [CapitolCampTrack
wiki](http://barcamp.org/CapitolCampTracks), or in the tradition of
unconfrencing, walked up to the front of the room to pitch talks and choose
blocks. Immediately, regardless of stripes or station, each of the
representatives who were hacker types huddled together and queried eachother
on what languages they had in their Stacks.
[SeeClickFix](http://seeclickfix.com) and [Democracy
Maps](http://pages.e-democracy.org/DemocracyMap) claimed [Ruby](http://www
.ruby-lang.org/en/). Myself and my associate James Turk (author of the
Sunlight Python API) knew what we were going to be repping. So it was settled
behind the microphone stand that the contingents would each get paired into
their own room. (In hindsight, it may have been a good idea to all stick
together for participation sake, but I'm the type of guy who isn't afraid to
spoil the soup with too many cooks.) It was settled thereafter that there
would be a session by the Senate CIO team on the OpenLegislation API, and

the new version they will be rolling out soon, along with some general
background on some of the Mobile App and Drupal development that happens in
their shop. After would be a 3 block hacksession, with a break-out for GIS and
GeoStack related stuff with the DemocracyMaps and SeeClickFix teams, and then
some more open discussions about social media, and more Drupal from the Senate
CIO Team.

After the schedule was settled and the camp broke for its first sessions, it
was established that there were going to be some "particularities" about the
network. For instance, our version of the civx beta was being hosted on port
9999 from our development machine, which was later determined to be blocked,
along with pretty much every port but port 80 (and ofcourse port 6777, which
was the port that IRC was running on, and subsequently became the port that we
served the beta to... gotta love paster) After spending much of the day
tweaking the beta and populating the navigation of the site, we finally had a
chance to crack open the OpenStates (formerly known as FiftyStates) API, and
see what sorts of NY related info we could dive into. After a brief discussion
with Turk and his compatriots, it was decided that since the OpenLeg 1.0 API
was not going to be supported indefinitely, and the senate was rolling out
their 2.0 in the very near future, OpenStates would wait to start scraping NY.
In the meantime, there was already some state related data, and we toyed with
some API calls querying out some simple JSON dumps in CIVX-land for future use
in widgets when the time comes.

By the end of the day, we had migrated, and were ready to present our
NYSenate.gov Dashboard. We considered it a "soft drop," meaning we didn't want
to show off too much of it and steal our own thunder for the next day's
capitol camp track, but we still got to show off some pretty shiny code to a
crowd of fellow opengov kin.

The after bar party at the Victory Cafe was wonderful. We had quite a
gathering of folk from each camp, representing a variety of flavors and layers
in the stack. First of all, it was worth mentioning that they were out of
Guiness, and that after ordering a Smithix in its stead, sadly, that tap too,
was on its last legs. Both of these scenarios were easily remedied by our
server, whom was doing a wonderful job tending to the sizable band of us, and
the rest of the patrons too for that matter. After a spot of rain, we all
migrated to the dining room proper of the establishment, and put in orders
just in time for the last (or what we thought was the last--shout out Nate) of
the CIVX team and Storytellers.

Not a whole mess of photos could adequately document the whole mess of food
that was ordered from around the table. These were the bacon cheddar fries,
not pictured are the delectable sweet potato fries with the marshmallow
dipping sauce... om nom nom

![](http://farm5.static.flickr.com/4117/4926780052_2e59949d29_m.jpg)

After some proper parlaying at the table upon a cornucopia of code bases,
licensing paths, and all brands of politicking, it occurred to me that a large
portion of the folks sitting around the horn, were also repping some form
[tiger stripes](http://rit.edu) or [another](http://rit.edu/alumni).

After some rather decent pub and grub, most of the teams scattered to the
winds, a few surlier louts hung around for a few extra moments, (and maybe a
few extra after that), continuing on rampantly across the spectrum of
distrology, BDFLs, doing it right, and failure to fail early.

The next day bright and early we started all over again. Stay tuned for Part
II.

AttachmentSize

[emplazacrop.png](http://foss.rit.edu/files/emplazacrop.png)

221.63 KB

