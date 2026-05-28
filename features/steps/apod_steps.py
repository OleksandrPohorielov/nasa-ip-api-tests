import os
from behave import given, when, then
from dotenv import load_dotenv

from src.clients.nasa_client import NasaClient
from src.utils.date_utils import get_yesterday_date


load_dotenv()


@given("I have a valid NASA API key")
def step_have_valid_nasa_api_key(context):
    api_key = os.getenv("NASA_API_KEY")

    assert api_key is not None, "NASA_API_KEY is missing in .env"
    assert api_key.strip() != "", "NASA_API_KEY is empty"


@when("I request the astronomy picture of the day for yesterday")
def step_request_apod_for_yesterday(context):
    yesterday = get_yesterday_date()

    nasa_client = NasaClient()
    context.nasa_response = nasa_client.get_apod(yesterday)


@when('I request the astronomy picture of the day for "{requested_date}"')
def step_request_apod_for_specific_date(context, requested_date):
    nasa_client = NasaClient()
    context.nasa_response = nasa_client.get_apod(requested_date)


@then("the NASA API response status code should be 200")
def step_check_nasa_status_code(context):
    assert context.nasa_response.status_code == 200, (
        f"Expected status code 200, but got {context.nasa_response.status_code}. "
        f"Response body: {context.nasa_response.text}"
    )


@then("the NASA API response should contain required APOD fields")
def step_check_apod_required_fields(context):
    response_json = context.nasa_response.json()

    required_fields = [
        "title",
        "explanation",
        "url",
        "media_type",
        "date"
    ]

    for field in required_fields:
        assert field in response_json, f"Missing required field: {field}"


@then("the media type should be image or video")
def step_check_media_type(context):
    response_json = context.nasa_response.json()

    media_type = response_json.get("media_type")

    assert media_type in ["image", "video"], (
        f"Expected media_type to be image or video, but got: {media_type}"
    )