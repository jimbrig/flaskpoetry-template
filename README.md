# Flask Application Template

## Design Decisions

- Use [poetry](https://python-poetry.org/) as primary dependency manager and
  package bundler.

- Use [dynaconf](https://www.dynaconf.com/) as primary configuration manager.

- Documentation via [mkdocs]()

- Infrastructure managed via [Terraform]() and hosted on [Azure]().

- Testing suite managed via [pytest]()

- Frontend designed with variety of ...

- Database engine is [Microsoft SQL Server]() (specifically, Azure SQL Server)
  and [SQLAlchemy]() is the ORM of choice.

- Application deployed via custom [Docker Container]()

- Production server ran by [gunicorn]().

- App hosted via [Azure App Service]() using [Custom Linux Docker Container Runtime]().

## Flask Extensions

- [FlaskDynaconf]()
- [Flask-SQLAlchemy]()
- [Flask-Migrate]()
- [Flask-DebugToolbar]()
- [Flask-MonitoringDashboard]()
- [Flask-Healthz]() | [py-healthcheck]()
- [Flask-WTF]()
- [Flask-Assets]()

## API Design

- API designed conforming to the [OpenAPI Standards]() with custom

- API documentation hosted at static route `/docs/<swagger|redoc|rapidoc>`.

- Specification file is under `static/openapi/openapi[.yml|.json]`.


