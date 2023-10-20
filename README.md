[![build status](https://github.com/asottile/tessdata/actions/workflows/main.yml/badge.svg)](https://github.com/asottile/tessdata/actions/workflows/main.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/asottile/tessdata/main.svg)](https://results.pre-commit.ci/latest/github/asottile/tessdata/main)

tessdata
========

`pip` installable versions of [tesseract-ocr data]

[tesseract-ocr data]: https://github.com/tesseract-ocr

## usage

usually you'll want to pick a particular package for installation.

currently the following are provided (send a PR to add more!):

- tessdata.eng
- tessdata.fast-eng

these will install to `{prefix}/share/tessdata` -- you can access this
directory path using the `tessdata` api:

```python
import tessdata

print(tessdata.data_path())  # /path/to/venv/share/tessdata
```
