from scapy.all import rdpcap, TCP, Raw
import json

def process_pcap(file_name):
    packets = rdpcap(file_name)  # Read the PCAP file
    y = []  # List to store matching objects

    for packet in packets:
        if packet.haslayer(TCP) and packet.haslayer(Raw):
            data = packet[Raw].load
            try:
                # Attempt to decode the packet's raw data as JSON
                json_data = json.loads(data.decode())
                # Check if the required fields are present
                print(json_data)# Append the object to the list
            except Exception as e:
                # Skip non-JSON or invalid packets
                continue
    
    return y

# Example usage:
pcap_file = "./traffic18112024.pcap"
filtered_data = process_pcap(pcap_file)
# print(filtered_data)
y=[]
# Print the results
for entry in filtered_data:
    print(entry)

