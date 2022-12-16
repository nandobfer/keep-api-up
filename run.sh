#!/bin/bash

cd $1

screen -X -S api kill
screen -X -S api-http kill

screen -m -d -S api yarn start
screen -m -d -S api-http yarn dev