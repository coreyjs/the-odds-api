from functools import wraps

ALLOWED_FORMATS = ["json"]


class RequestHelpers:

    @classmethod
    def _set_headers(cls) -> dict[str, str]:
        headers = {"Content-Type": "application/json"}

        return headers

    @staticmethod
    def prepare_request(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            headers = RequestHelpers._set_headers()

            kwargs["headers"] = {**kwargs.get("headers", {}), **headers}
            return func(*args, **kwargs)

        return wrapper
