
## Coding conventions
- Class names use PascalCase (e.g., MyClass).
- variables and function names use snake_case (e.g., this_variable, compute_something).
- Follow PEP 8 with the exception:
  - allow line lenghts up to 120 characters
- Use type annotations for public functions and methods.
- Keep functions single-responsibility.
- Prefer explicit is better than implicit; avoid clever one-liners that reduce readability.
- Use dataclasses / NamedTuple for simple structured data.
- Use f-strings for formatting.



## Testing
- Write unit tests in tests/ using pytest.
- Use parametrized tests for multiple input cases.
- Mock external dependencies (network, filesystem) with monkeypatch or pytest-mock.
- Coverage: focus on core logic; tests for edge cases and error handling.

## Docstrings & comments
- Add concise triple-quoted docstrings for modules, classes, and public functions using Google style docstrings.
- For internal helper code prefer short inline comments explaining why (not what).
