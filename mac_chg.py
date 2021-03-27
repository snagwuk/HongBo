import subprocess as sub
import re


def change_mac(interface, new_mac):
    # Checking if the new MAC Address has a length of 17 or not. If not print an error and quit, else change the MAC Address
    if len(new_mac) != 17:
        print('[-] Please enter a valid MAC Address')
        quit()

    print('\n[+] Changing the MAC Address to', new_mac)
    sub.call(['sudo', 'ifconfig', interface, 'down'])
    sub.call(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])
    sub.call(['sudo', 'ifconfig', interface, 'up'])


def get_current_mac(interface):
    output = sub.check_output(['ifconfig', interface], universal_newlines=True)
    search_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output)
    if search_mac:
        return search_mac.group(0)
    else:
        print('[-] Could not read the MAC Address')


xx = 'eth0'
xnew_mac = '18-B7-9E-5F-25-F6'
ORD = '00-0C-9A-DE-42-B0'
prev_mac = get_current_mac(xx)
print('\n[+] MAC Address before change -> {}'.format(prev_mac))

change_mac(xx, xnew_mac)

changed_mac = get_current_mac(xx)
print('\n[+] MAC Address after change -> {}'.format(changed_mac))

# Checking if the current MAC is same as the what the user intended to be
# If not then display an error
# Else display a message that says MAC Changed successfully
if changed_mac == xnew_mac:
    print('\n[+] MAC Address was successfully changed from {} to {}'.format(prev_mac, changed_mac))
else:
    print('\n[-] Could not change the MAC Address')
