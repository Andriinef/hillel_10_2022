import functools


# MODIFY THIS DECORATOR
def reverse_string(func):
    """If output is a string, reverse it. Otherwise, return None."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        to_be_reversed = func(*args, **kwargs)
        if isinstance(to_be_reversed, int):
            to_be_reversed = str(to_be_reversed)
        _reversed = to_be_reversed[::-1]
        if isinstance(to_be_reversed, int):
            _reversed = int(_reversed)
        return _reversed

    return wrapper


# TARGET FUNCTIONS
@reverse_string
def get_university_name() -> str:
    return "Western Institute of Technology and Higher Education"


@reverse_string
def get_university_founding_year() -> int:
    return 1957


# TEST OUPUT
print(get_university_name(), get_university_founding_year(), sep="\n")
