# Flask

Flask server for the projects page

## Endpoint

All `GET` and `POST` requests are to be sent to `/projects`

## Requests

Requests other than a `GET` request to get the webpage are to use the `POST` method to send `JSON` data. See `postData.js`. The data must contain the key `'action'`, which matches the name of any member function of `ProjectManager` in `projectmanager.py` that doesn't begin with `__` and isn't `parse_request`. For every parameter the function requires, the data should contain the name of the parameter as the key and the value of the parameter as the key's value. For example, the following would be a valid request:

```
{
    'action': 'create',
    'name': 'My Project'
}
```

## Responses

Every `POST` request will be followed by the following JSON response:

```
{
    'status': 200 (action in the request was completed successfully) | 400 (action resulted in an error),
    'data': 'success' | [error code] | [requested data]
}
```