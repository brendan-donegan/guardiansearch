import mock
import os
import unittest

from .. import guardianapi

class TestGuardianSearch(unittest.TestCase):

    def test_get_result_json(self):
        # Verify that the correct API call is made and result JSON returned
        # Have to mock the result of requests.get
        expected_json = {
            'response': {
                'status': 'ok',
            }
        }
        with mock.patch('requests.get') as requests_get:
            requests_get.return_value.ok = True
            requests_get.return_value.json.return_value = expected_json
            result_json = guardianapi.get_result_json(
                api_key=os.environ['API_KEY'],
                query="foo bar",
                from_date="2012-06-06",
                to_date="2014-06-06",
                page=2,
            )
            # Assert that requests.get is called correctly
            requests_get.assert_called_once_with(
                guardianapi.GUARDIAN_API,
                params={
                    'api-key': os.environ['API_KEY'],
                    'q': "foo bar",
                    'from_date': "2012-06-06",
                    'to_date': "2014-06-06",
                    'page': 2,
                }
            )
            self.assertEqual(expected_json, result_json)

    def test_get_result_json_not_ok(self):
        # Have to mock the result of requests.get
        expected_json = {}
        result_json = guardianapi.get_result_json(
            api_key=os.environ['API_KEY'],
            query="foo bar",
        )
        self.assertEqual(expected_json, result_json)

    def test_format_results(self):
        # Verify that results are formatted correctly
        expected_formatted = ["result 1 - http://result1.com"]
        formatted_results = guardianapi.format_results(
            [
                {'webTitle': 'result 1', 'webUrl': 'http://result1.com'}
            ]
        )
        self.assertEqual(expected_formatted, formatted_results)

    def test_get_search_results(self):
        # Verify that if there are multiple pages all results are returned
        expected_results = ["result 1 - http://result1.com"]
        received_results = guardianapi.get_search_results(
            query="foo bar",
            from_date="2012-06-06",
            to_date="2014-06-06",
        )
        self.assertEqual(expected_results, received_results)
