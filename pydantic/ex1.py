def print_args(*args, **kwargs):
    print("Positional arguments: ", args)
    print("Keyword arguments: ", kwargs)

print_args(1, 2, "abc", a=1, b=2)
