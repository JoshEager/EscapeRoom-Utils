# EscapeRoom-Utils

EscapeRoom-Utils is a collection of software tools designed for use in an escape room. 

##  Installation

### Install Dependencies
In order to use EscapeRoom-Utils, you need to have gcc, make, git, and python3. 

```sh
sudo apt install build-essential git python3
```

> **Note:** this command only works for debian based distros

### Clone the repository
```sh
git clone https://github.com/JoshEager/EscapeRoom-Utils.git
```

### Run the setup script
This will build the encryptor and generate a key for use in your escape room. 

```sh
cd EscapeRoom-Utils && ./setup.sh
```

## Running Utilities
To use any utility, simply navigate to the repository you just cloned and run
```sh
python3 <utility>.py
```
where utility is one of the Available Utilites

## Available Utilities

### `escape_room_encryptor`
🔒 Encrypts a secret message for the escape room.  
**Example Use Case:** Encrypting the key to a door.

### `escape_room_decryptor`
🔑 Decrypts an encrypted message.  
**Example Use Case:** Escapees use this to reveal hidden messages.

### `decryptor_loop`
🔄 Runs `escape_room_decryptor` continuously for repeated attempts.  
**Example Use Case:** In an actual escape room, escapees can keep trying until they succeed.
