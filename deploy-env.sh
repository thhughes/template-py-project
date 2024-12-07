#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 deploy-location"
    exit 1
fi

TARGET_DIR="$1"

# Check if the provided argument is a valid directory
if [ ! -d "$TARGET_DIR" ]; then
    echo "Error: '$TARGET_DIR' is not a valid directory."
    exit 2
fi
script_dir=$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")
DIRS_TO_COPY=(
    "${script_dir}/config"
    "${script_dir}/private"
    "${script_dir}/src"
)

for DIR in "${DIRS_TO_COPY[@]}"; do
    if [ -d "$DIR" ]; then
        cp -r "$DIR" "$TARGET_DIR"
        echo "[INFO] deployed [$DIR] to [$TARGET_DIR]"
    fi
done

COPY_FILES=(
    "${script_dir}/env.txt"
    "${script_dir}/requirements.txt"
    "${script_dir}/build.sh"
)
for F in "${COPY_FILES[@]}"; do
    if [ -f "$F" ]; then
        cp "$F" "$TARGET_DIR"
        echo "[INFO] deployed [$F] to [$TARGET_DIR]"
    fi
done