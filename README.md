 # Soundboard

A good team artifact to have present in a room of developers. Use with your own sounds!

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

## Sound ideas
Due to koda the sound folder is not very packed. But some ideas to create a nice board could be:
 - h for hallelujah: https://www.youtube.com/watch?v=nsBByTiKfyY, when the problem you have been trying to solve for 2 days is suddenly gone :-)
 - b for ba dum tss: https://www.youtube.com/watch?v=6zXDo4dL7SU, when someone is telling a "perfect bad" joke.

 How you get the youtube sounds is completely up to you. You can use other sources as well. Pygame should include most audio formats.

 ## Setup a Raspberry Pi to run the script

 Before starting, run the commands to setup the python environment:
 ```sh
$ pip install readchar

```
 This guide is tested and verified on a Raspberry Pi 3 with Raspberry Pi OS Released on 09-22-2022 (32 bit) 
 https://www.raspberrypi-spy.co.uk/2014/05/how-to-mount-a-usb-flash-disk-on-the-raspberry-pi/

List the usb drives mounted
 ```sh
$  ls -l /dev/disk/by-uuid/

```
Be  aware that the UUID found here will need to be put in the basepath of the main.py script.

Create a USB drive mount path
 ```sh
$ sudo mkdir /media/usb

```

Make sure the user has access to the folder 
 ```sh
$ sudo chown -R pi:pi /media/usb

```

To mount automaticallt 
 ```sh
$ sudo nano /etc/fstab

```

In the bottom of the file, add:
UUID={UUID OF DRIVE} /media/usb vfat defaults 0 2

 And the to run the main.py on boot, follow the steps in:  https://raspberrypi-guide.github.io/programming/run-script-on-boot

 ```sh
$  sudo nano /home/pi/.bashrc

```

Add the lines:

 ```sh
$ echo Running awesome script
$ sudo python /home/usb/main.py
```

