#!/usr/bin/env python
#coding: utf-8

import subprocess
from datetime import datetime

def jtalk(t, s):
    open_jtalk=['open_jtalk']
    mech=['-x', '/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice=['-m', '/usr/share/hts-voice/mei/mei_normal.htsvoice']
    speed=['-r', '{}'.format(s)]
    outwav=['-ow', 'open_jtalk.wav']
    cmd=open_jtalk+mech+htsvoice+speed+outwav
    c = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    c.stdin.write(t)
    c.stdin.close()
    c.wait()
    aplay = ['aplay', '-q', 'open_jtalk.wav']
    wr = subprocess.Popen(aplay)

def say_datetime():
    d = datetime.now()
    text = "{}月{}日、{}時{}分{}秒".format(d.month, d.day, d.hour, d.minute, d.second)
    jtalk(text)

if __name__ == '__main__':
    say_datetime()