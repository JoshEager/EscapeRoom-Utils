EscapeRoom-Utils is a set of software tools that are intended to be used for an escape room. 

In order to get started using EscapeRoom-Utils, you have to do the following

    1) Install Dependencies (gcc, make, git, python3)
         | sudo apt install build-essential git python3
          -> Will not work for distros using different Package managers

    2) Clone this repository
        git clone https://github.com/JoshEager/EscapeRoom-Utils.git 

    3) Move into this repository and build dependencies 
        cd EscapeRoom-Utils/rizzsec && make

    4) Generate an initial key for all your escape room encryption
        cd .. && python3 rizzsec/src/rizzsec-keygen.py -o ./key.key

    5) Now you're good to go. All utilities should work.
        - To run a utility (the name of each one and its functionality is listed below), simply move 
          into this git repository and run "python3 <utility>.py"

EscapeRoom-Utils contains the these utilities: 
    - escape_room_encryptor
        -> Used to generate a secret message being used in the escape room 
            ~ ex: You want to encrypt the key to a door
    - escape_room_decryptor
        -> Used by the escapees to decrypt your secret message
            ~ ex: The escapees find a message and need to decrypt it
    - decryptor_loop
        -> Runs escape_room_decryptor continuosly, should be used in an actual escape room environment
            ~ ex: You run this file so that the Escapees get as many attempts as they need
