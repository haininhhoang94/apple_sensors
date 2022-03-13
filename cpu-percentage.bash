top -l  2 | grep -E "^CPU" | tail -1 | awk '{ print "CPU: "$3 + $5"%" }'
