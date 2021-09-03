

class BaseValidationError(ValueError):
    pass

class NameTooShortError(BaseValidationError):
    pass

class NameTooLongError(BaseValidationError):
    pass


def validate(name):
    if len(name) > 25:
        raise NameTooLongError(name)
    elif len(name) < 2:
        raise NameTooShortError(name)

try:
    validate('MJey')
except BaseValidationError as err:
    raise err 