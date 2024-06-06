# -*- coding: utf-8 -*-


!pip install aperturedb
# !pip install cohere

!adb config ls

!adb config create podcast_search

!adb utils execute status

!adb utils visualize-schema

# Dependencies
import json
from aperturedb.Images import Images
from aperturedb.Utils import Utils, create_connector
from aperturedb import NotebookHelpers as nh
from aperturedb.Constraints import Constraints
from aperturedb import BlobDataCSV

# Connect to the ApertureDB instance.
db = create_connector()
utils = Utils(db)
print(utils.summary())

!adb ingest from-csv --ingest-type=BLOB transcripts_ingestion.csv

q = [
  {
    "FindBlob": {
      "constraints": {
        "type": [
          "==",
          "transcript"
        ]
      },
      "blobs": True,
      "results": {
        "all_properties": True
      }
    }
  }
]
responses, blobs = db.query(q)
print(db.get_last_response_str())

print(responses[0]["FindBlob"]["entities"][0]["page_url"])
