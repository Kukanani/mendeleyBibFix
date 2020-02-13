#!/bin/bash

sed \
-e 's/month = {1}/month = jan/g' \
-e 's/month = {2}/month = feb/g' \
-e 's/month = {3}/month = mar/g' \
-e 's/month = {4}/month = apr/g' \
-e 's/month = {5}/month = may/g' \
-e 's/month = {6}/month = jun/g' \
-e 's/month = {7}/month = jul/g' \
-e 's/month = {8}/month = aug/g' \
-e 's/month = {9}/month = sep/g' \
-e 's/month = {10}/month = oct/g' \
-e 's/month = {11}/month = nov/g' \
-e 's/month = {12}/month = dec/g' \
$1