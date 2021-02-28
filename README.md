# SleepTracker
Script I run to track my sleep during the pandemic.

My requirements with this project were something easy to setup, something that I could do from my phone right before I sleep, and something that would be quick to input.

This meant that I couldn't just run a script from my computer everytime I went to sleep. This also meant I couldn't be entering a date into a spreadsheet everytime I went to sleep because that would take too long.

In the end, I decided to go with this solution:
When I go to sleep, wake up, or decide I can't sleep, I sent either an "s", "w", or "c" respectively to a text channel on my private Discord server. Then occasionally I run the sleep.py script which records all the messages since the last time I ran the script. Another feature is that in case I forget to send the message, I can also input the estimated time that I went to sleep or woke up or couldn't sleep and it'll record that time rather than the time I sent the message at.