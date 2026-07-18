"""Rack-aware basit HDFS replikasyon yerleşimi simülasyonu."""
from __future__ import annotations
import random
if __name__ == "__main__":
 random.seed(42);nodes={"rack-a":["dn-a1","dn-a2"],"rack-b":["dn-b1","dn-b2"],"rack-c":["dn-c1"]};first_rack="rack-a";first=random.choice(nodes[first_rack]);other_racks=[rack for rack in nodes if rack!=first_rack];second_rack=random.choice(other_racks);second=random.choice(nodes[second_rack]);third=random.choice(nodes[second_rack])
 print("Blok replikaları:",first,second,third);print("Not: gerçek HDFS yerleşimi ağ topolojisi ve kapasiteye göre daha karmaşıktır.")
