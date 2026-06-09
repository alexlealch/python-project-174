# Claude Project Guide - Python OOP Study (Modulo 2)

## Project Overview
This project is a study environment for a Python course focusing on advanced Python concepts and Object-Oriented Programming (OOP), specifically Modulo 2. The goal is to implement exercises and understand architectural patterns, moving from functional programming to robust OOP design.

## Course Map & Progress

### 1. Functional Programming (`M2 - funciones`)
Focuses on high-order functions, state management, and concise data processing.
- **Closures**: Implementing functions that capture local state.
- **Lambdas & Higher-Order Functions**: Use of anonymous functions and functions that take/return other functions.
- **Map, Filter, Reduce**: Standard functional tools for collection processing.
- **Comprehensions**: Efficient use of list and dictionary comprehensions.
- **Recursion**: Understanding recursive calls and iterative transformations.
- **Abstraction**: Initial steps towards isolating complexity.

### 2. Testing (`M2 - pruebas`)
- **Assertions**: Using `assert` for validation and correctness checks.

### 3. Abstraction (`M2 - abstraccion`)
Transitioning from primitive data structures to structured representations.
- **Cartesian & Polar Coordinates**: Implementing mathematical representations of points.
- **Interfaces**: Defining how different components interact.

### 4. Object-Oriented Programming (`M2 - POO`)
Implementing design patterns and Domain-Driven Design (DDD) concepts.
- **Design & Configuration**: 
    - Using `**kwargs` for flexible object configuration.
    - Managing default options via class-level `OPTIONS` dictionaries.
- **Entities & Value Objects**:
    - **Value Objects**: Implemented via the `Url` class, where equality (`__eq__`) is based on value, not memory identity.
    - **Primitive Obsession**: Combatting the use of raw strings/dicts for complex logic by creating dedicated classes.
    - **Encapsulation**: Protecting internal state using the `_prefix` convention.
    - **Standard Library Integration**: Leveraging `urllib.parse` to avoid manual string manipulation.
- **Fluent Interface**:
    - Implemented in `M2 - POO - 29.Fluent Interface.py`.
    - Use of method chaining by returning `self` to create readable, pipeline-like data transformations.
    - Applied to the `Collection` class to perform normalization, deduplication, grouping, and sorting.
- **Constructors & Builders**:
    - Distinction between the language constructor (`__init__`) and the Builder design pattern for complex object creation.
    - Application of Value Objects to resolve "Primitive Obsession" in range validations.
    - Implemented in `M2 - POO - 30.Constructores-Builders.py` (Hotel Booking system).
- **SOLID Principles**:
    - Introduction to SOLID architecture.
    - **SRP (Single Responsibility Principle)**: Deep dive into splitting "God Classes" into cohesive pieces (Validation, Persistence, and Coordination).

### 5. GitHub Actions & CI/CD
Understanding automated workflows for software integration and delivery.
- **Workflows**: Configuration files in `.github/workflows` that can run in parallel.
- **Events**: Triggers for workflows (push, pull request, cron, or webhooks).
- **Jobs & Runners**: Units of work executed on temporary servers (Linux, macOS, Windows).
- **Steps & Actions**: Sequential commands within a job; use of reusable community actions.
    - **Actions**: Use of `uses` instead of `run` to invoke catalog actions (internal or external).
    - **Versioning**: Version specification (e.g., `@v3`) to ensure stability.
    - **Parameters**: Configuration of actions using the `with` key.
- **Task Management**: Dependency handling (`needs`), conditional execution (`if`), and matrix strategies for multi-OS testing.
- **Environment**: Management of environment variables (`env`) at job and step levels.

## Coding Standards & Patterns

- **Encapsulation**: Use a single leading underscore (e.g., `_variable`) for internal attributes.
- **Anti-Pattern Avoidance**: Avoid "Primitive Obsession" by encapsulating logic into dedicated classes.
- **Standard Library First**: Prefer built-in Python modules over manual implementation.
- **DDD Concepts**:
    - **Value Objects**: Defined by attributes (e.g., `Url`).
    - **Entities**: Defined by a unique identity.

## Workflow Guidelines
- **Exercise Implementation**: Solutions must be placed strictly between `# BEGIN` and `# END` markers.
- **Teaching Mode**: Detailed, pedagogical explanations of *why* an approach was taken are preferred.

## Key Commands
- Run exercises: `python "filename.py"`
- List files: `ls -R`
