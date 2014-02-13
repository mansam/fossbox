Title: Moving On...
Date: 2010-06-17T10:08:00
Slug: DaveSilver-moving-on
Author: DaveSilver
Tags: legacy, foss@rit
Category: legacy
URL: articles/DaveSilver/moving-on.html
save_as: articles/DaveSilver/moving-on.html
Summary: So as I said with previous entries, JT is working on making an all encompassing test for file types. Essentially the test will allow us to run all of our previous tests from one executable file. While he does that, I am moving on to trying to create a test that will allow us to test various different animation styles. What I mean by this, is we will be comparing having each frame as a separate image, multiple different types of sprite sheets, etc. Our goal is to know not only which image format  ... 

So as I said with previous entries, JT is working on making an all
encompassing test for file types. Essentially the test will allow us to run
all of our previous tests from one executable file. While he does that, I am
moving on to trying to create a test that will allow us to test various
different animation styles. What I mean by this, is we will be comparing
having each frame as a separate image, multiple different types of sprite
sheets, etc. Our goal is to know not only which image format will work best,
but also what the best way to use that image format is.

In other news, I have made a bar graph of our tests of image scaling. I am
currently working on finishing up the rest of the bar graphs but I figured
that for now I would at least post this one. [This is the graph
here.](http://img687.imageshack.us/img687/3299/scalingchart.png) The test we
did was pretty simple. Basically we had 4 image sets in each format at various
sizes and then we re-sized them all to the original image size. Then we looked
at the frame rate to see how it was affected by the scaling calculations. On
the chart the percent next to each format represents the size of the image
before it was scaled down. So the 200% images were 2 times the size of the
original image. The blue bar represents the average frame rate of the images
and the orange bar represents the average file size of the images. From this
test we essentially discovered that scaling is not a great option but I
thought I would post the chart for you guys to see anyway.

