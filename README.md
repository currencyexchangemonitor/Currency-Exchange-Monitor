# Currency Exchange Rate Monitoring with SMS Alerts

This Python script allows you to monitor currency exchange rates between different currency pairs and receive SMS alerts using Twilio when the exchange rate goes above or below specified thresholds. It integrates with the `uagents` library to schedule regular rate checks.

## Prerequisites

Before using this script, make sure you have the following prerequisites:

1. Python 3.x installed on your system.
2. Twilio account credentials (Account SID and Auth Token).
3. A valid Twilio phone number to send SMS alerts.
4. The `twilio`, `requests`, and `uagents` Python libraries installed. You can install them using pip:

   ```bash
   pip install twilio requests uagents
5. requirements.txt file will allow users to install these dependencies using pip install -r requirements.txt
   
## Getting Started

1. Clone this repository or download the script `currency_exchange_monitor.py`.

2. Modify the following variables in the script with your own Twilio account information:

   - `account_sid`: Your Twilio Account SID.
   - `auth_token`: Your Twilio Auth Token.
   - `twilio_phone_number`: Your Twilio phone number (from which alerts will be sent).

3. Replace the existing exchange rate API key in the script with your own. You can obtain an API key from `v6.exchangerate-api.com` and replace it to ensure accurate rate information. The key is located in this line of the script:

   ```python
   response = requests.get(f'https://v6.exchangerate-api.com/v6/86639d518exxxxxxx/latest/{base_currency}')

4. Ensure that the `requests` library is correctly installed. If not, install it using `pip`.

5. Run the script:

   ```bash
   python currency_exchange_monitor.py

## Usage

Follow these steps to monitor currency exchange rates and receive SMS alerts:

1. Enter the base currency (e.g., USD) and target currency (e.g., EUR) when prompted. The script will display the current exchange rate for 1 unit of the base currency to the target currency.

2. Set the upper and lower thresholds for the exchange rate. The script will monitor the rate and send alerts if it goes above or below these thresholds.

3. You can choose to add more currency pairs to monitor or stop by entering 'yes' or 'no' when prompted.

4. Specify the exchange rate check interval in seconds. The script will check the rates at this interval.

5. The script will continuously monitor the specified currency pairs and send SMS alerts via Twilio when the exchange rates cross the specified thresholds.

## Alerts

- When the exchange rate goes above the upper threshold, you will receive an SMS alert with an option to update the thresholds for that currency pair.

- When the exchange rate goes below the lower threshold, you will receive an SMS alert with an option to update the thresholds for that currency pair.

- If you choose to update the thresholds, you can modify the upper and lower values for better monitoring.

## Important Notes

- Make sure the lower threshold is less than the upper threshold.

- Currency pairs must be distinct; you cannot monitor the same pair with different thresholds.

- If you are using a free Twilio account and want to receive SMS alerts, you will need to verify the phone number to which you intend to receive the alerts in your Twilio account settings.

- This script utilizes the `v6.exchangerate-api.com` to fetch exchange rate data. You can obtain an API key from `v6.exchangerate-api.com`.
  
- Once an alert is sent, you can modify the threshold values or stop monitoring that currency pair.

Please feel free to contribute to or enhance this script as needed. If you encounter any issues or have questions, don't hesitate to reach out.

**Note**: Ensure you have the required Twilio credit to send SMS alerts.
