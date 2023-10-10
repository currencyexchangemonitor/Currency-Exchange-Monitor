# Code Structure

This document provides an overview of the organization and structure of the Python script in this repository. Understanding the code structure will help you navigate and make modifications as needed.

## File Structure

The codebase is organized as follows:

- `project_folder/`
  - `currency_exchange_monitor.py`  (Main Python script)
  - `Documentation/` (Project documentation)
    - `usage.md`  (Instructions on script usage)
    - `contributing.md`  (Guidelines for contributors)
    - `code_structure.md`  (Explanation of code structure)
  - `requirements.txt`  (Project dependencies)
  - `tests/`  (Unit tests, if applicable)
  - `README.md`  (Project README)

### Main Script: `currency_exchange_monitor.py`

- Entry point of the application.
- Handles user interaction, input, and execution of the core functionality.
- Divided into several sections, including:
  - Import statements
  - Function definitions
  - Main execution logic
  - User input handling
  - Integration with external APIs (e.g., Twilio)
  - Integration with the `uagents` library for periodic tasks
  - Error handling

### Function Definitions

1. `get_exchange_rate(base_currency, target_currency)`: Retrieves the exchange rate between two currencies from an external API.

2. `setup_twilio()`: Sets up Twilio account credentials, including the Account SID, Auth Token, and Twilio phone number.

3. `send_twilio_alert(message, client, twilio_phone_number)`: Sends SMS alerts using Twilio to a specified phone number.

4. `print_alert_message(base, target, upper, lower, ctx)`: Checks exchange rate thresholds, prints alerts, and handles user interaction for updating thresholds or removing currency pairs.

### Integration with `uagents`

- Utilizes the `uagents` library to schedule and execute periodic tasks.
- Utilizes the `@alice.on_interval(period=rate_check_interval)` decorator to define an asynchronous function that periodically checks exchange rate thresholds and sends alerts based on the specified interval.

## Dependencies

The script relies on the following Python libraries:
- `twilio`: Used for sending SMS alerts.
- `requests`: Used for making HTTP requests to retrieve exchange rate data.
- `uagents`: Used for scheduling and executing periodic tasks.

## Conclusion

Understanding the code structure will help you explore, modify, and contribute to this project effectively. If you have any questions or need assistance, refer to the documentation or reach out to the project maintainers.
