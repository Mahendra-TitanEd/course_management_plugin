# pylint: disable=open-builtin
from __future__ import absolute_import, print_function, unicode_literals

import os

from setuptools import find_packages, setup
from version import __version__

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
README = open(os.path.join(os.path.dirname(__file__), "README.md")).read()
CHANGELOG = open(os.path.join(os.path.dirname(__file__), "CHANGELOG.rst")).read()

setup(
    name="course-management-plugin",
    version=__version__,
    packages=find_packages(),
    package_data={"": ["*.html"]},  # include any Mako templates found in this repo.
    include_package_data=True,
    license="Proprietary",
    description="Django plugin to enhance Course Management features of base Open edX platform.",
    long_description="",
    author="Mahendra Chaudhari",
    author_email="MahendraC@TitanEd.com",
    url="https://github.com/Mahendra-TitanEd/course_management_plugin.git",
    zip_safe=False,
    keywords="Django, Open edX, example",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={
        # IMPORTANT: ensure that this entry_points coincides with that of edx-platform
        #            and also that you are not introducing any name collisions.
        # https://github.com/openedx/edx-platform/blob/master/setup.py#L88
        "lms.djangoapp": [
            "course_mgmt_plugin = course_mgmt_plugin.apps:CourseMgmtPluginConfig",
        ],
        "cms.djangoapp": [
            "course_mgmt_plugin = course_mgmt_plugin.apps:CourseMgmtPluginConfig",
        ],
    },
    extras_require={
        "Django": ["Django>=2.2,<2.3"],
    },
)
