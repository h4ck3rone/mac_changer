#!/usr/bin/python

import subprocess
import argparse
import re

def get_arguments():
    parser = argparse.ArgumentParser(description="MAC Address Changer")
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change MAC address", required=True)
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address", required=True)
    options = parser.parse_args()
    return options

def get_current_mac(interface):
    try:
        ifconfig_result = subprocess.check_output(['ifconfig', interface], text=True)
        mac_address_search = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_result)
        if mac_address_search:
            return mac_address_search.group(0)
        else:
            print("[-] Could not read MAC address.")
            return None
    except subprocess.CalledProcessError as e:
        print(f"[-] Failed to get MAC address: {e}")
        return None

def mac_changer(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    try:
        subprocess.call(['ifconfig', interface, 'down'])
        subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
        subprocess.call(['ifconfig', interface, 'up'])
        print("[+] MAC address was successfully changed.")
    except subprocess.CalledProcessError as e:
        print(f"[-] Failed to change MAC address: {e}")

def main():
    options = get_arguments()

    current_mac = get_current_mac(options.interface)
    if current_mac:
        print(f"[+] Current MAC address: {current_mac}")
    else:
        print("[-] Could not determine the current MAC address.")

    mac_changer(options.interface, options.new_mac)

    updated_mac = get_current_mac(options.interface)
    if updated_mac == options.new_mac:
        print(f"[+] MAC address successfully changed to {updated_mac}")
    else:
        print("[-] MAC address did not change.")

if __name__ == '__main__':
    main()



#! /usr/bin/python

# import subprocess
# import argparse
# import re
#
# from openpyxl.packaging import interface
#
#
# def get_arguments():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-i", "--interface", dest="interface", help="Interface to change MAC address")
#     parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address")
#     options = parser.parse_args()
#     if not options.interface:
#         parser.error("[-] Please specify an interface to change MAC address")
#     elif not options.new_mac:
#         parser.error("[-] Please specify a new MAC address")
#     return options
#
#
# def get_current_mac(interface):
#         ifconfig_result = subprocess.check_output(['ifconfig', interface]).decode("utf-8")
#         mac_changer_search_result = re.search(r"\w\w,\w\w,\w\w,\w\w,\w\w,\w\w",ifconfig_result)
#         if mac_changer_search_result:
#             return mac_changer_search_result.group(0)
#         else:
#             print("[-] Could not find the MAC address")
#             return None
#
# def mac_changer(interface, new_mac):
#     print(f"[+] Changing MAC address for {interface} to {new_mac}")
#
#     subprocess.call(['ifconfig', interface, 'down'])
#     subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
#     subprocess.call(['ifconfig', interface, 'up'])
#
#
#
# def main():
#     options = get_arguments()
#     current_mac = get_current_mac(options.interface)
#
#     if current_mac:
#         print(f"[+] Changing MAC address for {options.interface}")
#     else:
#         print("[-] Could not find the MAC address")
#
#     mac_changer(options.interface, options.new_mac)
#
#     updated_mac = get_current_mac(options.interface)
#     if updated_mac:
#         if updated_mac == options.new_mac:
#             print(f"[+] MAC address successfully changed to {updated_mac}")
#         else:
#             print("[-] MAC address did not change.")
#
#
# if __name__ == '__main__':
#     main()
#



