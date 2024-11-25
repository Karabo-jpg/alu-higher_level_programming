#!/bin/bash
# Fetches the content of the URL provided as the first argument and prints its size in bytes
curl -s "$1" | wc -c
