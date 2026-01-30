# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from werkzeug import urls

from . import _monkeypatches, _monkeypatches_pytz

if not hasattr(urls, 'url_join'):
    # see https://github.com/pallets/werkzeug/compare/2.3.0..3.0.0
    # see https://github.com/pallets/werkzeug/blob/2.3.0/src/werkzeug/urls.py for replacement
    from . import _monkeypatches_urls

from . import appdirs, cloc, osutil, pdf, pycompat, win32
from .config import config
from .convert import *
from .date_utils import *
from .debugger import *
from .float_utils import *
from .func import *
from .image import *
from .js_transpiler import ODOO_MODULE_RE, URL_RE, is_odoo_module, transpile_javascript
from .mail import *
from .misc import *
from .sourcemap_generator import SourceMapGenerator
from .sql import *
from .template_inheritance import *
from .translate import *
from .xml_utils import *
