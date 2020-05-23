"""
    3. Build an application that can be used to block certain websites
"""

hosts_path = "/etc/hosts"
redirect = "127.0.0.1"

opt = input("1.add\n2.remove\n")

if opt == '1':
    with open(hosts_path, 'r+') as file:
        content = file.read()
        website = input("Enter website to block ")
        if website in content:
            pass
        else:
            file.write(redirect + " " + website + "\n")
elif opt == '2':
    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        website = input("Enter a website to unblock ")
        if not any(website in line for line in content):
            file.write(line)

        file.truncate()
else:
    print("Not an Option")
