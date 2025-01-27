# Dependencies
sudo apt install build-essential git python3

# Clone the repo
git clone https://github.com/JoshEager/EscapeRoom-Utils.git

# Build Dependencies
cd EscapeRoom-Utils/rizzsec
make

# Make a key
cd ..
python3 ./rizzsec/src/rizzsec-keygen.py

# Remove the install script
rm ./install.sh
