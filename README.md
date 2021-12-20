# Soundboard

A good team artifact to have present in a room of developers. Use with your own sounds dependent on the team humor!
With inspiration from the almighty CANDI team, and published by BNJ software (https://www.linkedin.com/posts/it-minds_4-tips-til-en-produktiv-udviklingsproces-activity-6872113379411013632-krpk)

A simple python application that takes a sound (from the sounds folder) started with a letter typed on the keyboard, and plays it. E.g.

Running main.py and see the console showing:
"Ready for input"

```
project
│   README.md
│   main.py
│   startup.mp3    
│
└───sounds
│   │   a_test.mp3
```

Pressing "a" will then play a_test.mp3.

It is highly recommended only to use sounds up to 10 seconds!

## Getting started
### Windows
Run the command to install python and pip through chocolatey, if not already installed:
```sh
choco install python
choco install pip3
```

Then use pip to install pygame:
```sh
pip3 install pygame
```

Run the application:
```sh
python .\main.py
```

## Deployment
To get started in your office you will need to run the script and sounds on a raspberry pi and connect a lightweight speaker.
Create a script that auto starts the main file on boot of the raspberry pi.
More to follow...

## Sound ideas
Due to koda the sound folder is not very packed. But some ideas to create a nice board could be:
 - h for hallelujah: https://www.youtube.com/watch?v=nsBByTiKfyY, when the problem you have been trying to solve for 2 days is suddenly gone :-)
 - b for ba dum tss: https://www.youtube.com/watch?v=6zXDo4dL7SU, when someone is telling a "perfect bad" joke.

 How you get the youtube sounds is completely up to you. You can use other sources as well. Pygame should include most audio formats.
