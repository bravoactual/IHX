import time
import random

# List of 100 random WiFi network names
random_wifi_names = [
    "CoffeeShopGuest", "HomeSweetHome", "TechWizards", "SmartHouse", "SpeedyNet",
    "PublicWiFi", "Connectify", "SecureNet", "TechHub", "MyWiFiSpot",
    "Starlink", "DataStream", "WiFiExpress", "GuestNet", "WirelessWorld",
    "HotspotZone", "FastConnect", "EasyAccess", "NetSurfer", "SpeedDemon",
    "WiFiParadise", "Linksys", "iConnect", "TechConnect", "RouterRiders",
    "FreedomNet", "HomeNetwork", "SkyLink", "PowerSurge", "TheInternet",
    "NetNinja", "WebWarriors", "AirWave", "LinkStation", "CafeConnect",
    "NetBlitz", "WiFiWhiz", "BitTorrent", "ConnectMeNow", "FutureNet",
    "BroadbandBuddy", "SpeedySurf", "DigitalDive", "SkyHighNet", "WebSurge",
    "NetMagic", "FastLane", "SurfStream", "WiFiZone", "HotspotHeaven",
    "TechTornado", "NetSprint", "WirelessWonder", "SkyRocket", "CyberSurfer",
    "AirNet", "iStream", "DataDynamo", "SuperNet", "WebWizardry", "LinkWave",
    "StreamSaver", "WiFiGalaxy", "NetSavvy", "SpeedyWeb", "HomeBase",
    "SurfSpot", "WebWarp", "NetworkNirvana", "SpeedBlitz", "FastAccess",
    "AirStream", "CyberNet", "LinkMagic", "Connectopia", "NetNectar",
    "WiFiMaster", "DigitalDream", "SkySurf", "WebWhirlwind", "FastNet",
    "WirelessOasis", "TechTrailblazers", "LinkLagoon", "StreamSlinger",
    "WiFiSphere", "NetNova", "SpeedyLink", "ConnectopiaX", "WebWizard",
    "DataDive", "SkySpeed", "NetNest", "WebWave", "LinkLux", "SurfSafari",
    "WirelessWay", "SpeedySurge", "CloudConnect", "iSurf", "NetNurturer",
    "WebWizardX", "AirAccess", "ConnectopiaUltra", "LinkLegend", "DataDelight",
    "SkySailor", "WiFiWonders", "NetNebula", "SpeedyStream", "WebWanderer"
]

def simulate_network_connection(network):
    print(f"Connecting to {network}...")
    time.sleep(2)  # Simulate some delay
    print("Establishing connection...")
    time.sleep(2)  # Simulate more delay
    print("Connection established.\n")
    time.sleep(1)

def simulate_wifi_search(customer_network):
    print("Searching for available WiFi networks...")
    time.sleep(random.uniform(3, 5))

    # Simulate the discovery of available networks
    available_networks = [customer_network]
    for _ in range(random.randint(4, 9)):
        random_network = random.choice(random_wifi_names)
        available_networks.append(random_network)

    return available_networks

def print_progress_bar(iteration, total, length=50):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    print(f'\rProgress: |{bar}| {percent}% Complete', end='\r')
    if iteration == total:
        print()

def simulate_speed_test():
    download_speed = round(random.uniform(5, 100), 2)  # in Mbps
    upload_speed = round(random.uniform(1, 50), 2)  # in Mbps
    print(f"Download Speed: {download_speed} Mbps, Upload Speed: {upload_speed} Mbps")

def run_diagnostics(network, password):
    # Ask for kill switch activation
    kill_switch = input("Activate fast-forward mode? (Y/N): ").lower() == 'y'

    if kill_switch:
        print("Fast-forward mode activated. Performing quick diagnostics...")
        start_time = time.time()
        while time.time() - start_time < 60:  # Run for 60 seconds
            print("Running quick checks...", end='\r')
            time.sleep(5)  # Simulate a task for 5 seconds

        simulate_speed_test()
        print("\nQuick Diagnostics complete. Network status: Good.")
        return

    # Regular diagnostic process
    issues_found = 0
    issues_resolved = 0
    system_messages = ["Updating network drivers...", "Checking router firmware..."]
    diagnostic_messages = [
        "Checking signal strength", "Updating router firmware", 
        "Scanning for network interference", "Testing network speed"
    ]
    RED = "\033[91m"
    GREEN = "\033[92m"
    RESET = "\033[0m"

    print(f"{GREEN}Running diagnostics for network: {network}{RESET}")

    total_runtime = random.randint(900, 1800)
    elapsed_time = 0

    while elapsed_time < total_runtime:
        check_time = random.uniform(30, 180)
        elapsed_time += check_time
        print_progress_bar(elapsed_time, total_runtime)

        # Select and print a random diagnostic message
        random_message = random.choice(diagnostic_messages)
        print(f"\n{random_message} for {int(check_time)} seconds...")
        time.sleep(check_time)

        # Simulate occasional failures and improvements
        if random.random() < 0.1:
            issues_found += 1
            print(f"{RED}Detected a network issue.{RESET}")
            user_input = input("Attempt auto-fix? (Y/N): ")
            if user_input.lower() == 'y':
                print("Applying auto-fix...")
                time.sleep(random.uniform(5, 20))
                issues_resolved += 1
                print(f"{GREEN}Issue resolved.{RESET}")
                total_runtime += random.randint(60, 180)
            else:
                print("Skipping auto-fix.")

        # Simulate reboot if needed
        if elapsed_time >= total_runtime and issues_found > issues_resolved:
            print("Simulating network device reboot")
            for i in range(5, 0, -1):
                print(f"Rebooting in {i} seconds...", end='\r')
                time.sleep(1)
            print(f"{GREEN}Reboot complete.{RESET}")

    print(f"\nIssues found: {issues_found}, Issues resolved: {issues_resolved}")
    simulate_speed_test()
    print("\nDiagnostics complete.")

    with open("diagnostic_log.txt", "a") as log_file:
        log_file.write(f"Diagnostics run on {network}. Issues found: {issues_found}, Issues resolved: {issues_resolved}\n")
    print("Diagnostic log saved to system.")

def main():
    print("Welcome to AT&T Diagnostic Program")

    # Get user input for customer's network name
    customer_network = input("Please enter your network name: ")

    # Simulate a brief WiFi search
    available_networks = simulate_wifi_search(customer_network)

    print("\nAvailable WiFi networks:")
    for i, network in enumerate(available_networks):
        print(f"{i+1}. {network}")

    # Ask the customer to select the correct WiFi network
    while True:
        try:
            selection = int(
                input("\nPlease select your WiFi network (enter the number): "))
            if 1 <= selection <= len(available_networks):
                customer_network = available_networks[selection - 1]
                break
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Get user input for network password
    password = input("\nPlease enter your network password: ")

# Simulate connecting to the network
    simulate_network_connection(customer_network)

    # Run diagnostics
    run_diagnostics(customer_network, password)

    # Your pitch can start here
    print("\nPlease refer to outside tech")


if __name__ == "__main__":
    main()