import unittest

import guardiansearch

class TestGuardianSearch(unittest.TestCase):

    def test_get_result_json(self):
        # Verify that the correct API call is made and result JSON returned
        # Have to mock the result of requests.get
        expected_json = {}
        result_json = guardiansearch.get_result_json(
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
        result_json = guardiansearch.get_result_json(
            query="foo bar",
        )

    def test_format_results(self):
        # Verify that

