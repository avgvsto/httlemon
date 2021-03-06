import json

from backend_http.do_request import (
    InvalidUrl,
    HttpVerbNotImplemented,
    do_request,
)


def client_request(http_verb, url):

    try:

        response = do_request(http_verb, url)

        return beautify_response(response)

    except InvalidUrl:

        return 'No request: the provided url is invalid.'

    except HttpVerbNotImplemented:

        return 'No request: the provided HTTP verb is not allowed.'


def beautify_response(response):

    status_code = 'Status code: {}'.format(response.status_code)
    beautiful_json = beautify_json_dict(response.json())
    response_text = 'Response:\n\n{}'.format(beautiful_json)

    output_response = '{status_code}\n{response_text}'.format(
        status_code=status_code,
        response_text=response_text,
    )

    return output_response


def beautify_json_dict(original_json):

    return json.dumps(original_json, indent=4)
