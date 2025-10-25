# Alf.io Ansible Deployment

This repository contains Ansible playbooks for deploying Alf.io, a self-hosted ticketing system.

## Prerequisites

- Ansible 2.9 or higher
- Python 3.x
- Target servers running Ubuntu 20.04 or higher

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/akumakonticketsrepo.git
   cd akumakonticketsrepo
   ```

2. Create vault password file:
   ```bash
   python3 create_vault_pass.py
   ```

3. Edit the inventory files in `inventory/` to match your environment:
   - `inventory/production` for production environment
   - `inventory/development` for development environment

4. Update the group variables in `group_vars/all.yml` and encrypt sensitive data:
   ```bash
   ansible-vault edit group_vars/all.vault.yml
   ```

## Deployment

To deploy to production:
```bash
ansible-playbook -i inventory/production site.yml
```

To deploy to development:
```bash
ansible-playbook -i inventory/development site.yml
```

## Accessing Credentials

After deployment, credentials will be displayed on screen. Make sure to save them securely.

## Services

- Alf.io Web Interface: https://your-domain
- Admin Interface: https://your-domain/admin
- Database: PostgreSQL on the specified database server

## Maintenance

- SSL certificates will auto-renew via Certbot
- Database backups should be configured separately
- Monitor the services using your preferred monitoring solution

## Security

- All passwords are stored in encrypted vault files
- HTTPS is enforced for all connections
- Database access is restricted to the application network