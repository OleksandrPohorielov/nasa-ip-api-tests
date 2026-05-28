import ipaddress


def is_ip_in_range(ip_address, start_ip, end_ip):
    current_ip = ipaddress.ip_address(ip_address)
    range_start = ipaddress.ip_address(start_ip)
    range_end = ipaddress.ip_address(end_ip)

    return range_start <= current_ip <= range_end