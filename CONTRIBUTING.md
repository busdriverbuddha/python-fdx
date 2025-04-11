# Contributing to python-fdx

Thank you for considering contributing to python-fdx! This document provides guidelines and instructions to help you get started.

## Code of Conduct

Please be respectful and considerate of others when contributing to this project.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue on GitHub with the following information:

- A clear, descriptive title
- Steps to reproduce the bug
- Expected behavior
- Actual behavior
- Any relevant logs or error messages
- Your environment (Python version, OS, etc.)

### Suggesting Enhancements

If you have an idea for an enhancement, please create an issue on GitHub with:

- A clear, descriptive title
- A detailed description of the proposed enhancement
- Any relevant examples or use cases

### Pull Requests

1. Fork the repository
2. Create a new branch for your feature or bugfix: `git checkout -b feature-name`
3. Make your changes
4. Run tests and ensure your code passes all checks
5. Commit your changes with a descriptive commit message
6. Push to your fork: `git push origin feature-name`
7. Submit a pull request

## Development Setup

### Prerequisites

- Python 3.10 or higher

### Installation for Development

1. Clone the repository:
   ```bash
   git clone https://github.com/busdriverbuddha/python-fdx.git
   cd python-fdx
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the package in development mode:
   ```bash
   pip install -e .
   ```

## Coding Standards

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write docstrings for all public functions, classes, and methods
- Run `flake8` to check your code before submitting

## Testing

- Add tests for new features
- Ensure all tests pass before submitting a pull request
- Tests should be placed in the `tests` directory

## Documentation

- Update documentation for any new features or changes to existing features
- Example usage should be included for new features

Thank you for your contributions! 