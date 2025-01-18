# Password Generator

A simple Python-based password generator that creates secure passwords with customizable length, inclusion of numbers, and special characters. This project leverages the `random` and `string` modules to ensure randomness and variety in the generated passwords.

## Features

- Generate passwords with a minimum specified length.
- Optionally include numbers and/or special characters.
- Ensures generated passwords meet the specified criteria.

## Requirements

- Python 3.6 or higher.

## Installation

Clone the repository or download the script directly.

```bash
git clone <repository_url>
```

Navigate to the project directory:

```bash
cd password-generator
```

## Usage

Run the script using Python:

```bash
python password_generator.py
```

### Input Prompts:

1. **Enter the length of the password:** Specify the minimum length of the password.
2. **Do you want numbers in the password? (y/n):** Choose whether to include numeric characters.
3. **Do you want special characters in the password? (y/n):** Choose whether to include special characters.

### Example

```text
Enter the length of the password: 12
Do you want numbers in the password? (y/n): y
Do you want special characters in the password? (y/n): n
The generated password is : aBcDeFgHiJ12
```

## Code Structure

### `generate_password(min_length, numbers=True, special_characters=True)`

- **Arguments:**
  - `min_length` *(int)*: Minimum length of the password.
  - `numbers` *(bool)*: Whether to include numbers.
  - `special_characters` *(bool)*: Whether to include special characters.
- **Returns:**
  - *(str)*: A randomly generated password meeting the specified criteria.
- **Logic:**
  - Constructs a character pool based on user preferences.
  - Ensures the generated password meets the minimum length and includes the required character types.

### `main()`

Handles user interaction:
- Prompts the user for password preferences.
- Calls `generate_password` with user inputs.
- Displays the generated password.

## Customization

You can modify the script to include additional character sets or change the logic for generating passwords as per your requirements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for improvements or bug fixes.

## Author

Med Amine
