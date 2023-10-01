class RemoteRepoNotFound(Exception):
    pass


class ErrorAddingRepoToSQLite(Exception):
    pass


class NoEnvironmentFound(Exception):
    pass


class RepoAlreadyExistsOnDB(Exception):
    pass


class NoDataOnRepoDatabase(Exception):
    pass


class NoTopicOnRepo(Exception):
    pass
