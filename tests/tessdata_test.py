from __future__ import annotations

import os.path

import tessdata


def test_data_exists():
    data_path = tessdata.data_path()
    assert os.path.exists(data_path)
    assert os.path.exists(os.path.join(data_path, 'osd.traineddata'))
