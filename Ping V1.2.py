import socket
import struct
import dns.resolver
import time
import argparse

def get_ip(domain):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8']  # Google's DNS server
    answers = resolver.resolve(domain, 'A')
    for rdata in answers:
        return rdata.address

def send_ping(dest_ip):
    icmp_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    icmp_packet = struct.pack('!BBHHH', 8, 0, 0, 0, 1) + b'pingdata'
    checksum = 0
    for i in range(0, len(icmp_packet), 2):
        checksum += (icmp_packet[i] << 8) + icmp_packet[i + 1]
    checksum = (checksum >> 16) + (checksum & 0xFFFF)
    checksum = ~checksum & 0xFFFF
    icmp_packet = struct.pack('!BBHHH', 8, 0, checksum, 0, 1) + b'pingdata'
    icmp_socket.sendto(icmp_packet, (dest_ip, 1))
    start_time = time.time()
    try:
        response, _ = icmp_socket.recvfrom(1024)
        icmp_type = struct.unpack('!B', response[20:21])[0]
        if icmp_type == 0:
            elapsed_time = time.time() - start_time
            return elapsed_time
    except socket.error:
        pass
    return None

def main(domain, num_requests):
    total_time = 0
    successful_responses = 0
    for _ in range(num_requests):
        ip = get_ip(domain)
        response_time = send_ping(ip)
        if response_time is not None:
            total_time += response_time
            successful_responses += 1
    if successful_responses > 0:
        avg_ping = total_time / successful_responses
        packet_loss = ((num_requests - successful_responses) / num_requests) * 100
        print(f'Average Ping: {avg_ping} ms')
        print(f'Packet Loss: {packet_loss}%')
    else:
        print('All requests failed.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('domain', help='Domain or IP address to ping')
    parser.add_argument('num_requests', type=int, help='Number of ping requests')
    args = parser.parse_args()
    main(args.domain, args.num_requests)