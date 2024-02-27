**# Java Lexical Analyzer using PLY**

This repository provides a comprehensive and well-structured Python-based lexical analyzer (lexer) for Java code, built utilizing the PLY library. This lexer effectively tokenizes Java code, laying the groundwork for further parsing and analysis.

**Key Features:**

- **Extensive Tokenization:** Identifies a diverse range of Java tokens, including:
    - Keywords (e.g., `public`, `class`, `while`)
    - Identifiers (e.g., `main`, `message`)
    - Numbers (e.g., `10`, `42.3`)
    - Operators (e.g., `+`, `-`, `*`, `/`, `=`, `<`, `>`, `!`)
    - Punctuation (e.g., `(`, `)`, `{`, `}`, `;`, `,`)
    - Strings (e.g., `"Hello, World!"`)
    - Comments (e.g., `// This is a single-line comment`)
    - Additional special characters (e.g., `&`, `@`, `.`)
- **Robust Error Handling:** Gracefully handles invalid characters, providing informative error messages for debugging.
- **Customizable and Extendable:** Easily modify the lexer to recognize additional tokens or patterns to suit specific needs.

**Usage:**

1. **Install the PLY library:**

   ```bash
   pip install ply
   ```

2. **Run the lexer:**

   ```bash
   python lexer.py
   ```

3. **Provide Java code:** The lexer will prompt you to enter the Java code you want to analyze.
4. **Analyze and view output:** The lexer will analyze the code, identifying and displaying each token and its corresponding type.

**Code Structure:**

- **`tokens` List:** Defines the recognized token types (e.g., `IDENTIFIER`, `NUMBER`, `OPERATOR`).
- **Token-Defining Functions:** Implement regular expressions to match specific token patterns (e.g., `t_IDENTIFIER`, `t_NUMBER`, `t_KEYWORD`).
- **Error Handling:** The `t_error` function provides informative messages for invalid characters.
- **Lexer Creation:** The `lexer = lex.lex()` statement constructs the lexer instance.
- **Lexical Analysis:** Demonstrates the lexer's usage with sample Java code within a `while` loop.

**Potential Applications:**

- **Compiler Front-End:** Serves as the initial stage of Java compilers, responsible for splitting code into tokens for parsing.
- **Code Analysis Tools:** Enables analyzing code structure, identifying patterns, and detecting potential errors.
- **Educational Purposes:** Provides a practical example of lexical analysis concepts and techniques.

**Customization:**

- **Adding Tokens:** Expand the `tokens` list and define corresponding regular expressions to recognize additional token types.
- **Modifying Rules:** Adjust existing regular expressions to refine token recognition and handle specific patterns.
- **Extending Functionality:** Integrate with parser generators like PLY's `yacc` module for complete Java parsing.


**Additional Information:**

- PLY Library: [https://github.com/topics/ply?l=python](https://github.com/topics/ply?l=python)

