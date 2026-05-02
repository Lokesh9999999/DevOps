import json
from datetime import datetime
import random
import os

IMAGE_NAME = "nginx:latest"

# 🔹 Simulated vulnerability data
def generate_vulnerabilities(tool_name):
    severities = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
    vulnerabilities = []

    for i in range(random.randint(2, 5)):
        vuln = {
            "id": f"{tool_name.upper()}-VULN-{random.randint(1000,9999)}",
            "severity": random.choice(severities),
            "description": f"Sample vulnerability detected by {tool_name}"
        }
        vulnerabilities.append(vuln)

    return vulnerabilities


# 🔹 Trivy Scan (Simulated)
def scan_trivy(image):
    print("\n🔍 Running Trivy scan (simulated)...")

    data = {
        "tool": "Trivy",
        "image": image,
        "vulnerabilities": generate_vulnerabilities("trivy")
    }

    with open("trivy_report.json", "w") as f:
        json.dump(data, f, indent=4)

    return "✔ Trivy scan completed (simulated)"


# 🔹 Snyk Scan (Simulated)
def scan_snyk():
    print("\n🔍 Running Snyk scan (simulated)...")

    data = {
        "tool": "Snyk",
        "project": "Demo Project",
        "vulnerabilities": generate_vulnerabilities("snyk")
    }

    with open("snyk_report.json", "w") as f:
        json.dump(data, f, indent=4)

    return "✔ Snyk scan completed (simulated)"


# 🔹 Clair Scan (Simulated)
def scan_clair(image):
    print("\n🔍 Running Clair scan (simulated)...")

    data = {
        "tool": "Clair",
        "image": image,
        "vulnerabilities": generate_vulnerabilities("clair")
    }

    with open("clair_report.json", "w") as f:
        json.dump(data, f, indent=4)

    return "✔ Clair scan completed (simulated)"


# 🔹 Generate Summary Report
def generate_summary(results):
    print("\n📄 Generating summary report...")

    with open("summary_report.txt", "w") as f:
        f.write("DEVOPS SECURITY REPORT\n")
        f.write("========================\n")
        f.write(f"Scan Time: {datetime.now()}\n\n")

        for tool, result in results.items():
            f.write(f"{tool}: {result}\n")

        f.write("\nGenerated Files:\n")
        files = ["trivy_report.json", "snyk_report.json", "clair_report.json"]

        for file in files:
            if os.path.exists(file):
                f.write(f"✔ {file}\n")
            else:
                f.write(f"❌ {file} missing\n")

    print("✔ summary_report.txt created")


# 🔹 Main
if __name__ == "__main__":
    print("🚀 Starting DevOps Security Scanning (Simulation)...\n")

    results = {}

    results["Trivy"] = scan_trivy(IMAGE_NAME)
    results["Snyk"] = scan_snyk()
    results["Clair"] = scan_clair(IMAGE_NAME)

    generate_summary(results)

    print("\n✅ All scans completed (simulated)!")