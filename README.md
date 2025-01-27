# EscapeRoom-Utils

EscapeRoom-Utils is a collection of software tools designed for use in an escape room.

## Installation

### One-Command Install (Debian-based Distros)
If you're using Debian or a Debian-based distribution, run:

```sh
curl -fsSL https://raw.githubusercontent.com/JoshEager/EscapeRoom-Utils/main/install.sh | bash
```

> **Note:** If this works, you can skip the manual installation steps below.

### Manual Installation

1. **Install Dependencies**  
   Ensure you have the necessary dependencies installed:

   ```sh
   sudo apt install build-essential git python3
   ```

   > If you're using a non-Debian-based distribution, install `gcc`, `make`, `git`, and `python3` with your package manager.

2. **Clone the Repository**  
   Run the following command:

   ```sh
   git clone https://github.com/JoshEager/EscapeRoom-Utils.git
   ```

3. **Build Dependencies**  
   Navigate into the repository and build the required components:

   ```sh
   cd EscapeRoom-Utils/rizzsec && make
   ```

4. **Generate an Encryption Key**  
   Create an initial key for encryption in your escape room:

   ```sh
   cd .. && python3 rizzsec/src/rizzsec-keygen.py -o ./key.key
   ```
---

## Running Utilities  
To use any utility, simply navigate to the repository and run:

```sh
python3 <utility>.py
```
where utility is one of the Available Utilities


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

---

