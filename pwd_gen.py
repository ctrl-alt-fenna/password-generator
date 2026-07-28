import json
import os
import secrets
import string
from pathlib import Path
def load_config(filename="config.json"):
    """
    Load the password configuration. Returns the needed values so they can be used in the generator.
    """
    if not filename.endswith(".json"):
        raise TypeError("File must be JSON format")

    config_path = Path(filename)
    if not config_path.is_file():
        raise FileNotFoundError(f"Config file '{filename}' was not found.")    
    with open(config_path, "r") as config_file:
        data = json.load(config_file)
        
        try:
            password_length = data["password_length"]
            generate_count = data["generate_count"]
        except(KeyError, TypeError, ValueError) as exc:
            raise ValueError("Config must contain valid password_length and generate_count values") from exc
        
        use_special_chars = bool(data.get("use_special_chars", False))
        use_digits = bool(data.get("use_digits", False))
        use_uppercase = bool(data.get("use_uppercase", False))
        special_chars = data.get("special_chars", "")
        
    if password_length <= 0:
        raise ValueError("password_length must be a positive integer")
    if generate_count <= 0:
        raise ValueError("generate_count must be a positive integer")
    if use_special_chars and not isinstance(special_chars, str):
        raise ValueError("special_chars must be a string when special characters are enabled")

    return {
        "password_length": password_length,
        "generate_count": generate_count,
        "use_uppercase": use_uppercase,
        "use_digits": use_digits,
        "use_special_chars": use_special_chars,
        "special_chars": special_chars,
    }
    
def generate_password(config):
    """
    Generates one password that matches the selected parameters    
    """
    
    length = config["password_length"]
    valid_chartypes = []
    
    if config["use_uppercase"]:
        valid_chartypes.append(string.ascii_uppercase)
    if config["use_digits"]:
        valid_chartypes.append(string.digits)
    if config["use_special_chars"]:
        valid_chartypes.append(config["special_chars"])

    if not valid_chartypes:
        valid_chartypes.append(string.ascii_lowercase)
    
    if length < len(valid_chartypes):
        raise ValueError("Password length is too short for the selected character parameters")
    
    available_chars = "".join(valid_chartypes)
    password_chars = [secrets.choice(category) for category in valid_chartypes]
    
    for x in range(length - len(valid_chartypes)):
        password_chars.append(secrets.choice(available_chars))
    
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)

def create_passwords(config_filename="config.json", output_filename="password.txt"):
    """
    Create the passwords and write them to a file.
    """
    config = load_config(config_filename)
    
    with Path(output_filename).open("w", encoding="utf-8") as file:
        for i in range(config["generate_count"]):
            file.write(generate_password(config)+"\n")

    return output_filename

def pause_for_exit():
    """
    Pause before closing so the user gets notified of the status.
    """
    if os.name == "nt":
        import msvcrt
        print("Passwords succesfully generated. Press any key to exit...")
        msvcrt.getch()
    else:
        input("Passwords succesfully generated. Press Enter to exit...")
        
def main():
    try:
        output_file = create_passwords()
    except(FileNotFoundError, TypeError, ValueError, json.JSONDecodeError) as exc:
        # print(f"Error: {exc}" + exc.msg)
        return 1
    print(f"Passwords were written to {output_file}")
    pause_for_exit()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())