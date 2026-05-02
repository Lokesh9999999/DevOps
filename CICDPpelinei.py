import time
from datetime import datetime

# 🔥 Class name EXACTLY matches your file name logic
class CICDPpelinei:

    def log(self, message):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")

    def build(self):
        self.log("🔨 Building project...")
        time.sleep(1)
        return True

    def test(self):
        self.log("🧪 Running tests...")
        try:
            assert 1 + 1 == 2
            assert "ci/cd".upper() == "CI/CD"
            time.sleep(1)
            return True
        except:
            return False

    def lint(self):
        self.log("🔍 Checking code quality...")
        time.sleep(1)
        return True

    def security_scan(self):
        self.log("🔐 Performing security scan...")
        time.sleep(1)
        return True

    def deploy(self):
        self.log("🚀 Deploying application...")
        time.sleep(1)
        return True

    def rollback(self):
        self.log("↩ Rolling back deployment...")
        time.sleep(1)

    def notify(self, status):
        self.log(f"📢 Pipeline Status: {status}")

    def run(self):
        self.log("🚀 CI/CD Pipeline Started")

        if not self.build():
            self.notify("Build Failed ❌")
            return

        if not self.lint():
            self.notify("Lint Failed ❌")
            return

        if not self.test():
            self.notify("Test Failed ❌")
            return

        if not self.security_scan():
            self.notify("Security Scan Failed ❌")
            return

        if not self.deploy():
            self.rollback()
            self.notify("Deploy Failed ❌ (Rollback Done)")
            return

        self.notify("SUCCESS 🎉")


# 🔥 Main execution (matches class name EXACTLY)
if __name__ == "__main__":
    pipeline = CICDPpelinei()
    pipeline.run()