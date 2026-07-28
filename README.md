# Password Generator

A silly little Python that generates  random passwords based on configurable settings.

## Features

- Reads password parameters from `config.json`
- Supports configurable length, uppercase letters, digits, and special characters
- Generates multiple passwords and writes them to `password.txt`
- Uses Python's `secrets` module for cryptographically secure randomness

## Files

- `pwd_gen.py` - main script that loads configuration, generates passwords, and writes the output file
- `config.json` - configuration file for password rules and generation count
- `password.txt` - generated output file created by the script

## Usage

Run the script from the project folder:

```bash
python pwd_gen.py
```

The script will read `config.json`, create the requested number of passwords, and save them to `password.txt`.

## Configuration

The `config.json` file supports:

- `password_length` (integer): number of characters per password
- `generate_count` (integer): number of passwords to generate
- `use_uppercase` (boolean): include uppercase letters
- `use_digits` (boolean): include digits
- `use_special_chars` (boolean): include special characters
- `special_chars` (string): set of special characters to use when enabled

Example:

```json
{
  "password_length": 14,
  "use_uppercase": true,
  "use_digits": true,
  "use_special_chars": true,
  "special_chars": "!@#$%^&*()_+-=[]{}|;:,.<>?",
  "generate_count": 5
}
```

## Notes

- If no character type is enabled, lowercase letters are used by default.
- The script validates the configuration and raises errors for invalid values.

🤠
## To do
- Add interface
- Add encryption to the password file
- Optionally: add final boss with epic soundtrack

Thank you for reading this has been a stupid little project.