#  Copyright 2021, Verizon Media
#  Licensed under the terms of the ${MY_OSI} license. See the LICENSE file in the project root for terms
from unittest import TestCase

from ychaos.settings import ProdSettings, Settings


class TestSettings(TestCase):
    def test_settings_with_no_config_creates_ProdSettings_configuration(self):
        result_settings = Settings.get_instance()
        self.assertIsInstance(result_settings, ProdSettings)

    def test_settings_with_unknown_configuration(self):
        with self.assertRaises(Exception):
            Settings("unknown_config")
