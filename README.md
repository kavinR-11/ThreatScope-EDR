# ThreatScope-EDR

ThreatScope-EDR is a Python-based Endpoint Detection and Response (EDR) prototype designed to monitor system processes, detect suspicious behavior, and generate incident response reports.

## Overview

ThreatScope monitors system activity in real time and identifies potential threats using behavioral detection techniques. It focuses on detecting abnormal CPU usage and suspicious execution paths commonly associated with malware or unauthorized activity.

## Features

- Real-time process monitoring
- High CPU usage detection
- Suspicious process location detection
- Automated incident report generation
- Lightweight and dependency-minimal design

## Architecture

ThreatScope consists of modular detection components:

- Process Monitor – Detects abnormal CPU usage and suspicious execution paths
- Reporter Module – Generates forensic incident reports in JSON format
- Configuration System – Customizable detection thresholds

## How to Run

## Output

Incident reports are generated in:



## Purpose

This project demonstrates core Endpoint Detection and Response (EDR) concepts, including:

- Behavioral threat detection
- Endpoint monitoring
- Incident response evidence collection

## Author

Kavin R
