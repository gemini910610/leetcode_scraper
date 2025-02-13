import requests

class LeetCode:
    def __init__(self):
        self.url = 'https://leetcode.com/graphql/'
    def check_response(self, response, key=None):
        if isinstance(response, requests.Response):
            if response.status_code != 200:
                raise Exception(f'HTTP {response.status_code}\n{response.text}')
            response = response.json()
        if key is not None and key not in response:
            raise Exception(f'"{key}" not in response\n{response}')
    def scrape(self, query, params='', **variables):
        query = f'''
            query scrape{params}
            {{
                {query}
            }}
        '''
        data = {
            'query': query,
            'variables': variables
        }
        response = requests.post(self.url, json=data)
        self.check_response(response, 'data')
        return response.json()['data']
    def matched_user(self, query, params='($username: String!)', **variables):
        query = f'''
            matchedUser(username: $username)
            {{
                {query}
            }}
        '''
        response = self.scrape(query, params, **variables)
        self.check_response(response, 'matchedUser')
        return response['matchedUser']
