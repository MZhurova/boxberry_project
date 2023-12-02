from pathlib import Path

from selene.support.shared import browser
from selene import have, command

import tests


class MainPage:

    def open(self):
        browser.open('')

    def search(self):
        pass