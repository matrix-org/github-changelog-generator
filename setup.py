#!/usr/bin/env python

from distutils.core import setup

setup(name='github-changelog-generator',
      version='0.1',
      description='Generate changelogs from github PRs',
      scripts=['update_changelog'],
      install_requires=['PyGithub'],
)
