# Project Synopsis: OpenSec Sentinel

### **1. Introduction**

**OpenSec Sentinel** is a modular, home-lab scale Security Operations Center (SOC) and secure infrastructure platform. It is designed to bridge the gap between theoretical cybersecurity concepts and practical implementation by simulating a real-world enterprise security environment. Unlike simple dashboard demonstrations, OpenSec Sentinel is a functional security platform capable of monitoring live systems, detecting active threats, and facilitating incident response workflows.

### **2. Objective**

The primary objective of this project is to solve the visibility and security gap faced by small businesses and home laboratories, which often lack the resources for enterprise-grade tooling. The specific goals are:

* To establish comprehensive visibility into network and system activities.
* To implement effective threat detection using both rule-based engines and Machine Learning (ML).
* To automate incident response actions to mitigate threats in real-time.
* To ensure data integrity and auditability using immutable logging techniques.

### **3. Scope of the Project**

The scope covers the end-to-end engineering of a security platform, moving from bare-metal infrastructure to application-layer security. It involves:

* **Virtualization:** Setting up a Type-1 hypervisor to manage isolated network segments.
* **Security Operations:** Deploying a SIEM (Security Information and Event Management) system for log aggregation.
* **Development:** Creating a secure web application to serve as the protected asset.
* **DevSecOps:** Implementing CI/CD pipelines and Infrastructure as Code (IaC) for cloud deployment.
* **Forensics:** Building a tamper-proof audit trail for compliance verification.

### **4. Modules**

The project is divided into seven distinct architectural layers:

* **Module 1: Infrastructure Layer:** Configuration of the Proxmox hypervisor, internal virtual networks, firewalls (pfSense/iptables), and segmentation of victim/attacker zones.
* **Module 2: Logging & SIEM Layer:** Centralized log aggregation using the ELK Stack or Wazuh. This module handles normalization and correlation of logs from SSH, authentication events, and applications.
* **Module 3: Threat Detection Layer:** Implementation of detection logic, including a custom Malware Detection Model (ML-based) and Sigma-like rules for identifying brute-force attacks and privilege escalation.
* **Module 4: Incident Response Layer:** Development of automated workflows (SOAR-lite) to classify alert severity and trigger actions such as VM isolation or IP blocking.
* **Module 5: Secure Application Layer:** Development of a secure web API utilizing JWT authentication, Role-Based Access Control (RBAC), and secure coding practices to prevent common vulnerabilities.
* **Module 6: Immutable Audit & Integrity Layer:** Creation of a blockchain-inspired audit log using SHA-256 chaining to ensure log integrity and detect tampering.
* **Module 7: Cloud & DevOps Layer:** Extension of the infrastructure to the cloud (AWS/OCI) using Terraform and CI/CD pipelines for automated deployment.

### **5. Software, Hardware, and Tools Used**

**Hardware (Server Node)**

* **Product:** HP EliteDesk 800 G1 SFF
* **Processor:** Intel(R) Core(TM) i5-4570 CPU @ 3.20 GHz
* **RAM:** 4 GB
* **Network:** Intel(R) Ethernet Connection I217-LM
* **Graphics:** Intel(R) HD Graphics 4600

**Software & Tools**

* **Virtualization:** Proxmox Virtual Environment (VE).
* **Operating Systems:** Ubuntu Server (Sentinel Core), Kali Linux (Attacker), Windows/Linux (Targets).
* **SIEM/Logging:** Wazuh or ELK Stack (Elasticsearch, Logstash, Kibana).
* **Development:** Python (ML/Automation), JavaScript/Node.js (Web App).
* **DevOps/Cloud:** Git, Terraform, AWS/OCI.
* **Security:** iptables, pfSense, OpenSSL.

### **6. Expected Outcome**

Upon completion, the project will deliver:

* A fully operational **SOC environment** running on bare-metal hardware.
* A **GitHub repository** containing infrastructure scripts, detection rules, and application source code.
* **Documentation** detailing the architecture, decision-making process, and incident response playbooks.
* Demonstrable **proof-of-concept** scenarios showing a complete attack lifecycle: Log generation → Alert triggering → Automated response.

### **7. Future Enhancements**

* **Scalability:** Upgrading hardware to support a larger cluster of monitored VMs.
* **Advanced ML:** Integrating Deep Learning models for anomaly detection in network traffic.
* **Threat Intel Integration:** Connecting the SIEM to live threat intelligence feeds (e.g., AlienVault OTX) for real-time reputation checking.
* **Full Cloud Hybridization:** Establishing a permanent site-to-site VPN between the home lab and the cloud environment.

### **8. References**

* **Virtualization:** Proxmox VE Documentation.
* **Security Frameworks:** MITRE ATT&CK Matrix, OWASP Top 10.
* **SIEM:** Wazuh / Elastic Stack Official Documentation.
* **Network Security:** *Network Security Assessment* by Chris McNab.
* **Compliance:** NIST Cybersecurity Framework standards.
