from unittest.case import TestCase
from unittest.mock import MagicMock

from apiwrapper.clients.api_client import ApiClient


class EndpointTest(TestCase):

    def setUp(self, testing_class):
        self.api_client = ApiClient()
        self.test_class = testing_class(self.api_client)
        self.test_class._make_get_request = MagicMock(
            side_effect=self.side_effect)

    def side_effect(self, endpoint):
        return endpoint

    def assert_endpoints(self, endpoint_should_be, endpoint_to_check):
        assert (endpoint_to_check == endpoint_should_be), \
            self.print_assertion_error(endpoint_should_be, endpoint_to_check)

    def print_assertion_error(self, endpoint_should_be, endpoint_to_check):
        return "Should be: " + endpoint_should_be + " but was: " + \
          endpoint_to_check
