from pathlib import Path

from selene.support.shared import browser
from selene import have, command

import tests


class ECommercePage:

    def open(self):
        browser.open('e-commerce')