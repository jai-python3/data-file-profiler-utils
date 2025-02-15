#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=7.0',
    "Rich",
    "file-helper-utils",
    "PyYAML",
]

test_requirements = [ ]

setup(
    author="Jaideep Sundaram",
    author_email='jai.python3@gmail.com',
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.10',
    ],
    description="A Python module for simple data file profiling.",
    entry_points={
        'console_scripts': [
            'profile-data-file=data_file_profiler_utils.profile_data_file:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='data_file_profiler_utils',
    name='data_file_profiler_utils',
    packages=find_packages(include=['data_file_profiler_utils', 'data_file_profiler_utils.*']),
    package_data={
        "data_file_profiler_utils": [
            "conf/config.yaml",
        ]
    },
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jai-python3/data-file-profiler-utils',
    version='0.1.3',
    zip_safe=False,
)
