import platform
import re
import subprocess


def run_traceroute(target_ip, max_hops=10):
    system_name = platform.system().lower()

    if "windows" in system_name:
        command = ["tracert", "-d", "-h", str(max_hops), target_ip]
    else:
        command = ["traceroute", "-n", "-m", str(max_hops), target_ip]

    completed_process = subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=60
    )

    return completed_process.stdout + completed_process.stderr


def find_target_hop(traceroute_output, target_ip):
    for line in traceroute_output.splitlines():
        hop_match = re.match(r"^\s*(\d+)\s+", line)

        if hop_match and target_ip in line:
            return int(hop_match.group(1))

    return None


def is_target_reached_within_hops(target_ip, max_hops):
    output = run_traceroute(target_ip, max_hops)
    target_hop = find_target_hop(output, target_ip)

    return target_hop is not None and target_hop <= max_hops, target_hop, output