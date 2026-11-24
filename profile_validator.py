"""Agent profile schema and validator for Base/EVM. Requires jsonschema >= 4.18.

Run tests: python profile_validator.py
Export JSON: python -c "import json, profile_validator as p; print(json.dumps(p.SCHEMA, indent=2))"
"""

from jsonschema import Draft202012Validator, ValidationError


SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Agent profile",
    "type": "object",
    "required": ["name", "bio", "skills", "wallet_address"],
    "additionalProperties": False,
    "$defs": {"nonblank": {"type": "string", "pattern": r"\S"}},
    "properties": {
        "name": {"$ref": "#/$defs/nonblank"},
        "bio": {"$ref": "#/$defs/nonblank"},
        "skills": {
            "type": "array",
            "minItems": 1,
            "uniqueItems": True,
            "items": {"$ref": "#/$defs/nonblank"},
        },
        "wallet_address": {
            "description": "20-byte EVM address; format only, not ownership or checksum.",
            "type": "string",
            "minLength": 42,
            "maxLength": 42,
            "pattern": "^0x[0-9A-Fa-f]{40}$",
        },
    },
}

_validator = Draft202012Validator(SCHEMA)


def validate_profile(profile):
    """Return None on success; raise jsonschema.ValidationError on invalid input."""
    _validator.validate(profile)


if __name__ == "__main__":
    import unittest

    class ProfileTests(unittest.TestCase):
        profile = {
            "name": "Atlas",
            "bio": "Turns public data into charts.",
            "skills": ["SQL", "data visualization"],
            "wallet_address": "0x" + "aB" * 20,
        }

        def test_valid(self):
            validate_profile(self.profile)

        def test_all_fields_required(self):
            for field in self.profile:
                with self.subTest(field=field), self.assertRaises(ValidationError):
                    validate_profile({k: v for k, v in self.profile.items() if k != field})

        def test_bad_fields(self):
            for field, value in [
                ("name", "  "), ("bio", 99), ("skills", "writing"),
                ("skills", []), ("skills", [" "]), ("skills", ["SQL", "SQL"]),
                ("wallet_address", "0x" + "a" * 39),
                ("wallet_address", "0x" + "z" * 40),
                ("wallet_address", self.profile["wallet_address"] + "\n"),
                ("wallet_adress", self.profile["wallet_address"]),
            ]:
                with self.subTest(field=field, value=value), self.assertRaises(ValidationError):
                    validate_profile({**self.profile, field: value})

    unittest.main()
