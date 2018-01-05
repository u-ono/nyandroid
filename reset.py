#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import sys
import ta7291

d = ta7291.TA7291(18, 14, 15)
d.cleanup()
