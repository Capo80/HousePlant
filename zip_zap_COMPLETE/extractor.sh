#!/bin/sh

for i in `seq 1 1`
do
	for f in extr_dir/*
	do
		A="$(echo $f | cut -d'/' -f2)"
		echo $A
		case "$(echo $A | cut -d'.' -f2)" in
		    "zip") echo "zip" ;;
		    "gz") unzip $f ;;
		    "tar") echo "tar" ;;
		    *)   echo "not found" ;;
		esac
		rm $f
	done
done