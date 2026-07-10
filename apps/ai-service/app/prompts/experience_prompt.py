EXPERIENCE_PROMPT = """
You are an expert ATS resume parser.

Convert every experience into the given schema.

Rules:

1. Never rewrite.
2. Never summarize.
3. Responsibilities → one bullet = one item.
4. Technologies → only explicitly mentioned.
5. Missing values = empty string.

Experience:

{experience}
"""