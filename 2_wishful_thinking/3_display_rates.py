# Wishful thinking is a powerful technique for building software programs.
from datetime import date


def display_todays_usd_to_cad_rate():
    # Do something here to get the rate...
    today = date.today()
    todays_rate = get_usd_to_cad_rate(today)
    # and then just print out the rate
    print(f"Today's USD to CAD rate is: {todays_rate}")


# The function above might have us thinking, how do we want to build supporting functions....


def get_usd_to_cad_rate(date):
    # Wouldn't it be nice if we could call a function
    # to get the most recent rates from an API,
    # say the last 5 days...
    response = get_recent_rates_from_api(days=5)
    # And then we had a function do any parsing or manipulation
    # necessary...
    rates = parse_rates_from_api_response(response)
    # And then we could just call a function that would filter all
    # the rates by the date.
    return filter_rates_by_date(rates, date)


import requests


def get_recent_rates_from_api(days):
    r = requests.get(
        f"https://www.bankofcanada.ca/valet/observations/FXUSDCAD/json?recent={days}"
    )
    return r.json()


def parse_rates_from_api_response(response):
    observations = response["observations"]
    rates = {}
    for observation in observations:
        obs_date, obs_rate = extract_date_and_rate(observation)
        rates[obs_date] = obs_rate
    return rates


def extract_date_and_rate(observation):
    return (observation["d"], observation["FXUSDCAD"]["v"])


def filter_rates_by_date(rates, date):
    return rates[str(date)]


# We can also combine this wishful thinking approach with something resembling TDD.

# These tests would work on the data
def test_parse_rates_from_api_response():
    response = {
        "observations": [
            {"d": "2021-11-23", "FXUSDCAD": {"v": "1.2707"}},
            {"d": "2021-11-22", "FXUSDCAD": {"v": "1.2680"}},
        ]
    }
    rates = parse_rates_from_api_response(response)
    assert rates == {"2021-11-23": "1.2707", "2021-11-22": "1.2680"}


def test_extract_date_and_rate():
    observation = {"d": "2021-11-23", "FXUSDCAD": {"v": "1.2707"}}
    date, rate = extract_date_and_rate(observation)
    assert date == "2021-11-23"
    assert rate == "1.2707"


def test_filter_rates_by_date():
    today = "2021-11-23"
    rates = {"2021-11-23": "1.2707", "2021-11-22": "1.2680"}
    result = filter_rates_by_date(rates, today)
    assert result == "1.2707"


# These tests would call the API
import pytest


@pytest.mark.default_cassette("valet.yaml")
@pytest.mark.vcr
def test_display_todays_usd_to_cad_rate(capsys):
    display_todays_usd_to_cad_rate()
    captured = capsys.readouterr()
    assert "Today's USD to CAD rate is: 1.2707" in captured.out


@pytest.mark.default_cassette("valet.yaml")
@pytest.mark.vcr
def test_get_usd_to_cad_rate():
    today = "2021-11-23"
    rate = get_usd_to_cad_rate(today)
    assert rate == "1.2707"


@pytest.mark.default_cassette("valet.yaml")
@pytest.mark.vcr
def test_get_recent_rates_from_api():
    api_response = get_recent_rates_from_api(5)
    assert len(api_response["observations"]) == 5
