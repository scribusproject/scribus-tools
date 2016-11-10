#!/bin/bash
# simple script to download an attachment (which in our case is a patch) from a mantisbt ticket

# define usage function
usage(){
	echo "Usage: $0 http://path/to/mantis/patch"
	exit 1
}

# invoke  usage
# call usage() function if URL not supplied
[[ $# -eq 0 ]] && usage

wget --no-check-certificate --user-agent="Firefox" -O 1.patch $1 
