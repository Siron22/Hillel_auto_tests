from distutils.core import setup

setup(name='Hillel_auto_tests',
      version='1.0',
      description='Sample testing project',
      packages=['ui_web_tests', 'api_tests'],
      install_requires=['pytest',
                        'selenium',
                        'webdriver-manager',
                        'allure-pytest'
                        ]
      )