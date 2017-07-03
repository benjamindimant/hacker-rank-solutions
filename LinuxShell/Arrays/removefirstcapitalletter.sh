#!/bin/bash

a=($(cat))
echo ${a[@]/[[:upper:]]/.}}
