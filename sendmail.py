#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
import sys
from email.mime.text import MIMEText

def sendmail(port, from_addr, to_addr, subject, text):

    argvs = sys.argv

    msg = MIMEText(text,"plain", "utf-8")

    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr

    s = smtplib.SMTP("localhost", port)

    s.sendmail(
        from_addr,
        [to_addr],
        msg.as_string(),
        )

    s.quit()

if __name__ == "__main__":
    argvs = sys.argv
    PORT = argvs[1]
    FROM_ADDR = argvs[2]
    TO_ADDR = argvs[3]
    SUBJECT = argvs[4]
    TEXT = argvs[5]
    sendmail(PORT, FROM_ADDR, TO_ADDR, SUBJECT, TEXT)
