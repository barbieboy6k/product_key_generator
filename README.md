# product_key_generator
A Python Tkinter application that securely generates a formatted product key from user-provided email and password inputs.

```markdown
# Product Key Generator
A Python script that generates a secure product key using Tkinter for the user interface. The key is based on the email and password provided by the user and is formatted with hyphens for readability.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/product-key-generator.git
    ```

2. Navigate to the project directory:
    ```sh
    cd product-key-generator
    ```

## Usage

Run the script:
```sh
python product_key_generator.py
```

## Example
The application will display a window with two input fields:

Email: Enter your email address.
Password: Enter your password.
Click the "Generate Key" button to generate the product key.

The generated product key will be displayed below the button.

Click on the displayed product key to copy it to your clipboard.

## Code Explanation
generate_product_key(email, password)
Generates a secure product key by hashing the email and password, interleaving the hashes, and formatting the result.

on_generate()
Handles the "Generate Key" button click event, validates input, and displays the product key.

copy_to_clipboard(event)
Copies the generated product key to the clipboard when the result label is clicked.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the included LICENSE file for details.
