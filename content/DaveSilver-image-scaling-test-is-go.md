Title: Image Scaling Test Is Go...
Date: 2010-06-15T14:01:00
Slug: DaveSilver-image-scaling-test-is-go
Author: DaveSilver
Tags: legacy, foss@rit
Category: legacy
Summary: So JT and I spent today making a new testing file that is specific to scalability testing. First we ditched JPGs, and 32 bit BMPs because they were having problems and were just overall not viable formats. Then we made versions of every remaining image format at 4 different resolutions, 1 set at the original resolution, 1 set at a resolution that was 2 times as large, 1 set at a resolution that was 4 times as large, and finally 1 set at a resolution that was 1.73 times as large so that if the fu ... 

So JT and I spent today making a new testing file that is specific to
scalability testing. First we ditched JPGs, and 32 bit BMPs because they were
having problems and were just overall not viable formats. Then we made
versions of every remaining image format at 4 different resolutions, 1 set at
the original resolution, 1 set at a resolution that was 2 times as large, 1
set at a resolution that was 4 times as large, and finally 1 set at a
resolution that was 1.73 times as large so that if the functions we were using
to scale the images had built in optimization techniques, that image would
still give it a "run for its money", so to speak. After we had all of the new
images we created a new version of the testing program that allowed us to
scale all of the images to any size we wanted. We then ran the test and scaled
every image to the original image size.

The goal with this test was to determine if scaling images through the code is
a viable option. Ideally, if it turned out that scaling the images through the
code did not cause a major slowdown, software creators would have the ability
to create one image set at the highest resolution they needed, and then just
scale the images down to accommodate lower resolutions. This would be helpful
because it would drastically decrease hard-drive capacity needed for the game.
The only negative that would come about from this situation would be that the
images would lose detail when being scaled down. In theory though, this would
not be that big of a deal and would be a viable sacrifice considering the
upsides.

We are running the tests now and I will update the blog when we have our
results.

