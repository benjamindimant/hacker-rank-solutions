#!/bin/bash

read
arr=($(cat))
str=${arr[@]}
echo $((${str// /^}))}} # double // replaces all occurences of space with ^
