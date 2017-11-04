import unittest

from .. import guardianapi

class TestGuardianSearch(unittest.TestCase):

    def test_get_result_json(self):
        # Verify that the correct API call is made and result JSON returned
        # Have to mock the result of requests.get
        expected_json = {}
        result_json = guardianapi.get_result_json(
            query="foo bar",
            from_date="2012-06-06",
            to_date="2014-06-06",
            page=2,
        )
        # Assert that requests.get is called correctly
        self.assertEqual(expected_json, result_json)

    def test_get_result_json_not_ok(self):
        # Have to mock the result of requests.get
        expected_json = {}
        result_json = guardianapi.get_result_json(
            query="foo bar",
        )

    def test_format_results(self):
        # Verify that results are formatted correctly
        expected_formatted = ""
        formatted_results = guardianapi.format_results({})
        self.assertEqual(expected_formatted, formatted_results)
