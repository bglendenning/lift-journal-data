# Lift Journal Data

## Installing as a package

Add `git+https://github.com/bglendenning/lift-journal-data.git` to your project's requirements.

## Installing the requirements

```bash
user@host:./lift-journal-data$ python -m venv <venv_dir>
user@host:./lift-journal-data$ source <venv_dir>/bin/activate
user@host:./lift-journal-data$ pip install -r requirements.txt
```

## Configuring the environment

```bash
# Granular database configuration
user@host:./lift-journal-data$ export LIFT_JOURNAL_DATA_DB_ENGINE=<database engine>
user@host:./lift-journal-data$ export LIFT_JOURNAL_DATA_DB_USERNAME=<database username>
user@host:./lift-journal-data$ export LIFT_JOURNAL_DATA_DB_PASSWORD=<database password>
user@host:./lift-journal-data$ export LIFT_JOUNRAL_DATA_DB_SERVER=<database server>
user@host:./lift-journal-data$ export LIFT_JOURNAL_DATA_DB_NAME=<database name>

# URL database configuration
user@host:./lift-journal-data$ export LIFT_JOURNAL_DATA_DB_URL=<database url>
```

## Managing the database

`lift_journal_data.db.manage` provides database management functions. The script provides three command line arguments:

* `--create-tables` creates all non-existent tables defined in the ORM models
* `--drop-tables` drops all existent tables defined in the ORM models
* `--load-lifts` populates the `lift` table with fixture data

Ordering of arguments has no impact on order of operations:

```bash
user@host:./lift-journal-data$ python -m lift_journal_data.db.manage --create-tables --drop-tables --load-lifts
```

The preceding command will result in the following order of operations:

1. drop all tables
2. create all tables
3. load lifts fixture

### Using the management script from within the repository

_Lift Journal Data_'s database management script must be executed as a module.

```bash
user@host:./lift-journal-data$ python -m lift_journal_data.db.manage <arguments>
```

### Using the management script in a virtual environment as an installed package

```bash
user@host:./lift-journal-data$ ljd_manage <arguments>
```

## Testing

`lift-journal-data` has no database engine-specific dependencies, so an in-memory SQLite database is used for testing. Python's _unittest_ is used for running tests.

```bash
user@host:./lift-journal-data$ python -m unittest discover
```
