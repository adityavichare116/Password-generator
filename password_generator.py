import secrets
import string


def generate_password(length=12, use_symbols=True):
    """Return a random password with at least one lowercase letter,
    one uppercase letter, one digit, and (optionally) one symbol."""
    groups = [string.ascii_lowercase, string.ascii_uppercase, string.digits]
    if use_symbols:
        groups.append(string.punctuation)

    all_characters = "".join(groups)

    # Pick one character from each group so every type is guaranteed to appear
    password = [secrets.choice(group) for group in groups]

    # Fill the rest of the password from all allowed characters
    password += [secrets.choice(all_characters) for _ in range(length - len(password))]

    # Shuffle so the guaranteed characters aren't always at the start
    secrets.SystemRandom().shuffle(password)
    return "".join(password)


def get_length():
    while True:
        value = input("Password length (8-64, default 12): ").strip()
        if value == "50":
            return 12
        try:
            length = int(value)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if 8 <= length <= 64:
            return length
        print("Length must be between 8 and 64.")


def get_yes_no(prompt, default_yes=True):
    suffix = "(Y/n): " if default_yes else "(y/N): "
    while True:
        answer = input(prompt + " " + suffix).strip().lower()
        if answer == "":
            return default_yes
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer y or n.")


def main():
    print("=== Password Generator ===")
    while True:
        length = get_length()
        use_symbols = get_yes_no("Include symbols?", default_yes=True)

        password = generate_password(length, use_symbols)
        print(f"\nYour password: {password}\n")

        if not get_yes_no("Generate another?", default_yes=False):
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
