# Lift Journal Data

## Intent

`lift-journal-data` serves as an authority for Lift Journal database structure and interactions. This repository should provide the following:

1. Database table population
2. Database migrations
3. Python API to encapsulate and abstract SQLAlchemy ORM CRUD operations for dependent projects
4. Comprehensive tests
5. Pydantic models and data validation

### Why encapsulate and abstract SQLAlchemy ORM CRUD operations?

Dependent projects can have more focused, cleaner, and easier to read code with less context shifts and limited potential for technical debt.

### Why include Pydantic models?

Pydantic models are used for serialization, validation, etc. in many modern Python API projects. If the database structure changes, the Pydantic schema definitions should also change. By providing Pydantic models, `lift-journal-data` maintains its authority of the data and decouples dependent projects from data concerns.

## Installation

`lift-journal-data` can be installed using `pip`. With an active Python virtual environment, install `lift-journal-data` using `pip install git+https://github.com/bglendenning/lift-journal-data.git` or add `git+https://github.com/bglendenning/lift-journal-data.git` to your project's requirements and `pip install -r <requirements_file>`.

## Environment Variables

`lift-journal-data` depends on some environment variables for database connection configuration. Environment variables can be provided granularly:

```bash
user@host:./lift-journal-data$ export LIFT_JOURNAL_DATA_DB_ENGINE=<database engine>
user@host:./lift-journal-data$ export LIFT_JOURNAL_DATA_DB_USERNAME=<database username>
user@host:./lift-journal-data$ export LIFT_JOURNAL_DATA_DB_PASSWORD=<database password>
user@host:./lift-journal-data$ export LIFT_JOUNRAL_DATA_DB_SERVER=<database server>
user@host:./lift-journal-data$ export LIFT_JOURNAL_DATA_DB_NAME=<database name>
```

You can also specify a full database URL. This value supersedes the granular environment variables.

```bash
user@host:./lift-journal-data$ export LIFT_JOURNAL_DATA_DB_URL=<database url>
```

## Testing

Because `lift-journal-data` has no database engine-specific dependencies, an in-memory SQLite database is used for testing. This simplifies test composition and configuration.

Python's `unittest` is used for running tests:

```bash
user@host:./lift-journal-data$ python -m unittest discover
```
