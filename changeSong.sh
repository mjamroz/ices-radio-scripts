#!/usr/bin/env bash
kill -SIGUSR1 `ps x |grep "ices ices.conf" |grep -v grep |awk '{print $1}'`
