#!/bin/bash


for item in *; do
  if [ -d "$item" ]; then
    echo "$item is a directory"
  elif [ -f "$item" ]; then
    echo "$item is a file"
  else
    echo "$item is not a file or a directory"
  fi
done
