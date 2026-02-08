# schemas/fact_schema.py

fact_schema = {
    "type": "object",
    "properties": {
        "fact": {"type": "string"},
        "length": {"type": "number"}
    },
    "required": ["fact", "length"]
}
