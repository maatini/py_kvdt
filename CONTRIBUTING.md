# Contributing to py_kvdt

Thank you for considering contributing to `py_kvdt`! This project aims to be a robust, modern, and readable library for KVDT data processing.

## Getting Started

1.  **Environment**: Use [Devbox](https://www.jetpack.io/devbox/) for a consistent development environment.
    ```bash
    devbox shell
    ```
2.  **Installation**: Install the package in editable mode with development dependencies.
    ```bash
    uv pip install -e .
    ```

## Project Structure

- `src/pykvdt/`: Core library code.
    - `model.py`: Dataclasses for Tokens, Sentences, and Definitions.
    - `parser.py`: The recursive descent parser.
    - `structures.py`: **The most important file for adding new sentence types.**
    - `definitions.py`: List of all KVDT field definitions.
    - `generator.py`: Test data generation logic.
- `tests/`: Comprehensive test suite.
- `scripts/`: Production and utility scripts.

## How to Add a New Sentence Type

Sentence types are defined in `src/pykvdt/structures.py`. To add a new one:

1.  Find the `SENTENCE_TYPES` dictionary.
2.  Add a new `SentenceDefinition` entry.
3.  Use `F(field_id, mandatory, count, rules)` for fields and `G(items, mandatory, count, rules)` for nested groups.
4.  Example:
    ```python
    "9999": SentenceDefinition("9999", "My New Sentence", [
        F("8000", True, 1),
        F("0102", False, 1),
    ])
    ```

## Development Workflow

1.  **Write Tests**: For any new feature or bug fix, add a test in `tests/`.
2.  **Linting**: We use `ruff` and `black`.
    ```bash
    devbox run lint
    devbox run format
    ```
3.  **Run Tests**: Ensure all tests pass.
    ```bash
    devbox run test
    ```
4.  **Coverage**: Maintain >95% coverage.
    ```bash
    python3 -m coverage run -m unittest discover tests
    python3 -m coverage report
    ```

## Documentation

We use `pdoc` for automated API documentation. If you add new classes or methods, please provide clear docstrings and type hints.
```bash
devbox run docs
```

## Pull Requests

1.  Create a feature branch.
2.  Ensure CI passes (or run local tests/linting).
3.  Submit the PR with a clear description of the changes.
