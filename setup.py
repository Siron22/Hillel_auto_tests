from distutils.core import setup

setup(name='Hillel_auto__tests',
      version='1.0',
      description='Sample testing project',
      packages=['ui_web_tests'],
      install_requires=['pytest',
                        'selenium',
                        'webdriver-manager',
                        'allure-pytest'
                        ]
      )