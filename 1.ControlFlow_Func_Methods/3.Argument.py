# 1. normal argument
# 2. default argument
# 3. *args      type(args) = tuple
# 4. **kwargs   type(kwargs) = dict


def func(p1, p2, p3=100, *args, **kwargs):
    print(p1, p2, p3, args, kwargs)

    