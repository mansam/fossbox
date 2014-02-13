Title: Tales of Thor's Day
Date: 2010-07-22T14:06:00
Slug: jtmengel-tales-of-thors-day
Author: jtmengel
Tags: legacy, foss@rit
Category: legacy
URL: articles/jtmengel/tales-of-thors-day.html
save_as: articles/jtmengel/tales-of-thors-day.html
Summary: Alright, time for the Thor's Day Blog, also know as Thursday by some nations that don't recognize the day's pagan origins. Ahem, but anyways, today was a day of killing off the tests we started yesterday on using classes, inheriting sprite, in conjunction with dirty lists.  In case I'm not making sense, we finished the tests to confirm that we could effectively speed things up by doing A) storing all the relevant information pertaining to the image for easy access B) allowing us to intelligently ... 

Alright, time for the Thor's Day Blog, also know as Thursday by some nations
that don't recognize the day's pagan origins. Ahem, but anyways, today was a
day of killing off the tests we started yesterday on using classes, inheriting
sprite, in conjunction with dirty lists.

In case I'm not making sense, we finished the tests to confirm that we could
effectively speed things up by doing A) storing all the relevant information
pertaining to the image for easy access B) allowing us to intelligently access
a sprite grouping method RenderUpdates which would ensure that we wouldn't
draw overlapping rectangles and of course C) modify our Sprites to function
precisely how we need for easy and efficient implementation into the Game
Engine of Fortune Hunter.

After the tests, Dave and I dolled out responsibilities for the next 2 weeks
and while we'll be working together (in the same room/desk) we won't be
working with each other (on the same project). Since I arbitrarily chose to
infer that there's a difference between working "with each other" and
"together", here's what we'll be working on in the near future:

Dave: Polish up Drawable Object and incorporate the RenderUpdates group into
the code. Since this is a significant amount of code and potential loss-of-
sanity, Dave will just have one large project to take on.

JT (the charming and cunning blogger you're reading right now): I'll be taking
on Collapsing the last few tests into our test 'suite' (I just want to call it
a 'suite', it might be more accurate to replace it with 'kinda nice test
program')

This means including our rotate test, our multiple Dirty Sprite Tests, and
finally the dreaded SVG tests (which is currently still on the drawing board
so to speak)

Just a quick note: The SVG data collection is going to be a two-parter where
only the second part will be programmed into Python; The first part will rely
on me taking sample art assets of varying sizes and complexity (as well as
possibly finding and citing resources online) to define what type of size
discrepencies you can expect converting from SVG's to rendered formats.

That being said, if anyone has a suggestion on where to start my research on
SVG conversion (or materials explaining the details of SVGs might be equally
helpful) please let me know via email at
[JTMengel@gmail.com](mailto:JTMengel@gmail.com)

