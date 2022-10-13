import os.path
import subprocess
import sys

import const


def is_installed(name: str):
    result = subprocess.run(
        ["which", name],
        stdout=subprocess.DEVNULL,

        # make sure only errors are printed to console
        stderr=subprocess.STDOUT
    )
    return result.returncode == 0


def setup():
    debugger_name = "mitmproxy"

    if not is_installed("brew"):
        sys.exit("[ERROR] `brew` is not installed!")

    if not is_installed(debugger_name):
        print(f"[INFO] `{debugger_name}` not found. Installing it...")

        result = subprocess.run(["brew", "install", debugger_name])
        if result.returncode != 0:
            sys.exit(f"[ERROR] failed to install {debugger_name}")

    dot_mitmproxy_path = os.path.expanduser("~/.mitmproxy")
    if not os.path.exists(dot_mitmproxy_path):
        os.makedirs(dot_mitmproxy_path, exist_ok=True)

        mitmproxy_config_path = f"{dot_mitmproxy_path}/config.yaml"
        with open(mitmproxy_config_path, "w") as file:
            file.write(f"listen_port: {const.proxy_port}\nweb_port: {const.web_proxy_port}")

        print(f"[INFO] Added configuration file at `{mitmproxy_config_path}`")

    print(f"[INFO] Done. Run `mitmweb` to start debugging")


if __name__ == "__main__":
    setup()
