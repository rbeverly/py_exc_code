# README

If you modify pottery.py while timer.py is running, you'll see the original version running as an imported module (until you restart timer.py), and you'll also see the modified version running as a separate process using os.system().

Of course, the separate process executes whatever the most recent version of the code is. 

This is just a simple demonstration for educational purposes.