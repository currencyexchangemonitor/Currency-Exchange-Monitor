import requests
import time
import logging
from twilio.rest import Client
from uagents import Agent, Context

# Set the logging level for the twilio.http_client logger to a higher level (e.g., WARNING)
logging.getLogger('twilio.http_client').setLevel(logging.WARNING)


# Function to fetch the exchange rate
def get_exchange_rate(base_currency, target_currency):
    response = requests.get(f'https://v6.exchangerate-api.com/v6/YOUR-API-KEY/latest/{base_currency}')
    data = response.json()
    conversion_rates = data.get('conversion_rates', {})
    exchange_rate = conversion_rates.get(target_currency)
    return exchange_rate


# Function to set up Twilio account credentials
def setup_twilio():
    account_sid = "Enter your Twilio Account SID"
    auth_token = "Enter your Twilio Auth Token"
    twilio_phone_number = "Enter your Twilio phone number"  # Use your valid Twilio phone number here
    client = Client(account_sid, auth_token)
    return client, twilio_phone_number


# Function to send SMS using Twilio
def send_twilio_alert(message, client, twilio_phone_number):
    try:
        client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to="+917846xxxxxx"  # Replace with the phone number you want to send the alert to (for free twilio account verify the number from your twilio account)
        )
        print("Twilio alert sent successfully.")
    except Exception as e:
        print(f"Error sending Twilio alert: {str(e)}")

# Function to check threeshold and handle printing alert messages
def print_alert_message(base, target, upper, lower, ctx):
    exchange_rate = get_exchange_rate(base, target)
    if exchange_rate is not None:
        message = f'Current rate of 1 {base} is {exchange_rate} {target}'
        ctx.logger.info(message)

        if exchange_rate > upper:
            alert_message = f'Alert: {base} to {target} rate is above {upper}'
            ctx.logger.info(alert_message)
            send_twilio_alert(alert_message, client, twilio_phone_number)

            # Ask the user if they want to update both thresholds
            update_thresholds = input(f"Do you want to update both thresholds for {base} to {target}? (yes/no): ").lower()
            if update_thresholds == 'yes':
                new_upper = float(input('Enter the new upper threshold: '))
                new_lower = float(input('Enter the new lower threshold: '))
                currency_pairs[currency_pairs.index((base, target, upper, lower))] = (base, target, new_upper, new_lower)
            else:
                currency_pairs.remove((base, target, upper, lower))
                ctx.logger.info(f'Removed currency pair {base} to {target} from monitoring.')

        elif exchange_rate < lower:
            alert_message = f'Alert: {base} to {target} rate is below {lower}'
            ctx.logger.info(alert_message)
            send_twilio_alert(alert_message, client, twilio_phone_number)

            # Ask the user if they want to update both thresholds
            update_thresholds = input(f"Do you want to update both thresholds for {base} to {target}? (yes/no): ").lower()
            if update_thresholds == 'yes':
                new_upper = float(input('Enter the new upper threshold: '))
                new_lower = float(input('Enter the new lower threshold: '))
                currency_pairs[currency_pairs.index((base, target, upper, lower))] = (base, target, new_upper, new_lower)
            else:
                currency_pairs.remove((base, target, upper, lower))
                ctx.logger.info(f'Removed currency pair {base} to {target} from monitoring.')


if __name__ == '__main__':
    currency_pairs = []

    while True:
        base_currency = input('Enter the base currency (e.g., USD): ').upper()
        target_currency = input('Enter the target currency (e.g., EUR): ').upper()

        # Check if the currency pair already exists in the list
        if (base_currency, target_currency) in [(pair[0], pair[1]) for pair in currency_pairs]:
            print(f'The currency pair {base_currency} to {target_currency} is already in the list.')
            continue  # Skip adding the existing currency pair

        # Get the exchange rate and display it
        exchange_rate = get_exchange_rate(base_currency, target_currency)
        if exchange_rate is not None:
            message = f'Current rate of 1 {base_currency} is {exchange_rate} {target_currency}'
            print(message)

        while True:
            upper_threshold = float(input('Enter the upper threshold: '))
            lower_threshold = float(input('Enter the lower threshold: '))

            # Check if lower threshold is less than upper threshold
            if lower_threshold >= upper_threshold:
                print("Lower threshold must be less than the upper threshold. Please enter valid thresholds.")
            else:
                break

        currency_pairs.append((base_currency, target_currency, upper_threshold, lower_threshold))

        add_another = input('Do you want to add another currency pair? (yes/no): ').lower()
        if add_another != 'yes':
            break

    rate_check_interval = float(input('Enter the exchange rate check interval (in seconds): '))

    client, twilio_phone_number = setup_twilio()

    # Integration with uagents
    alice = Agent(name="Alice", seed="Alice recovery phrase")

    @alice.on_interval(period=rate_check_interval)
    async def check_thresholds_wrapper(ctx: Context):
        for base, target, upper, lower in currency_pairs:
            print_alert_message(base, target, upper, lower, ctx)

    alice.run()
