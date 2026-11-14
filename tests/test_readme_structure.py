"""The README keeps the short shape shared with cdx-manager and logics-manager."""
import re
import unittest
from pathlib import Path

README = Path(__file__).resolve().parents[1] / "README.md"


class ReadmeStructureTests(unittest.TestCase):
    def test_shared_sections_in_order_without_subsections(self):
        text = README.read_text(encoding="utf-8")
        self.assertEqual(re.findall(r"(?m)^## (.+)$", text), ["Get started in a minute", "What you can do", "Documentation"])
        self.assertIsNone(re.search(r"(?m)^#{3,} ", text))

    def test_short_and_ends_with_the_licence_line(self):
        lines = README.read_text(encoding="utf-8").rstrip("\n").split("\n")
        self.assertLessEqual(len(lines), 90)
        self.assertIn("MIT licensed", lines[-1])


if __name__ == "__main__":
    unittest.main()
