class GithubAPIRequestFailedError(Exception):
    def __init__(self, *args) -> None:
        super().__init__("Github API request has failed", *args)


class GithubAPIUnavailableError(BaseException):
    detail = "Github API Unavailable Error"
