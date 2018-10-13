import os
import unittest

import requests

from test import configuration as testConfiguration
from configuration import configuration as projectConfiguration


class TestSmogonIsResponsive(unittest.TestCase):
    def test_ping(self):
        pingNumberOfPackets = testConfiguration['health']['PingNumberOfPackets']
        pingTimeout = testConfiguration['health']['PingTimeout']
        hostName = projectConfiguration['smogon.com']['HostName']
        pingResponse = os.system("ping -c {} -W {} {} > /dev/null".format(pingNumberOfPackets, pingTimeout, hostName))
        self.assertEqual(pingResponse, 0, "The server at {} did not respond to ping.".format(pingResponse))

    def test_http_get(self):
        url = "https://{}/".format(projectConfiguration['smogon.com']['HostName'])
        httpTimeout = float(projectConfiguration['smogon.com']['HttpTimeout'])
        response = requests.get(url, timeout=httpTimeout)
        self.assertEqual(response.status_code, 200, "The server at {} did not respond with 200.".format(url))
