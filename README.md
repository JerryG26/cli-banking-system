# CLI Banking System

A command-line banking application built with **Python** to practice Object-Oriented Programming (OOP), software engineering principles, and backend development fundamentals.

This project simulates basic banking operations, including account management, deposits, withdrawals, transfers, and transaction history.

## Project Status

**In Development — Phase 1: User Registration and Authentication**

This project is being developed incrementally, with each phase focusing on improving code quality, business logic, and software architecture.

## Objectives

- Apply Python Object-Oriented Programming principles.
- Practice encapsulation, inheritance, abstraction, and polymorphism.
- Implement proper input validation and exception handling.
- Follow separation of concerns and clean-code principles.
- Organize code using models, services, repositories, and UI layers.
- Practice Git and GitHub version control.
- Build a foundation for future SQL and FastAPI projects.

## Planned Features

### User Authentication
- Register a new user account.
- Log in using registered credentials.
- Validate user information.
- Prevent duplicate registrations.
- Manage authenticated user sessions.

### Bank Account Management
- Create and manage bank accounts.
- View account information.
- Check available balances.
- Support unique account identifiers.

### Banking Transactions
- Deposit money into an account.
- Withdraw available funds.
- Transfer funds between accounts.
- Prevent transactions with invalid amounts.
- Handle insufficient funds.

### Transaction History
- Record completed transactions.
- View transaction history.
- Display transaction details.
- Track deposits, withdrawals, and transfers.

### Administration
- Manage registered accounts.
- View account information.
- Apply appropriate access restrictions.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Git | Version control |
| GitHub | Remote repository hosting |
| VS Code | Development environment |
| WSL Ubuntu | Linux development environment |

The initial application will use **in-memory data storage** without a database or external framework.

## Planned Project Structure

The following directory structure is proposed and may change during development.

```text
cli-banking-system/
├── main.py
├── models/
│   ├── user.py
│   ├── bank_account.py
│   └── transaction.py
├── services/
│   ├── auth_service.py
│   ├── account_service.py
│   └── transaction_service.py
├── repositories/
│   ├── user_repository.py
│   └── account_repository.py
├── ui/
├── tests/
├── .gitignore
└── README.md
```

## Architecture

The application will follow a layered architecture.

- **UI Layer:** Handles command-line menus, user input, and output.
- **Service Layer:** Processes banking operations and enforces business rules.
- **Repository Layer:** Manages data storage and retrieval.
- **Model Layer:** Defines application entities and their behavior.

The goal is to keep components modular, maintainable, and testable.

## Installation and Setup

### Prerequisites

- Python 3
- Git
- A terminal or code editor

### Clone the Repository

Using SSH:

```bash
git clone git@github.com:JerryG26/cli-banking-system.git
cd cli-banking-system
```

### Run the Application

Once the application entry point has been implemented:

```bash
python3 main.py
```

**Note:** The application is still under development and may not be executable yet.

## Development Roadmap

- [ ] Phase 1 — User Registration and Authentication
- [ ] Phase 2 — Bank Account Management
- [ ] Phase 3 — Deposits, Withdrawals, and Transfers
- [ ] Phase 4 — Transaction History
- [ ] Phase 5 — Administration
- [ ] Phase 6 — Input Validation and Error Handling
- [ ] Phase 7 — Architecture Refactoring and Testing

### Future Improvements

- SQL database integration
- Persistent account and transaction storage
- Secure password hashing
- Unit and integration testing
- REST API development with FastAPI

## Development Principles

This project emphasizes:

1. **Correctness:** Banking operations must follow consistent business rules.
2. **Encapsulation:** Internal object state should be properly protected.
3. **Separation of Concerns:** Each layer should have clearly defined responsibilities.
4. **Maintainability:** Code should remain readable and easy to modify.
5. **Testability:** Business logic should be independently testable.

## Disclaimer

This application is intended for **educational purposes only**.

It does not process real financial transactions and should not be used as a production banking system.

## Author

**JerryG26**

GitHub: https://github.com/JerryG26

---

*Built as a hands-on Python OOP and backend development learning project.*