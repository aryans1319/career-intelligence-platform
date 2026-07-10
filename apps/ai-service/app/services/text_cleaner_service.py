import re


class TextCleanerService:

    def clean(self, text: str) -> str:

        # Normalize line endings
        text = text.replace("\r\n", "\n")
        text = text.replace("\r", "\n")

        # Insert newline before common section headings
        headings = [
            "Experience",
            "Projects",
            "Technical Skills",
            "Skills",
            "Education",
            "Certifications",
            "Achievements",
            "Summary",
        ]

        for heading in headings:
            text = re.sub(
                rf"(?<!\n){heading}",
                f"\n{heading}",
                text,
            )

        # Collapse multiple spaces
        text = re.sub(r"[ \t]+", " ", text)

        # Collapse multiple blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text.strip()