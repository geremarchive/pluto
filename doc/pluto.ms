.defcolor dr rgb #af2123
.defcolor db rgb #331987

.de CH
.NH
.gcolor dr
..

.de CT
.NH 2
.gcolor dr
..

.de RC
.gcolor black
..

.TL
.ps 20
.gcolor dr
 Pluto - The Customizable File Manager
.gcolor black
.AU
.gcolor db
.ps 15
Geremachek
.gcolor black
.AI
.ps 10
geremachek.io
.CH
Installation
.RC
.CT
Downloading And Extracting
.RC
.PP
You can download pluto at
.gcolor blue
.UL http://geremachek.io/repos/pluto.tar.gz
.RC
It doesn't matter where you extract this tar ball.
.CT
Setting it Up
.gcolor black
.PP
The pluto.tar.gz file not only contains the pluto executable, but a 
.B setup.sh 
script aswell. This script acts as an installer for pluto. The script will give the user
a choice between a "default" installation that will move pluto to your path and 
generate a standard
.B ~/.plutorc
file and a standard
.B ~/.pluto/themes
folder with the all default themes. You can also choose an "advanced" install option
that lets the user choose what
.B ~/.plutorc
options you want aswell as what themes to install in
.B ~/.pluto/themes .
.CH
Configuration
.RC
.CT
~/.plutorc
.RC
.PP
As mentioned before, pluto comes with a rc file in the home directory. This rc file
contains different "tags" that corespond to different aspects of pluto that can be
configured with the following argument.
.RC
