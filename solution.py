

def solve(value):
    return {key: [r for r in value["records"] if r[value["field"]] == key] for key in sorted({r[value["field"]] for r in value["records"]})}
