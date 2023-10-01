import sqlalchemy


class Repos:
    def __init__(self, metadata: sqlalchemy.MetaData) -> None:
        self.metadata = metadata
        repos = sqlalchemy.Table(
            "repositories",
            self.metadata,
            sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
            sqlalchemy.Column("url", sqlalchemy.String),
            sqlalchemy.Column("name", sqlalchemy.String),
            sqlalchemy.Column("created_at", sqlalchemy.String),
            sqlalchemy.Column("updated_at", sqlalchemy.String),
            sqlalchemy.Column("pushed_at", sqlalchemy.String),
            sqlalchemy.Column("description", sqlalchemy.String),
            sqlalchemy.Column("fork", sqlalchemy.Boolean),
            sqlalchemy.Column("disabled", sqlalchemy.Boolean),
            sqlalchemy.Column("homepage", sqlalchemy.String),
            sqlalchemy.Column("language", sqlalchemy.String),
            sqlalchemy.Column("private", sqlalchemy.Boolean),
            sqlalchemy.Column("visibility", sqlalchemy.String),
            sqlalchemy.Column("default_branch", sqlalchemy.String),
            sqlalchemy.Column("topics", sqlalchemy.String),
            sqlalchemy.Column("added_date", sqlalchemy.String),
        )
        return None
