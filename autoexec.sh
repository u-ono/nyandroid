#!/bin/sh

while :
    do
        exec /usr/bin/env python /opt/nyandroid/reset.py
        exec /usr/bin/env python /opt/nyandroid/rfcomm-server.py
        exec /usr/bin/env python /opt/nyandroid/reset.py
    done
