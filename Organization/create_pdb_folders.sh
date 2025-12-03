#!/bin/bash

# Get the current directory name
current_dir=$(basename "$PWD")
txt_file="${current_dir}.txt"

if [ -z "$txt_file" ]; then
    echo "No .txt file found in current directory."
    exit 1
fi

# skip first line (header) and process rows
tail -n +2 "$txt_file" | while IFS=',' read -r pdb segment; do
    
    # clean whitespace
    pdb=$(echo "$pdb" | tr -d ' ')
    segment=$(echo "$segment" | tr -d ' ')

    # pdb_id is first four characters
    pdb_id=${pdb:0:4}

    # extract chain from the "start-end:CHAIN" format
    # segment example: 76-158:A → chain = A
    chain=$(echo "$segment" | awk -F':' '{print $2}')

    # folder name = pdb:chain  (e.g., 1grj:A)
    folder_name="${pdb_id}:${chain}"

    mkdir -p "$folder_name"
    echo "Created folder: $folder_name"

done
