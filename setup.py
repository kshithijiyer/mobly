# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import platform
import setuptools
from setuptools.command import test
import sys

install_requires = [
    'future', 'portpicker', 'psutil>=5.4.4', 'pyserial', 'pyyaml',
    'timeout_decorator'
]

if sys.version_info < (3, ):
    install_requires.extend([
        'enum34',
        # "futures" is needed for py2 compatibility and it only works in 2.7
        'futures',
    ])

if platform.system() == 'Windows':
    install_requires.append('pywin32')


class PyTest(test.test):
    """Class used to execute unit tests using PyTest. This allows us to execute
    unit tests without having to install the package.
    """

    def finalize_options(self):
        test.test.finalize_options(self)
        self.test_args = ['-x', "tests/mobly"]
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


def main():
    setuptools.setup(
        name='mobly',
        version='1.8.1',
        maintainer='Ang Li',
        maintainer_email='mobly-github@googlegroups.com',
        description='Automation framework for special end-to-end test cases',
        license='Apache2.0',
        url='https://github.com/google/mobly',
        download_url='https://github.com/google/mobly/tarball/1.8.1',
        packages=setuptools.find_packages(exclude=['tests']),
        include_package_data=False,
        scripts=['tools/sl4a_shell.py', 'tools/snippet_shell.py'],
        tests_require=[
            'mock',
            # Needed for supporting Python 2 because this release stopped supporting Python 2.
            'pytest<5.0.0',
            'pytz',
        ],
        install_requires=install_requires,
        cmdclass={'test': PyTest},
    )


if __name__ == '__main__':
    main()
