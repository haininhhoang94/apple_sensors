ps -A -o %cpu,%mem | awk '{ mem += $2} END {print "RAM: " mem "%"}'