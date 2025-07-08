# MMIS Ghana - Municipal Management Information System

This project is a Django-based Municipal Management Information System (MMIS) for District Assemblies in Ghana. It aims to digitize and streamline various departmental functions, enhancing efficiency and transparency.

## Project Overview

The MMIS is designed to replace manual processes with an integrated digital platform. Key modules include:

*   **Human Resources & Payroll Management:** Employee records, leave, attendance, payroll.
*   **Accounts & Financial Management:** Revenue collection, expenditure, budgeting, reporting.
*   **Town & Country Planning:** Building permits, land use applications.
*   **Births & Deaths Registry:** Registration of births and deaths.
*   **General Administration:** User management, document management (future), audit trails.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python (3.8 or newer recommended)
*   pip (Python package installer)
*   Git (for cloning the repository, if applicable)

### Installation

1.  **Clone the repository (if you have it in git):**
    ```bash
    git clone <repository-url>
    cd mmis-ghana # Or your project directory name
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    At the moment, the main dependency is Django.
    ```bash
    pip install Django~=5.2
    ```
    (If a `requirements.txt` file is provided in the future, use `pip install -r requirements.txt`)

4.  **Apply database migrations:**
    This will create the necessary database tables.
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser:**
    This account will allow you to access the Django admin interface.
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to set a username, email, and password.

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be accessible at `http://127.0.0.1:8000/`.
    *   Admin interface: `http://127.0.0.1:8000/admin/`
    *   HR Employee List (example): `http://127.0.0.1:8000/hr/employees/` (requires login)

## Current Structure

*   `mmis_project/`: Contains the main project settings and configurations.
*   `hr_payroll/`: App for Human Resources and Payroll.
*   `finance/`: App for Accounts and Financial Management.
*   `planning/`: App for Town & Country Planning.
*   `registry/`: App for Births & Deaths Registry.
*   `general_admin/`: App for cross-cutting features like user profiles, departments, audit logs.
*   `templates/`: Contains base HTML templates and project-wide templates like `home.html` and `dashboard.html`.
    *   Each app also has its own `templates/<app_name>/` directory for app-specific templates.

## Next Steps & Future Development

*   Full implementation of CRUD (Create, Read, Update, Delete) operations for all core models.
*   Development of user-facing forms and views beyond the Django admin.
*   Implementation of business logic for each module (e.g., payroll calculation, permit approval workflows).
*   Refinement of UI/UX based on the provided Stitch mockups.
*   Role-based access control and permissions for different user types.
*   Reporting and analytics features.
*   Document Management System.
*   Citizen Engagement Portal (future phase).

This `README.md` will be updated as the project progresses.
