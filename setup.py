#!/usr/bin/env python

from setuptools import setup

setup(
    name='DTU-RM_notifier',
    version='1.0.1',
    description="GUI for DTU's resume manager",
    long_description="This python package initiates a notification tool displaying the latest updates from DTU's resume manager",
    author='Dushyant Rathore',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stablegit
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords = "DTU resume manager notification tool",
    author_email='dushyant.bgs@gmail.com',
    url='https://github.com/dushyantRathore/DTU_RM_Notifier',
    packages=['RMnotifier'],
    install_requires=[
        "mechanize",
        "requests<=2.11.1",
        "beautifulsoup4"
    ],
    entry_points={
        'console_scripts':
            ['RMnotifier = RMnotifier.RM_Main:main']
    }
)