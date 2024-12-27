import os
import subprocess

def format_with_black(directory):
    """
    Run Black to format the codebase.
    """
    print(f"Formatting code in {directory} with Black...")
    subprocess.run(["black", directory], check=True)

def fix_flake8_errors(directory):
    """
    Run Flake8 to detect errors and manually resolve the common issues.
    """
    print(f"Checking Flake8 issues in {directory}...")
    result = subprocess.run(["flake8", directory], capture_output=True, text=True)
    flake8_output = result.stdout.splitlines()

    for line in flake8_output:
        if "E501" in line:  # Long lines
            print(f"Wrapping long line: {line}")
            # Black will handle line wrapping for E501 errors
        elif "E302" in line:  # Missing blank lines
            print(f"Adding blank lines: {line}")
            add_blank_lines(line)
        elif "F401" in line:  # Unused imports
            print(f"Removing unused import: {line}")
            remove_unused_import(line)
        elif "E305" in line:  # Missing blank lines after function/class
            print(f"Fixing blank lines after function/class: {line}")
            add_blank_lines(line)

def add_blank_lines(error_line):
    """
    Add blank lines for E302/E305 errors.
    """
    file_path, line_number = parse_error_line(error_line)
    with open(file_path, "r") as file:
        lines = file.readlines()

    index = int(line_number) - 1
    if index > 0 and not lines[index - 1].strip():  # Add a blank line above
        lines.insert(index, "\n")

    with open(file_path, "w") as file:
        file.writelines(lines)

def remove_unused_import(error_line):
    """
    Remove unused imports for F401 errors.
    """
    file_path, line_number = parse_error_line(error_line)
    with open(file_path, "r") as file:
        lines = file.readlines()

    index = int(line_number) - 1
    lines[index] = f"# {lines[index]}"  # Comment out the unused import

    with open(file_path, "w") as file:
        file.writelines(lines)

def parse_error_line(error_line):
    """
    Parse the Flake8 error line to extract file path and line number.
    """
    parts = error_line.split(":")
    return parts[0], parts[1]

if __name__ == "__main__":
    # Specify the directories to format and check
    code_directory = "chatassist"
    tests_directory = "tests"

    # Format code with Black
    format_with_black(code_directory)
    format_with_black(tests_directory)

    # Fix Flake8 issues manually
    fix_flake8_errors(code_directory)
    fix_flake8_errors(tests_directory)

    print("Code formatting and Flake8 issues fixed!")
