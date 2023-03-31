from distutils.core import setup

setup(name='Hillel_auto_tests',
      version='1.0',
      description='Sample testing project',
      packages=['ui_web_tests', 'api_tests_v2'],
      install_requires=['pytest',
                        'selenium',
                        'webdriver-manager',
                        'allure-pytest',
                        'allure-pytest',
                        'allure-python-commons',
                        'pylint-gitlab',
                        'pylint-pytest',
                        'pytest-check',
                        'pytest-xdist',
                        'webdriver-manager',
                        'pylint',
                        'jsonpath',
                        'requests',
                        'randomuser'
                        ]
      )


