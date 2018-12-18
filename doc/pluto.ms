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
.B ~/.config/pluto/config
file and a standard
.B ~/.config/pluto/themes
folder with the all default themes. You can also choose an "minimal" install option that creates and empty
.B ~/.config/pluto/config
and an empty
.B ~/.config/pluto/themes .
.CH
Configuration
.RC
.CT
~/.config/pluto/config
.RC
.PP
As mentioned before, pluto comes with a config file in the home directory. This config file
contains different variables that corespond to different aspects of pluto that can be
configured with the following arguments.
.RC
.IP \(bu
sel [bold, rev, dim, underline] - Changes how items are selected
.IP \(bu
theme [Any .plut file in ~/.config/pluto/themes] - Changes the theme
.IP \(bu
exit [any character] - Changes the key for exiting
.IP \(bu
del [any character] - Changes the key for deleteing a file
.IP \(bu
show-hidden [true, false] - Show dotfiles by default
.IP \(bu
toggle-hidden [any character] - Show/hide dotfiles
.IP \(bu
up [up, any character] - Changes the key for the up function
.IP \(bu
down [down, any character] - Changes the key for the down function
.IP \(bu
left [left, any character] - Changes the key for the left function
.IP \(bu
right [right, any character] - Changes the key for the right function
.IP \(bu
move [any character] - Changes the key for the move function
.CT
~/.config/pluto/themes
.RC
.PP
All color configuration takes place in 
.B .plut
files in the 
.B themes
directory
it uses the same varible system but has different varibles. They are:
.RC
.IP \(bu
file [0-256] - Changes the color of files
.IP \(bu
dir [0-256] - Changes the color directories
.IP \(bu
cwd-color [0-256] - Changes the color of the cwd
.IP \(bu
cwd-format [bold, rev, dim, underline]
.CH
Macros
.RC
.CT
Directory Macros
.RC
.PP
Macros allow the user to move to any directory with a simple keypress.
Macros a formated like
.B macro:/path/to/dir=key
