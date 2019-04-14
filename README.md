<h1 align="center"><i>Pluto</i></h1>
 
<p align="center">A simple and rice-able file manager.</center>

<h1 align="center"><i>Features</i></h1>

* Fast (Compiled Python Code)
* Configurable, you can map any key to any function or script to improve your workflow
* Automatic screen resize
* Instantly open files in your favorite terminal or GUI programs
* Simple

<center>
<a href="https://asciinema.org/a/224295" target="_blank"><img src="https://asciinema.org/a/224295.svg" /></a>
</center>

<p align="center">Pluto running with my configs</p>

<h1 align="center"><i>Installing Pluto</i></h1>

```shell
curl "https://raw.githubusercontent.com/geremachek/pluto/master/install.sh" | sh
```

<h1 align="center"><i>Configuring Pluto</i></h1>

A configuration file is located in ```~/.config/pluto```. This allows you to optomize pluto for your workflow

## Miscellaneous

* ```dir-slash [true/false]```
> Enable the slash on the end of directories
* ```select-type [reverse/bold/dim]
> Change how files are visually selected

## Bar

* ```bar [true/false]```
> Enable the bar
* ```bar-locale [bottom/top]```
> Change the location of the bar
* ```barx [n]```
> Set bar x offset to n
* ```bary [n]```
> Set bar y offset to n
* ```bar-color [n]```
> Set bar color to n
* ```bar-format [reverse/bold/dim/none]```
> Change how the bar is formated

## Offset

* ```side-offset [n]```
> Set the element x offset to n
* ```top-offset [n]```
> Set the offset of the top of the elements to n
* ```bottom-offset [n]```
> Set the offset of the bottom of the elements to n

## Binding

* ```bind [key] [action]```
> Bind a key to an action
* ```bind [key] cd:[path]```
> Bind key to a directory jump to path
* ```bind [key] script:[script]```
> Bind key to the execution of script on selected file

## Opening Files

* ```open term [file/file extension] [program]```
> Open any matching file extension or every file with program in a terminal
* ```open back [file/file extension] [program]```
> Open any matching file extension or every file with program in a GUI or background process

## Colors

* ```color [dir/file/file extension] n```
> Set the color of any file, dir or matching file extension to n

## Arrow
* ```arrow-select [true/false]
> Enable arrow select
* ```arrow [string]```
> Define what the arrow is
* ```arrow-color [n]```
> Define what color the arrow is
