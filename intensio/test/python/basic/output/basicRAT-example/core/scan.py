# -*- coding: utf-8 -*-
import socket
ptcqQnsYbNiTmBucYhVDQPrLJMAteEwx = [ 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 179, 443, 445,
514, 993, 995, 1723, 3306, 3389, 5900, 8000, 8080, 8443, 8888 ]
def nJbsVvmkIEyjoTbMKITynVDBoOUcrQfH(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        return 'Error: Invalid IP address.'
    LYrLArXEKHtLdMkUOPrCGRxYmOfobMyc = ''
    for jlhecqcTXPPgOJPSmDwrBwNMWxAUbLrv in ptcqQnsYbNiTmBucYhVDQPrLJMAteEwx:
        KnysYSpUilAculyoRPGzkvTtOEZhUaga = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        gxjBBtJpSQzeZzTHlbQmriNvBgrcyFxz = KnysYSpUilAculyoRPGzkvTtOEZhUaga.connect_ex((ip, jlhecqcTXPPgOJPSmDwrBwNMWxAUbLrv))
        socket.setdefaulttimeout(0.5)
        rXCSYSCjglQMGSmXEAQRMIWgYlHYkRZC = 'open' if not gxjBBtJpSQzeZzTHlbQmriNvBgrcyFxz else 'closed'
        LYrLArXEKHtLdMkUOPrCGRxYmOfobMyc += '{:>5}/tcp {:>7}\n'.format(jlhecqcTXPPgOJPSmDwrBwNMWxAUbLrv, rXCSYSCjglQMGSmXEAQRMIWgYlHYkRZC)
    return LYrLArXEKHtLdMkUOPrCGRxYmOfobMyc.rstrip()
