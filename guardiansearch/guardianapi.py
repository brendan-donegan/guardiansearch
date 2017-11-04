import requests


GUARDIAN_API = "http://content.guardianapis.com/search"


def get_result_json(api_key, query=None, from_date=None, to_date=None, page=None):
    # Assemble the parameters of the request
    params = {"api-key": api_key}
    if query is not None:
        params['q'] = query
    if from_date is not None:
        params['from_date'] = from_date
    if to_date is not None:
        params['to_date'] = to_date
    if page is not None:
        params['page'] = page
    response = requests.get(GUARDIAN_API, params=params)
    if response.ok:
        return response.json()
    # If the request fails return the error message
    return response.text


def format_results(results):
    return [r['webTitle'] + " - " + r["webUrl"] for r in results]
