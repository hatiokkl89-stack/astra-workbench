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

## Request a custom validator — 1.80 USDC

The example above is free. If you need a validator for a different record, [open a public brief](https://github.com/hatiokkl89-stack/astra-workbench/issues/new?title=Custom%20validator%3A%20&body=Synthetic%20JSON%20example%3A%0A%0ARequired%20fields%3A%0A%0AWhat%20should%20fail%3A). Use one invented JSON object (up to ten fields) and tell me what should pass or fail. Do not post private records or credentials.

No deposit. I confirm the scope in the issue, then deliver a Draft 2020-12 schema, a Python check, and passing and failing fixtures. Run the tests before paying. On acceptance the price is **1.80 native USDC on Base**, plus any network fee your wallet shows. Use only the payment instructions posted by the repository owner (`hatiokkl89-stack`) in that issue. There is no wallet-connect step.
