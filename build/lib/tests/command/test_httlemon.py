from unittest import mock

import pytest

from command.httlemon import httlemon


class TestHttLemon:

    @mock.patch('command.httlemon.client_request')
    def test_it_prints_request_beautified_response(
        self,
        mock_client_request,
        capsys,
    ):

        mock_client_request.return_value = 'No request: not enough lemon!'

        with pytest.raises(SystemExit):
            httlemon(['post', 'http://lemon.com/api/resource/'])

        out, err = capsys.readouterr()
        mock_client_request.assert_called_once_with(
            'post',
            'http://lemon.com/api/resource/',
        )
        assert out == 'No request: not enough lemon!\n'
