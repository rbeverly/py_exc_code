import schedule
import time
import os
import pottery

# Executes super important pottery routine every minute.
# But we want some consistent pottery and also some
# more experimental pottery!

def make_consistent():
	pottery.make()

def make_wabisabi():
	os.system("python -c 'import pottery; pottery.make()'")

schedule.every(1).minutes.do(make_consistent)
schedule.every(1).minutes.do(make_wabisabi)

while True:
	schedule.run_pending()
	time.sleep(1)