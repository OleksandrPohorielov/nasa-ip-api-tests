import socket


def resolve_domain(domain):
    results = socket.getaddrinfo(
        domain,
        None,
        family=socket.AF_INET,
        type=socket.SOCK_STREAM
    )

    ip_addresses = set()

    for result in results:
        ip = result[4][0]
        ip_addresses.add(ip)

    return list(ip_addresses)