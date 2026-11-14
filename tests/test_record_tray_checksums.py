"""The release ledger records each asset's checksum and the schema major the build reads."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import record_tray_checksums as ledger  # noqa: E402


class RecordTrayChecksumsTests(unittest.TestCase):
    def test_records_checksum_and_schema_major_per_release(self):
        with tempfile.TemporaryDirectory() as tmp:
            asset = Path(tmp) / "cdx-tray-0.18.0-x86_64-unknown-linux-musl.tar.gz"
            asset.write_bytes(b"fictional asset")
            path = Path(tmp) / "release-archives.json"
            self.assertEqual(ledger.record(path, [str(asset)], major=1), [("v0.18.0", "x86_64-unknown-linux-musl")])
            entry = json.loads(path.read_text())["releases"]["v0.18.0"]
            self.assertEqual(entry["schema_major"], 1)
            self.assertEqual(entry["tray_assets"]["x86_64-unknown-linux-musl"], ledger.sha256(asset))

    def test_refuses_a_file_that_is_not_a_tray_asset(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(SystemExit):
                ledger.record(Path(tmp) / "ledger.json", [str(Path(tmp) / "other.tar.gz")], major=1)

    def test_reads_the_schema_major_from_the_tray_source(self):
        self.assertGreaterEqual(ledger.schema_major(), 1)


if __name__ == "__main__":
    unittest.main()
