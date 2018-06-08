#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
import sys
from email.mime.text import MIMEText

def sendmail(port, from_addr, to_addrs, data):

    s = smtplib.SMTP("localhost", port)

    s.sendmail(
        from_addr,
        to_addrs,
        data
        )

    s.quit()

if __name__ == "__main__":
    argvs = sys.argv
    PORT = argvs[1]
    FROM_ADDR = argvs[2]
    TO_ADDRS = argvs[3]
    DATA = argvs[4]
    sendmail(PORT, FROM_ADDR, TO_ADDRS, DATA)
