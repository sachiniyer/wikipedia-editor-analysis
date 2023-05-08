#!/bin/bash

source_dir="temp"
target_dir="output"

files=$(ls "${source_dir}")

for file in ${files}; do

  if [ -e "${target_dir}/${file}.csv" ]; then
    echo "File ${file} exists in the target directory, deleting it."
    rm "${target_dir}/${file}.csv"
  else
    echo "File ${file} does not exist in the target directory."
  fi

done
