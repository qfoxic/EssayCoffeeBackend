#!/bin/bash
./manage.py dumpdata --settings=dev_administer_settings --indent=2 -e admin -e contenttypes -e sessions  > initial_data.json
