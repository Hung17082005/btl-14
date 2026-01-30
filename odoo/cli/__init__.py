import logging
import os
import sys

import odoo

from . import (
    cloc,
    deploy,
    genproxytoken,
    populate,
    scaffold,
    server,
    shell,
    start,
    tsconfig,
)
from .command import Command, main
