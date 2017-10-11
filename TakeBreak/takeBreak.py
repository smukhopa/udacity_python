import time
import webbrowser

total_breaks = 3
break_count = 0

print "Start time: " + time.ctime()
while break_count < total_breaks:
    time.sleep(3)
    webbrowser.open("https://www.google.com/")
    break_count += 1

print "Finished"

