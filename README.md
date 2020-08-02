# BPlay


This project is aimed at giving input to the computer using webcam feed. It sends virtual keypresses of arrow keys based on user movement.

---------------

## Setup

Run the following in command line after you are in the project direcotry:

    pip install -r requirements.txt

You may need to run

    pip3 install -r requirements.txt

based on you pip settings.

---------------------

Usage:

To run the main script:

    main.py [-h] -f FILTER [-w WEBCAM]

You have the following optional arguments too:


    -h, --help                      Show this help message and exit

    -f FILTER, --filter FILTER      Range filter. RGB or HSV. Default is HSV

    -w WEBCAM, --webcam WEBCAM      Input number for Video Source. Default 0


Running only the following also works as command line arguments have defaults preset:

    python main.py

Please note you might have to use `python3 main.py` based on your configurations.

###  How to Use

1. To use it first attach a small paper or an object on your collar, it should be of a unique color and unlike all colors present in the frame.

2. Then run `python main.py` and press `t`.

   > You will now see binary mask on of your webcam feed and a slider window to adjust HSV values.
   > Adjust the HSV values using the slider such that only the object on your collar is of white color and rest of the frame is black as shown below.
   > Press `t` again. Now a red circle will be fixed on your collar.

3. Press `s` to set the position of the circle. This will be a reference of your movement.

4. Now, go to this [link](https://www.kiloo.com/subway-surfers/) to test it out. Make sure you are in the web browser window.

 > After the game stars try moving the centre which is the object to outside the circle in different directions. Based on your quadrant you will give virtual keypress of `up`, `down`, `left` or `right`.

 > Enjoy the game and have fun !!!

5. Press `q` to exit.

#### Additional Functionality

You can resize the circle using `+` or `-`.

You can reset the circle using `r`.

Press `s` to reposition the circle and then press `s` again to set it.

