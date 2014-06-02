#!/bin/bash
./manage.py dumpdata --settings=administer_settings --indent=2 -e auth.Permission -e admin -e contenttypes -e sessions  > initial_data.json
