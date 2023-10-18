# Weather Notification Project

This project is a Python script that provides weather notifications based on the OpenWeatherMap API. It checks the weather forecast for a specific location and sends a text message using Twilio if rain is expected in the next few hours.

## Prerequisites

Before running the script, make sure you have the following:

1. Python installed on your system.
2. The required Python packages installed. You can install them using `pip`:
3. OpenWeatherMap API Key - Get your API key by signing up at [OpenWeatherMap](https://openweathermap.org/api).
4. Twilio Account - Sign up for a Twilio account to get the necessary credentials (Account SID and Auth Token).

## Configuration

To use this script, you need to configure it with your API keys and phone numbers. You can set these values as environment variables or directly in the script.

1. Set the following environment variables:
- `OWN_API_KEY` - Your OpenWeatherMap API key.
- `ACCOUNT_SID` - Your Twilio Account SID.
- `AUTH_TOKEN` - Your Twilio Auth Token.
- `MY_NUMBER` - Your phone number (to receive notifications).

Ensure that you replace the placeholder values with your actual credentials.

Set the MY_LAT and MY_LONG variables to the latitude and longitude of your location. By default, the script is configured for Serres, Greece.

### Usage
The script will check the weather forecast for your location and notify you if rain is expected in the next 12 hours.
If rain is expected, you will receive a text message with the estimated time of rain.
You can choose whether to send the message or not by responding to the script's prompt: "Do you want to send a message? Y or N?"

### Acknowledgments
This project was created as a learning exercise and is not affiliated with any flight data providers or notification services.


