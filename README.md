# Agent profile validator

Validate a JSON agent profile offline. The Draft 2020-12 schema requires a name, bio, nonempty list of distinct skills, and a 20-byte EVM address. The address check is syntactic: it does not verify a checksum, ownership, or blockchain activity. Both examples are synthetic.

## Run

From this directory:

```sh
python -m pip install "jsonschema>=4.18"
python profile_validator.py
```

The second command runs the embedded tests. To validate a file:

```sh
python -c "import json; from profile_validator import validate_profile; validate_profile(json.load(open('valid.json')))"
```

A valid file exits silently. Try `invalid.json` instead: its repeated skill raises `ValidationError`. Other languages can use [the standalone schema](profile.schema.json) with a Draft 2020-12 validator.

[Related service on WURK](https://wurk.fun/store/e6e2088f-e294-4907-829e-3adda1dd6561)
