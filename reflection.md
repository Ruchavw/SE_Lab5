# Reflection – Static Code Analysis Lab

## 1. Which issues were the easiest to fix, and which were the hardest? Why?

- **Easiest:**  
  The easiest issues to fix were stylistic ones, such as adding missing docstrings, renaming functions to `snake_case`, and removing unused imports. These were straightforward because they didn’t affect program logic—only formatting and documentation.

- **Hardest:**  
  The most challenging fixes were related to unsafe or incorrect logic, such as replacing `eval()` with safe alternatives and handling the mutable default argument. These required understanding how the code worked and ensuring that the fix didn’t break functionality.

---

## 2. Did the static analysis tools report any false positives? If so, describe one example.

Yes.  
`pylint` flagged the use of the `global` statement in `load_data()` as a potential issue.  
Although using globals is generally discouraged, in this small, single-file script it was necessary to maintain state across functions. Therefore, this warning was considered a false positive in this specific context.

---

## 3. How would you integrate static analysis tools into your actual software development workflow?

- **Local development:**  
  Run `pylint`, `flake8`, and `bandit` automatically through pre-commit hooks to catch issues before committing.  

- **Continuous Integration (CI):**  
  Integrate these tools in a CI pipeline (e.g., GitHub Actions) so that every pull request triggers static analysis checks. The build should fail if critical issues or security vulnerabilities are detected.

This ensures consistent code quality, security, and style enforcement across all contributors.

---

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

- Code became **more readable and maintainable** due to consistent naming conventions and added docstrings.  
- Using `with open(..., encoding='utf-8')` improved **resource safety and portability**.  
- Removing `eval()` eliminated a **security vulnerability**.  
- Type validation and input checks made the functions **more robust against runtime errors**.  
- Overall, the program is now safer, cleaner, and better aligned with Python best practices.

---

