Title: libtelepathy on the XO
Date: 2012-03-16T20:38:00
Slug: imnotlistening-libtelepathy-on-the-xo
Author: imnotlistening
Tags: legacy, foss@rit
Category: legacy
Summary: ## Telepathy-glib ... 

## Telepathy-glib

To make life easier I am going to use lib telepathy for dealing with the
separate chat protocols and features and what not. Libtelepathy greatly
reduces the effort required for developing a full featured communication
program, e.g: IM, VoIP, and video chat/conferencing. Many major applications
these days are now using it as a back end. The XO file system does have a
telepathy package in the yum repositories, however it is not the latest and
greatest. There has been lots of recent and good progress on libtelepathy, so
getting the latest code on the XO is a high priority.

## Telepathy dependencies

The latest version of telepathy I compiled required a later version of a few
packages not present in the XO yum repositories: glib and glibs dep, gettext.

Compiling these two libraries was very straight forward. In my XO dev
environment:

#### gettext

`

$ tar -xzf gettext-0.18.1.1.tar.gz

$ cd gettext-0.18.1.1

$ ./configure --disable-nls

$ make

# make install

`

#### glib-2

`

$ tar -xjf glib-2.28.8.tar.bz2

$ cd glib-2.28.8

$ export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig

$ ./configure

$ make

# make install

`

## And finally, compiling telepathy

Compiling telepathy was just as easy.

`

$ tar -xzf telepathy-glib-0.17.4.tar.gz

$ cd telepathy-glib-0.17.4

$ ./configure

$ make

# make install

`

## Installing Telepathy on the XOs

Since I don't want to overwrite any previous libraries, I went ahead and used
the default install prefix of all the libraries in /usr/local. Thus to install
the libraries on the XO, I simply copied /usr/local/lib/* to the XO.

From the 32 bit VM:

`

$ cd /usr/local

$ rsync -rav lib australia.student.rit.edu:/mnt/dm-0/olpc-dev/

`

From the XO:

`

$ su

# cd /usr/local/lib

# rsync -ravl australia.student.rit.edu:/mnt/dm-0/olpc-dev/lib/* .

`

Yay, we are done. I think. More on this later.

