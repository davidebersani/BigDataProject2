#!/bin/bash
# Script to set the correct path in the scripts.
dir="$(pwd)"
mkdir -p scripts
for filename in template-scripts/*; do
    name="$(basename $filename)"
    sed "s@=REPO_DIR=@$dir@g" $filename > scripts/$name
done

