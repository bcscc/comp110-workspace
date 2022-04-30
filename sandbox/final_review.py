a: dict[str, list[int]] = {"a": [1, 2, 3], "b": [100, 2, 3]}

def x(a: dict[str, list[int]]) -> dict[str, bool]:
    result: dict[str, bool] = {}
    for i in a:
        result[i] = sum(a[i]) > 100
    return result

def factorial(a: int, b: int = 1) -> int:
    product: int = b
    if a == 1:
        return product
    else:
        product = product * (a - 1)
        return factorial((a - 1), product)

print(factorial(4))