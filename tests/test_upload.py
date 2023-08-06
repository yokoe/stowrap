import unittest
import stowrap
from dotenv import load_dotenv
import tempfile
from datetime import datetime
import os

load_dotenv()


class TestUpload(unittest.TestCase):
    def test_gcs_upload(self):
        with tempfile.TemporaryDirectory() as tempdir:
            testfile = os.path.join(tempdir, "test.txt")
            with open(testfile, "w") as f:
                print(datetime.now(), file=f)
                stowrap.Client("gcs").upload(
                    os.environ["TEST_GCS_BUCKET"], testfile, "test.txt"
                )


if __name__ == "__main__":
    unittest.main()
