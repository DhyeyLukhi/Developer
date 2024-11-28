from urllib.parse import urlencode, urlunparse

# Define the base components of the URL
scheme = 'https'
netloc = 'example.com'
path = '/somepage'
params = {'param1': 'value1', 'param2': 'value2'}

# Encode the query parameters
query = urlencode(params)

# Construct the URL
url = urlunparse((scheme, netloc, path, '', query, ''))
print(url.translate())

# print(url)
