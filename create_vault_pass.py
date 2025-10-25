#!/usr/bin/env python3
import os
import argparse
import getpass

def main():
    parser = argparse.ArgumentParser(description='Generate Ansible Vault password file')
    parser.add_argument('--password', help='Vault password')
    args = parser.parse_args()

    password = args.password if args.password else getpass.getpass('Enter Ansible Vault password: ')
    
    with open('.vault_pass', 'w') as f:
        f.write(password)
    
    os.chmod('.vault_pass', 0o600)

if __name__ == '__main__':
    main()