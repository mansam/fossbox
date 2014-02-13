Title: Finally have time to start this project.
Date: 2012-03-16T19:55:00
Slug: imnotlistening-finally-have-time-to-start-this-project
Author: imnotlistening
Tags: legacy, foss@rit
Category: legacy
URL: articles/imnotlistening/finally-have-time-to-start-this-project.html
save_as: articles/imnotlistening/finally-have-time-to-start-this-project.html
Summary: Finally... Its spring quarter and I have some time to get a native video chat app running on an XO. There is a lot of talk about the OVC application created by a couple of RIT students: [http://foss.rit.edu/projects/ovc](http://foss.rit.edu/projects/ovc). While they work on the python implementation, I am going to detail my progress towards building a native C application.  To start of with, here is how I set up my development environment for writing/compiling XO code. I don't know if there are  ... 

Finally... Its spring quarter and I have some time to get a native video chat
app running on an XO. There is a lot of talk about the OVC application created
by a couple of RIT students:
[http://foss.rit.edu/projects/ovc](http://foss.rit.edu/projects/ovc). While
they work on the python implementation, I am going to detail my progress
towards building a native C application.

To start of with, here is how I set up my development environment for
writing/compiling XO code. I don't know if there are better ways or not, but
this worked for me. This is all based on the guide posted here: [http://wiki.l
aptop.org/go/Compiling_C/C%2B%2B_program_for_the_OLPC](http://wiki.laptop.org/
go/Compiling_C/C%2B%2B_program_for_the_OLPC). Here are the basic steps (I will
describe each on more detail after):

`

1. Build 32 bit VM for building code with a native XO file system copy.

2. Copy the XO file system from an XO onto the VM.

3. chroot into the copied XO file system.

4. Configure the XO chroot environment, install some dev software and
configure a user account to your liking.

`

### 1. Getting a 32 bit kernel running

This step was necessary since I am running a 64 bit OS (Fedora 12) on my
machine. However, to chroot into a 32 bit device, the kernel's 32bitness must
match. Thus I needed a dev environment that used a 32 bit kernel. The easiest
way to do this was, by far, to make a 32 bit VM (Fedora 16).

### 2. Copy the file system off the XO.

To copy the data of the the XO, I copied from the XO to my computer via rsync.
I used the commands from the guide on wiki.laptop.org with a few changes:

On my desktop:

`

$ cd /mnt/dm-0/olpc-dev

$ mkdir olpc-root

$ mkdir -p olpc-root/proc

$ mkdir olpc-root/dev

$ su

# mknod olpc/dev/null c 1 3

# chmod 666 olpc/dev/null

`

On the XO:

`

$ su

# cd /

# rsync -a bin sbin lib usr etc home var australia.student.rit.edu:/mnt/dm-0
/olpc-dev/olpc-root

# rsync -a proc/cpuinfo australia.student.rit.edu:/mnt/dm-0/olpc-dev/olpc-
root/proc

`

At this point, I had all the important stuff for compiling against an OLPC
laptop on my 64 bit desktop. From there I copied the FS I had built verbatim
to the 32 bit VM.

### 3. chroot

This sets me up in a shell that is effectively running on an XO laptop only
the underlying hardware is a little more beefy. Not much though, my VM is not
particularly quick. However, there is enough disk space to compile lots of
libraries and the like. On the 32 bit VM:

`

$ su

# chroot olpc-root

#

`

### 4. Configuring a user account for myself

Now that I have a chroot'able build environment for cross compiling (well,
sort of cross compiling) I installed some software using yum; some was
necessary for development, some just for comfort and ease of use.

Necessary software (may already be installed though):

- gcc  
- make  
- glib-devel  
- gtk2-devel

Comfort software:

- zsh  
- emacs

### Notes

Unfortunately the 32 bit VM along with a chroot environment is pretty slow.
Unfortunately for my setup there really is nothing I can do about this other
than installing a native 32 bit system. But I don't want to go there.

For now at least, this has accomplished everything I have needed for
developing C code against gtk. I will go into more detail on how I compiled
and installed the latest telepathy library and dependencies.

