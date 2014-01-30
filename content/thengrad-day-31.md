Title: Day 31
Date: 2013-07-11T11:20:00
Slug: thengrad-day-31
Author: thengrad
Tags: legacy, foss@rit
Category: legacy
Summary: After not paying attention and eating food that went bad last night I wasn't ... 

After not paying attention and eating food that went bad last night I wasn't
feeling all that well today. I tried to remain as productive as possible even
with the nausea. I was looking for the elusive problem that was cause the game
to only sell basic lemonade even though I switched the recipe. It took me a
while to notice that the way the properties referenced the class variables
were not updating properly so that even thought the one property was changing
the value the other property wasn't picking up on the change. To fix this I
had to have the property that access a subset of another class variable call
the property for that variable instead of the variable itself. I had to go
through and change about four of the the properties so that they wouldn't run
into this problem as well.

