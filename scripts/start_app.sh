#!/usr/bin/env bash
pipenv run collectstatic --noinput
pipenv run start
