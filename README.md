# Computer-Networks-Ping

## Overview

This project implements a Python-based tool to measure the ping response time for a specific server. Inspired by the traditional ping command, it evaluates the Round-Trip Time (RTT) and Packet Loss Rate for client-server communications.

The tool allows users to:

1. Check access speeds to a server.
2. Calculate minimum, maximum, and average RTT values.
3. Measure packet loss percentages.

It supports both domain names and IP addresses as input and provides detailed results for network analysis.

## Features

### Validation of IP Addresses:
* Confirms if an input string is a valid IP address using socket.inet_pton.

### Domain-to-IP Resolution:
* Resolves domain names to their respective IP addresses using dns.resolver.Resolver.

### Reverse DNS Lookup:
* Retrieves the domain name associated with an IP address.

### Ping Implementation:
* Sends ICMP echo requests to the specified destination.

* Measures RTT for each packet.

* Reports packet loss rates.

### Customizable Request Count:
* Users can define the number of requests sent during the ping process.

## Dependencies

This project requires the following Python libraries:

    sys: Interaction with the Python interpreter.
    time: Measuring elapsed time during operations.
    struct: Handling binary data.
    socket: Network communication and address validation.
    dns: Domain resolution.

To install dependencies, run:

    pip install dnspython

## **How It Works**

### Input Handling:
The user specifies a domain name or an IP address as the target.

The tool verifies and resolves the input accordingly.

### Packet Sending:
The program sends a specified number of ICMP echo requests to the target.

### Response Analysis:
For each response, the RTT is calculated and recorded.

If no response is received within a timeout, the packet is marked as lost.

### Result Reporting:
Outputs RTT statistics (minimum, maximum, average).

Calculates and displays the percentage of packet loss.
