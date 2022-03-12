def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two tables into one."""
    result: dict[str, list[str]] = {}
    for i in table1:
        result[i] = table1[i]
    for j in table2:
        if j in result:
            for k in table2[j]:
                result[j].append(k)
        else:
            result[j] = table2[j]
    return result

print(concat({"cat": ["M", "O", "E", "W"]}, {"cat": ["S"], "dog": ["W", "O", "O", "F"]}))