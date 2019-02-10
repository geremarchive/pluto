#!/bin/sh

curl https://raw.githubusercontent.com/geremachek/pluto/master/pluto.bin > pluto.bin
curl https://raw.githubusercontent.com/geremachek/pluto/master/config > config
chmod +x pluto.bin

sudo mv pluto.bin /usr/bin/pluto

if [ ! -d $HOME/.config ]
then
	mkdir $HOME/.config
fi

mkdir $HOME/.config/pluto
mv config $HOME/.config/pluto/config

printf "\033[1;32mPluto has been installed!\033[0m\n"
