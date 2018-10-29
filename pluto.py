#!/usr/bin/env python3

from curses import *
from os import *
from sys import *
import os.path

cwd = getcwd()
cfiles = listdir(cwd)

index=0

while index < len(cfiles):
    files = cfiles[index]
    if files[0] == ".":
        cfiles.pop(cfiles.index(files))
    else:
        index += 1

s = initscr()

new=[]

scrolled = False

start_color()

use_default_colors()

curs_set(0)

for i in range(0, 256):
    init_pair(i + 1, i, -1)

my, mx = s.getmaxyx()

noecho()
s.keypad(1)

count=0

sc1 = my-2
sc2 = 0

for files in cfiles:
    if count != my-2:
        count += 1
        s.move(count, 1)
        if os.path.isdir(files):
            s.addstr(files, color_pair(13))
        else:
            s.addstr(files, color_pair(0))
        s.move(count,1)
    else:
        break

s.move(1,1)

if os.path.isdir(cfiles[0]):
    s.addstr(cfiles[0], color_pair(13) + A_REVERSE)
    s.move(1,1)
else:
    s.addstr(cfiles[0], color_pair(0) + A_REVERSE)
    s.move(1,1)

cfile = 0
cy, cx = 1, 1

while True:
    key = s.getch()
    if key == ord("q"):
        endwin()
        exit()
    elif key == KEY_DOWN:
        if cfile != len(cfiles)-1 and cy != my-2 and scrolled == False:
            if os.path.isdir(cfiles[cfile]):
                s.addstr(cfiles[cfile], color_pair(13))
                s.move(cy,1)
            else:
                s.addstr(cfiles[cfile], color_pair(0))
                s.move(cy,1)

            cfile += 1
            cy += 1 
            s.move(cy, 1)
            if os.path.isdir(cfiles[cfile]):
                s.addstr(cfiles[cfile], color_pair(13) + A_REVERSE)
                s.move(cy,1)
            else:
                s.addstr(cfiles[cfile], color_pair(0) + A_REVERSE)
                s.move(cy,1)
        else:
            if cfile == len(cfiles)-1 or new[-1:] == cfiles[-1:] and cy == my-2:
                continue
            elif cy == my-2:
                scrolled = True
                s.clear()
                sc2 += 1
                sc1 += 1
                new = cfiles[sc2:sc1]
                s.move(1,1)
                count=0
                for files in new:
                    if count != my-2:
                        count += 1
                        s.move(count, 1)
                        if os.path.isdir(files):
                            s.addstr(files, color_pair(13))
                        else:
                            s.addstr(files, color_pair(0))
                            s.move(count,1)
                    else:
                        break

                if os.path.isdir(new[cfile]):
                    s.addstr(new[cfile], color_pair(13) + A_REVERSE)
                    s.move(cy,cx)
                else:
                    s.addstr(new[cfile], color_pair(0) + A_REVERSE)
                    s.move(cy,cx)
            elif cy != my-2 and scrolled == True:
                if os.path.isdir(new[cfile]):
                    s.addstr(new[cfile], color_pair(13))
                    s.move(cy,1)
                else:
                    s.addstr(new[cfile], color_pair(0))
                    s.move(cy,1)

                cfile += 1
                cy += 1 
                s.move(cy, 1)
                if os.path.isdir(new[cfile]):
                    s.addstr(new[cfile], color_pair(13) + A_REVERSE)
                    s.move(cy,1)
                else:
                    s.addstr(new[cfile], color_pair(0) + A_REVERSE)
                    s.move(cy,1)
                
    elif key == KEY_UP:
            if cfile != 0 and cy != 1 and scrolled == False:
                if os.path.isdir(cfiles[cfile]):
                    s.addstr(cfiles[cfile], color_pair(13))
                    s.move(cy,cx)
                else:
                    s.addstr(cfiles[cfile], color_pair(0))
                    s.move(cy,cx)

                cfile -= 1
                cy -= 1 
                s.move(cy, 1)
                if os.path.isdir(cfiles[cfile]):
                    s.addstr(cfiles[cfile], color_pair(13) + A_REVERSE)
                    s.move(cy,cx)
                else:
                    s.addstr(cfiles[cfile], color_pair(0) + A_REVERSE)
                    s.move(cy,cx)
            else:
                if scrolled == False:
                    continue
                elif scrolled == True:
                    if cy != 1:
                        if os.path.isdir(new[cfile]):
                            s.addstr(new[cfile], color_pair(13))
                            s.move(cy,cx)
                        else:
                            s.addstr(new[cfile], color_pair(0))
                            s.move(cy,cx)

                        cfile -= 1
                        cy -= 1 
                        s.move(cy, 1)
                        if os.path.isdir(new[cfile]):
                            s.addstr(new[cfile], color_pair(13) + A_REVERSE)
                            s.move(cy,cx)
                        else:
                            s.addstr(new[cfile], color_pair(0) + A_REVERSE)
                            s.move(cy,cx)
                    elif cy == 1 and cfiles[0] != new[0]:
                        s.clear()
                        sc2 -= 1
                        sc1 -= 1
                        new = cfiles[sc2:sc1]
                        s.move(1,1)
                        count=0
                        for files in new:
                            if count != my-2:
                                count += 1
                                s.move(count, 1)
                                if os.path.isdir(files):
                                    s.addstr(files, color_pair(13))
                                else:
                                    s.addstr(files, color_pair(0))
                                    s.move(count,1)
                            else:
                                break

                        s.move(1,1)
                        cfile=0

                        if os.path.isdir(new[cfile]):
                            s.addstr(new[cfile], color_pair(13) + A_REVERSE)
                            s.move(cy,cx)
                        else:
                            s.addstr(new[cfile], color_pair(0) + A_REVERSE)
                            s.move(cy,cx)
                    else:
                        continue

    elif key == KEY_RIGHT:
        if os.path.isdir(cfiles[cfile]):
            scrolled = False
            s.clear()
            s.refresh()
            chdir(cfiles[cfile])
            cwd = getcwd()
            cfiles.clear()
            cfiles = listdir(cwd)
            cfile = 0
            cy, cx = 1, 1
            s.move(1,1)            

            count=0

            index=0

            while index < len(cfiles):
                files = cfiles[index]
                if files[0] == ".":
                    cfiles.pop(cfiles.index(files))
                else:
                    index += 1

            for files in cfiles:
                if count != my-2:
                    count += 1
                    s.move(count, 1)
                    if os.path.isdir(files):
                        s.addstr(files, color_pair(13))
                    else:
                        s.addstr(files, color_pair(0))
                    s.move(count,1)
                else:
                    break
            
            s.move(1,1)            

            if os.path.isdir(cfiles[0]):
                s.addstr(cfiles[0], color_pair(13) + A_REVERSE)
                s.move(1,1)
            else:
                s.addstr(cfiles[0], color_pair(0) + A_REVERSE)
                s.move(1,1)
        else:
            continue
    elif key == KEY_LEFT:
        scrolled = False
        s.clear()
        s.refresh()
        chdir("..")
        cwd = getcwd()
        cfiles.clear()
        cfiles = listdir(cwd)
        cfile = 0
        cy, cx = 1, 1
        s.move(1,1)            

        count=0

        index=0

        while index < len(cfiles):
            files = cfiles[index]
            if files[0] == ".":
                cfiles.pop(cfiles.index(files))
            else:
                index += 1

        for files in cfiles:
            if count != my-2:
                count += 1
                s.move(count, 1)
                if os.path.isdir(files):
                    s.addstr(files, color_pair(13))
                else:
                    s.addstr(files, color_pair(0))
                s.move(count,1)
            else:
                break
            
        s.move(1,1)            

        if os.path.isdir(cfiles[0]):
            s.addstr(cfiles[0], color_pair(13) + A_REVERSE)
            s.move(1,1)
        else:
            s.addstr(cfiles[0], color_pair(0) + A_REVERSE)
            s.move(1,1)       
    else:
        continue

endwin()
