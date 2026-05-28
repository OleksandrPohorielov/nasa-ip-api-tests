from behave import when, then

from src.clients.ipinfo_client import IpInfoClient
from src.utils.ip_utils import is_ip_in_range
from src.utils.dns_utils import resolve_domain
from src.utils.traceroute_utils import is_target_reached_within_hops


@when("I retrieve my public IP address")
def step_retrieve_public_ip(context):
    ipinfo_client = IpInfoClient()
    context.public_ip = ipinfo_client.get_public_ip()


@then("my public IP should not be in the range {start_ip} to {end_ip}")
def step_public_ip_should_not_be_in_range(context, start_ip, end_ip):
    is_in_range = is_ip_in_range(context.public_ip, start_ip, end_ip)

    assert not is_in_range, (
        f"Public IP {context.public_ip} is inside restricted range "
        f"{start_ip} - {end_ip}"
    )


@when("I resolve the domain {domain}")
def step_resolve_domain(context, domain):
    context.resolved_ips = resolve_domain(domain)


@then("the resolved IP address should be {expected_ip}")
def step_resolved_ip_should_be(context, expected_ip):
    assert expected_ip in context.resolved_ips, (
        f"Expected {expected_ip}, but resolved IPs were: {context.resolved_ips}"
    )


@when("I perform a traceroute to {target_ip}")
def step_perform_traceroute(context, target_ip):
    context.target_ip = target_ip
    context.max_hops = 10

    reached, target_hop, output = is_target_reached_within_hops(
        target_ip=context.target_ip,
        max_hops=context.max_hops
    )

    context.traceroute_reached = reached
    context.traceroute_target_hop = target_hop
    context.traceroute_output = output


@then("the target should be reached within {max_hops} hops")
def step_target_should_be_reached_within_hops(context, max_hops):
    max_hops = int(max_hops)

    assert context.traceroute_reached, (
        f"Target {context.target_ip} was not reached within {max_hops} hops. "
        f"Target hop: {context.traceroute_target_hop}. "
        f"Traceroute output:\n{context.traceroute_output}"
    )