#!/bin/python

from scapy.all import *

class cortex(Packet):
  name='cortex'
  fields_desc = [	IntField("Start",1234567890),
  					IntField("size",20),
  					IntField("FlowID",1),
  					IntField("MonRequest",0),
  					IntField("postamble",1234567890)
  				]

srcPort = random.randint(1024,65535)
seq=1000
flags = "S"
packet = IP(dst="10.10.9.100") / TCP(sport=srcPort, dport=8000, flags=flags, seq=seq) / cortex()

rep = sr1(packet)

ack=seq+1
dstSeq=rep.seq

packet = IP(dst="10.10.9.100") / TCP(sport=srcPort, dport=8000, flags="A", seq=dstSeq, ack=ack) / cortex()
rep = sr1(packet)

rep.show()
