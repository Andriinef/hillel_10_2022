# MODIFY THIS DECORATOR
import functools
import random


def mask_data(target_key: str, replace_with: str = "*"):
    """Replace the value of a dictionary with a 'masked' version."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            to_be_masked = func(*args, **kwargs)
            new_dist = {}
            for key, value in to_be_masked.items():
                if key == target_key:
                    value = replace_with * random.randint(4, 8)
                new_dist[key] = value

            return new_dist

        return wrapper

    return decorator


# TARGET FUNCTIONS
@mask_data(target_key="name")
def get_user(name: str, age: int):
    return {"name": name, "age": age}


# TEST OUPUT
print(get_user(name="Alice", age=30), get_user(name="Bob", age=25), sep="\n")
