#!/bin/sh

sudo pip install flake8 pep8
mv ./pre-commit.py .git/hooks/pre-commit

chmod a+x .git/hooks/pre-commit
rm -- "$0"

