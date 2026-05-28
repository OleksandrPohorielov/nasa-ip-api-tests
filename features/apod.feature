Feature: NASA Astronomy Picture of the Day API

  Scenario: Retrieve APOD for yesterday
    Given I have a valid NASA API key
    When I request the astronomy picture of the day for yesterday
    Then the NASA API response status code should be 200
    And the NASA API response should contain required APOD fields
    And the media type should be image or video

  Scenario Outline: Retrieve APOD for different dates
    Given I have a valid NASA API key
    When I request the astronomy picture of the day for "<date>"
    Then the NASA API response status code should be 200
    And the NASA API response should contain required APOD fields
    And the media type should be image or video

    Examples:
      | date       |
      | 2024-01-01 |
      | 2024-05-10 |
      | 2025-02-15 |