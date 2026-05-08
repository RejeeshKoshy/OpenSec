# OpenSec
An attempt to create open sourced enterpirised grade security for SMBs using wazuh and IForest.

# The Project: **OpenSec Sentinel**

*A Modular Home-Lab SOC + Secure Infrastructure Platform*

## What Problem Does It Solve?

Small businesses and home labs:

* don’t know what’s happening on their systems
* don’t have SOC visibility
* can’t afford enterprise security tooling
* have poor logging, alerting, and response

**OpenSec Sentinel** gives:

* visibility
* detection
* response
* auditability
* learning

---

## Architecture (What You’ll Build)

### Infrastructure Layer (Systems + Networking)

* Proxmox VE as hypervisor
* Multiple VMs:

  * Linux server
  * Windows client
  * Attacker VM (Kali)
* Internal virtual network
* Firewall rules (pfSense / iptables)

### Logging & SIEM Layer

* Central log server (ELK / OpenSearch / Wazuh)
* Log sources:

  * SSH logs
  * auth logs
  * file access logs
  * application logs
* Normalization & correlation rules

### Threat Detection Layer

* Malware detection model (your ML strength)
* Rule-based detection (Sigma-like rules)
* Brute-force detection
* Privilege escalation detection

### Incident Response Layer

* Alert severity classification
* Automated actions:

  * isolate VM
  * block IP
  * disable account
* Incident timeline generation

### Secure Application Layer

* Secure web app / API
* JWT-based auth
* Role-based access
* Secure file uploads
* Audit logging

### Immutable Audit & Integrity Layer

* Blockchain-inspired audit log
* SHA-256 chained records
* Tamper detection
* Integrity verification tool

### Cloud & DevOps Layer

* Deploy components to cloud (AWS / OCI)
* CI/CD pipeline
* Infrastructure as Code (Terraform-lite)
* Secrets management
