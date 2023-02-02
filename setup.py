from distutils.core import setup

setup(name='Selenium test project',
      version='1.0',
      description='Sample testing project',
      packages=['web_test'],
      install_requires=['pytest',
                        'selenium',
                        'webdriver-manager',
                        ]
      )