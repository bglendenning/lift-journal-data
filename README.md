# Lift Journal Data

## Background

The _Lift Journal_ project as a whole serves two purposes:

1. A demonstration of my approach to development
2. An educational venture to work with technologies I have little to no experience with

### History

In 2019, I left my nearly-decade-long position as a building information modeler, parametric programmer, and office IT services provider at a structural engineering firm and spent 6 months working with Python and Django while applying for remote web developer positions. I had some general entry-level experience, having performed various contract services for UI/UX design, front end development, and some minor back end development.

Having gone through the interview and technical assessment process for multiple companies, I found that my background and experience were limiting my opportunities. Most companies weren't looking for a hacker with hustle, even in 2019 there was a strong emphasis on academic knowledge of algorithms as a basis for problem-solving in assessments for web developer positions.

I received a response from Swappa, and was asked to interview, but no agenda was specified. After my experiences with other companies, I felt that, given the opportunity to express my strengths, I would give a much better impression of what value I can provide. I decided to create a web service using unfamiliar technologies to solve a legitimate problem. I had 7 days to do this, and felt that if I could get it done it would highlight my ability to efficiently and effectively learn, understand, and implement new information.

I created the original _Lift Journal_ project in a monolithic repository using Python, [Flask](https://flask.palletsprojects.com/en/3.0.x/), [Blueprint JS](https://blueprintjs.com/), and [D3](https://d3js.org/). The service handled user registration, issued Javascript web tokens, allowed users to log their weight lifting sessions, and allowed users to record and view their progress over time by rendering timeseries plots of weight lifting records. The work helped me to land my first full-time web developer position.

### Intent

`lift-journal-data` serves as an authority for Lift Journal database structure and interactions. The philosophy behind its creation is the same as the original _Lift Journal_: work with unfamiliar technologies to solve a real problem. It is one repository of three in an exercise in domain driven development. The intent of this repository is to provide the following:

1. Database table population
2. Database migrations
3. Python API to encapsulate and abstract SQLAlchemy ORM CRUD operations for dependent projects
4. Comprehensive tests
5. Pydantic models

#### Why encapsulate and abstract SQLAlchemy ORM CRUD operations?

The project data structure provides for a limited scope of interactions with the data. By abstracting the SQLAlchemy operations, dependent projects can have focused, clean, and easier to read code with less context shifts and limited potential for technical debt.

#### Why include Pydantic models?

Pydantic models are used for serialization, validation, etc. in many modern Python API projects. If the database structure changes, the Pydantic schema definitions should also change. By providing Pydantic models, `lift-journal-data` maintains its authority of the data and decouples dependent projects from data concerns.

## Installation

`lift-journal-data` can be installed using `pip`. With an active Python virtual environment, install `lift-journal-data` using `pip install git+https://github.com/bglendenning/lift-journal-data.git` or add `git+https://github.com/bglendenning/lift-journal-data.git` to your project's requirements and `pip install -r <requirements_file>`.

## Environment Variables

`lift-journal-data` depends on some environment variables for database connection configuration. Environment variables can be provided granularly:

```bash
export LIFT_JOURNAL_DATA_DB_ENGINE=<database engine>
export LIFT_JOURNAL_DATA_DB_USERNAME=<database username>
export LIFT_JOURNAL_DATA_DB_PASSWORD=<database password>
export LIFT_JOUNRAL_DATA_DB_SERVER=<database server>
export LIFT_JOURNAL_DATA_DB_NAME=<database name>
```

You can also specify a full database URL. This value supersedes the granular environment variables.

```bash
export LIFT_JOURNAL_DATA_DB_URL=<database url>
```

## Testing

Because `lift-journal-data` requires no database engine-specific dependencies, an in-memory SQLite database is used for testing. This simplifies test composition and configuration.  

## Acknowledgments

I would like to thank Nathan LeBert for introducing me to test driven development, domain driven development, and [FastAPI](https://fastapi.tiangolo.com/) during our shared time at [Acres](https://www.acres.com/). We didn't get to work with those things much, but his foresight and enthusiasm for understanding architectural concepts and keeping up with emerging technologies greatly influenced my thinking as a developer.

I would also like to thank Pavel Dorovskoy, Applied GeoSolutions (now defunct), and [Carbon Mapper](https://carbonmapper.org/) for inviting and encouraging me to accept contracts to perform a variety of full stack work. The experiences I earned from those ventures contributed to my progress as a developer by presenting challenging problems to solve that continuously filled gaps in my knowledge and allowed for my progression as a developer and problem-solver in general.

Finally, I would like to thank Ben Edwards and Michael Lipson at [Swappa](https://swappa.com/) for having the courage to gamble on hiring a very inexperienced developer. The lessons learned while trying to be productive in the demanding environment of a popular marketplace facilitator, and the wisdom and experience shared by my colleagues, helped to shape my conception of what is necessary to be a valuable member of a team composed of much more skilled and capable developers than myself. 

The humility I gain by reminiscing about my ignorance and ineptitude in all of these ventures helps to keep my ego somewhat grounded.
