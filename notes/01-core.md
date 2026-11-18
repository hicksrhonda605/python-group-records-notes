# Group records by a field: implementation

## What the example does

This small-input implementation groups records by a required string field. It sorts group keys for deterministic output; missing fields fail explicitly.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
{
  "field": "team",
  "records": [
    {
      "team": "a",
      "n": 1
    },
    {
      "team": "b",
      "n": 2
    },
    {
      "team": "a",
      "n": 3
    }
  ]
}
```

Expected result:

```json
{
  "a": [
    {
      "team": "a",
      "n": 1
    },
    {
      "team": "a",
      "n": 3
    }
  ],
  "b": [
    {
      "team": "b",
      "n": 2
    }
  ]
}
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
