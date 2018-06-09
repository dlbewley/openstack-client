#!/usr/bin/env bash
# remove OS environment vars

for v  in $(env |grep ^OS_ | cut -f1 -d=); do
    echo "unsetting $v";
    unset $v;
done
