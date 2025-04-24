# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/gueriboutmathieu/micro_llm/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                               |    Stmts |     Miss |  Cover |   Missing |
|--------------------------------------------------- | -------: | -------: | -----: | --------: |
| micro\_llm/\_\_init\_\_.py                         |        0 |        0 |   100% |           |
| micro\_llm/app.py                                  |       27 |       27 |     0% |      1-48 |
| micro\_llm/config/\_\_init\_\_.py                  |        0 |        0 |   100% |           |
| micro\_llm/config/auth\_config.py                  |        8 |        8 |     0% |      1-12 |
| micro\_llm/config/openai\_config.py                |        4 |        4 |     0% |       1-6 |
| micro\_llm/routes/\_\_init\_\_.py                  |        0 |        0 |   100% |           |
| micro\_llm/routes/auth\_routes.py                  |       19 |       19 |     0% |      1-23 |
| micro\_llm/routes/fastapi\_app.py                  |       19 |       19 |     0% |      1-30 |
| micro\_llm/routes/llm\_routes.py                   |        8 |        8 |     0% |      1-16 |
| micro\_llm/routes/utils/\_\_init\_\_.py            |        0 |        0 |   100% |           |
| micro\_llm/routes/utils/origins\_middleware.py     |        9 |        9 |     0% |      1-14 |
| micro\_llm/routes/utils/validate\_user\_wrapper.py |        8 |        8 |     0% |      1-11 |
| micro\_llm/services/\_\_init\_\_.py                |        0 |        0 |   100% |           |
| micro\_llm/services/auth\_service.py               |       24 |       24 |     0% |      1-31 |
| micro\_llm/services/llm\_service.py                |       11 |       11 |     0% |      1-23 |
|                                          **TOTAL** |  **137** |  **137** | **0%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/gueriboutmathieu/micro_llm/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/gueriboutmathieu/micro_llm/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gueriboutmathieu/micro_llm/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/gueriboutmathieu/micro_llm/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Fgueriboutmathieu%2Fmicro_llm%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/gueriboutmathieu/micro_llm/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.