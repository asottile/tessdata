from __future__ import annotations

import os.path
import sys


def data_path() -> str:
    return os.path.join(sys.prefix, 'share', 'tessdata')
