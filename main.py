import json
import unittest
from datetime import datetime, timezone

# Load JSON files
with open("./data-1.json") as f:
    jsonData1 = json.load(f)

with open("./data-2.json") as f:
    jsonData2 = json.load(f)

with open("./data-result.json") as f:
    jsonExpectedResult = json.load(f)


# 🔹 Convert Format 1
def convertFromFormat1(jsonObject):
    loc = jsonObject["location"].split("/", 4)  # efficient split (max 5 parts)

    return {
        "deviceID": jsonObject["deviceID"],
        "deviceType": jsonObject["deviceType"],
        "timestamp": jsonObject["timestamp"],  # already in ms
        "location": {
            "country": loc[0],
            "city": loc[1],
            "area": loc[2],
            "factory": loc[3],
            "section": loc[4],
        },
        "data": {
            "status": jsonObject["operationStatus"],
            "temperature": jsonObject["temp"],
        },
    }


# 🔹 Convert Format 2
def convertFromFormat2(jsonObject):
    # Faster ISO → ms conversion
    dt = datetime.fromisoformat(jsonObject["timestamp"].replace("Z", "+00:00"))
    timestamp = int(dt.timestamp() * 1000)

    return {
        "deviceID": jsonObject["device"]["id"],
        "deviceType": jsonObject["device"]["type"],
        "timestamp": timestamp,
        "location": {
            "country": jsonObject["country"],
            "city": jsonObject["city"],
            "area": jsonObject["area"],
            "factory": jsonObject["factory"],
            "section": jsonObject["section"],
        },
        "data": jsonObject["data"],  # direct reference (no extra memory)
    }


# 🔹 Main function
def main(jsonObject):
    # Faster check
    if "device" in jsonObject:
        return convertFromFormat2(jsonObject)
    return convertFromFormat1(jsonObject)


# 🔹 Unit Tests
class TestSolution(unittest.TestCase):

    def test_sanity(self):
        self.assertEqual(jsonExpectedResult, jsonExpectedResult)

    def test_dataType1(self):
        self.assertEqual(
            main(jsonData1),
            jsonExpectedResult,
            "Converting from Type 1 failed",
        )

    def test_dataType2(self):
        self.assertEqual(
            main(jsonData2),
            jsonExpectedResult,
            "Converting from Type 2 failed",
        )


if __name__ == "__main__":
    unittest.main()
