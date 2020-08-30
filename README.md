# Dicum

Dicum is a small game for tease and denial lovers that like to get locked up. 

![Game Preview](https://github.com/joka-beep/dicum/blob/master/preview/preview-alpha.png)

## How does it work?

You get a set of buttons that allow you to activate the next action, like roulette, you don't know what will be your next draw. Possible actions are 

* Draw a closed lock
* Draw an open lock
* Draw a teaser-image
* Draw a website (possibly a teaser)
* Draw a time that is added to your next lockup time

If you draw more than the limit of closed locks (currently 2), the game will stop and is blocked for the lockup time. The lockup time is at minimum one hour and might be increased when you draw a time increase.

If you draw open locks, you get released and can do whatever you want until you start to play the game again.

## Installation

Option 1 (easy):
* Download the binary and run it. (Might only work in Linux, I have only tested locally.)

Option 2 (for development): 
* Install python3 `sudo apt install python3`
* Clone the repository `git clone ... && cd dicum`
* Create a virtual environment for python `python3 -m venv venv`
* Source the environment `source venv/bin/activate`
* Install requirements from requirements.txt `pip install ...`
* Run the game `python3 DicumUI/DicumUI.py`

## Configuration

When you run the program for the first time, it will create the directory `~/.config/dicum` in which the program stores all resources.
Create a file `game.csv` and add for example the following commands: 
```csv
img,pic1.png,0
img,pic2.png,0
img,pic3.png,0
num,2,0
num,3,0
num,5,0
num,5,0
num,12,0
lock,unlock,0
lock,unlock,0
lock,lock,0
lock,lock,0
```

img : image name
num : number of hours added to your lockup time
lock: lock/unlock is a closed, open lock, respectively
the last number (currently 0 everywhere) shall be used in the future, but is not used for now.

The images (pic1.png, pic2.png, pic3.png) must exist in `~/.config/dicum/resources/images/`. I have not checked any image copyrights, so you'll have to add your own images.

If you want to run the game from executable, run the following commands, while you have sourced your venv:
```bash
$ pip install pyinstaller
$ cd Dicum/
$ pyinstaller Dicum.spec
```
