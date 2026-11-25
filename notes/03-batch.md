# Ordered batch processing for Group records by a field

`batch.py` accepts an outer JSON array containing separate inputs. This is an extra level of nesting when `solve` itself accepts a list. It produces one result envelope per item, preserving input order and zero-based position.

```sh
python3 batch.py < samples/batch.json
```

The batch covers these three input/output pairs:

## Case 1

Input:
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

Result:
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

## Case 2

Input:
```json
{
  "field": "kind",
  "records": [
    {
      "kind": "x"
    }
  ]
}
```

Result:
```json
{
  "x": [
    {
      "kind": "x"
    }
  ]
}
```

## Case 3

Input:
```json
{
  "field": "kind",
  "records": []
}
```

Result:
```json
{}
```

## Partial failures

Each successful item has `ok: true` and `result`. A failed item has `ok: false` and an exception type; later items still run. Exit status 1 means at least one item failed, while status 2 means the batch envelope itself was invalid. An empty outer array is a valid empty batch.

This small-input implementation groups records by a required string field. It sorts group keys for deterministic output; missing fields fail explicitly.

The implementation processes sequentially, avoiding shared-state concurrency and keeping output order predictable. Input is limited to one MiB and 1000 items; this version materializes all results in memory. The next lesson removes that whole-batch memory requirement with line-oriented processing.
