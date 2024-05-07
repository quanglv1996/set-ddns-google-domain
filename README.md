# Dynamic DNS Update Script

This Python script updates the IP address associated with Dynamic DNS (DDNS) service providers, particularly for Google Domains. It periodically checks the public IP address of the network and updates the DNS records if the IP address has changed.

## Dependencies

- Python 3.x
- Requests library (install using `pip install requests`)

## Configuration

1. Edit the `ddns_dict` dictionary in the script to include your DDNS sub-domains, usernames, passwords, and hostnames.
2. Ensure you have correct permissions to execute the script.
3. Make sure your firewall allows outgoing HTTP/HTTPS connections.

## Usage

1. Modify the `ddns_dict` dictionary with your DDNS configuration details.
2. Run the script using Python 3:

    ```python
        python3 setdns.py
    ```

3. The script will run indefinitely, periodically checking the public IP address and updating DDNS records if necessary.

## Logging

The script logs its activities to a file named `ddns.log` in the same directory as the script itself.

## Note

- Ensure the script is executed on a system with reliable internet connectivity and is capable of running indefinitely.
- Customize error handling and logging mechanisms as per your requirements.
