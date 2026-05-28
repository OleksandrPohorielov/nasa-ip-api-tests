Feature: Network and IP checks

  Scenario: Public IP should not be in restricted range
    When I retrieve my public IP address
    Then my public IP should not be in the range 101.33.28.0 to 101.33.29.0

  Scenario: Resolve Google public DNS domain
    When I resolve the domain google-public-dns-a.google.com
    Then the resolved IP address should be 8.8.8.8

  Scenario: Traceroute to Google DNS should reach target within 10 hops
    When I perform a traceroute to 8.8.8.8
    Then the target should be reached within 10 hops