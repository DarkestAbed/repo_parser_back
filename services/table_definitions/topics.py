import sqlalchemy


class Topics:
    def __init__(self, metadata: sqlalchemy.MetaData) -> None:
        self.metadata = metadata
        topics = sqlalchemy.Table(
            "topics",
            self.metadata,
            sqlalchemy.Column("id", sqlalchemy.Integer),
            sqlalchemy.Column("url", sqlalchemy.String),
            sqlalchemy.Column("topic", sqlalchemy.String),
        )
        return None
