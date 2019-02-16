from curses import *
import os.path
from os import *
import io

keyMaps = {
}

fileColors = {
}

openFiles = {
}

cwd = getcwd()
home = os.path.expanduser('~') 
chdir(home)
if os.path.isfile(home + '/.config/pluto/config'):
    chdir('.config/pluto')
    with io.open('config', 'r') as config:
        for line in config:
            command = line.split(' ')[0]
            if command == "#" or line.isspace() or line == "\n" or line == "":
                pass
            elif command == "dir-slash":
                if line.split(' ')[1].rstrip() == "true":
                    dirSlash = True
                elif line.split(' ')[1].rstrip == "false":
                    dirSlash = False
                else:
                    pass
            elif command == "select-type":
                if line.split(' ')[1].rstrip() == 'reverse':
                    selType = A_REVERSE
                elif line.split(' ')[1].rstrip() == 'dim':
                    selType = A_DIM
                elif line.split(' ')[1].rstrip() == "underline":
                    selType = A_UNDERLINE
                else:
                    pass
            elif command == "bar":
                if line.split(' ')[1].rstrip() == 'true':
                    barEnable = True
                elif line.split(' ')[1].rstrip() == 'false':
                    barEnable = False
                else:
                    pass
            elif command == "side-offset":
                sideOffset = int(line.split(' ')[1].rstrip())
            elif command == "top-offset":
                topOffset = int(line.split(' ')[1].rstrip())
            elif command == "bottom-offset":
                bottomOffset = int(line.split(' ')[1].rstrip())
            elif command == "bar-locale":
                barLocale = str(line.split(' ')[1].rstrip())
            elif command == "barx":
                barX = int(line.split(' ')[1].rstrip())
            elif command == "bary":
                barY = int(line.split(' ')[1].rstrip())
            elif command == "bar-color":
                barColor = int(line.split(' ')[1].rstrip())
            elif command == "bar-format":
                if line.split(' ')[1].rstrip() == "reverse":
                    barFormat = A_REVERSE
                elif line.split(' ')[1].rstrip() == "bold":
                    barFormat = A_BOLD
                elif line.split(' ')[1].rstrip() == "dim":
                    barFormat = A_DIM
                elif line.split(' ')[1].rstrip() == "none":
                    barFormat = A_NORMAL
            elif command == "color":
                fileColors[line.split(' ')[1].rstrip()] = int(line.split(' ')[2].rstrip())
            elif command == "open":
                openFiles[line.split(' ')[2].rstrip()] = [str(line.split(' ')[3].rstrip()), str(line.split(' ')[1].rstrip())]
            elif command == "bind":
                if line.split(' ')[1].rstrip() == "up":
                    keyMaps[line.split(' ')[2].rstrip()] = KEY_UP
                elif line.split(' ')[1].rstrip() == "down":
                    keyMaps[line.split(' ')[2].rstrip()] = KEY_DOWN
                elif line.split(' ')[1].rstrip() == "left":
                    keyMaps[line.split(' ')[2].rstrip()] = KEY_LEFT
                elif line.split(' ')[1].rstrip() == "right":
                    keyMaps[line.split(' ')[2].rstrip()] = KEY_RIGHT
                elif line.split(' ')[1].rstrip() == "space":
                    keyMaps[line.split(' ')[2].rstrip()] = ord(" ")
                else:
                    keyMaps[line.split(' ')[2].rstrip()] = ord(str(line.split(' ')[1].rstrip()))
            else:
                print("\033[31;1;3mError:\033[0m " + line.rstrip())
                exit()
chdir(cwd)
