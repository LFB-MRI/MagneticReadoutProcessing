#!/bin/bash
cd "$(dirname "$0")"

for i in *.yml; do
    [ -f "$i" ] || break

    terminalizer render -o "${i%.*}.gif" -q 100 "$i"
done