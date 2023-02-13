from distutils.core import setup

setup(name='hillel_auto_selenium_test',
      version='1.0',
      description='Sample testing project',
      packages=['ui_web_tests'],
      install_requires=['pytest',
                        'selenium',
                        'webdriver-manager',
                        ]
      )