import platform
from modules.mod_interfaceRunCmd import mod_interfaceRunCmd


class mod_info(mod_interfaceRunCmd):
    def setup_mod(self):
        print(f'Module Setup (mod_info) called successfully!')

    def run_mod(self):
        print(f'Info Module')
        sRet = "System: " + self.get_model()
        sRet += "macOS version: " + self.get_macVer() + "\n"
        sRet += "WiFi: " + "\n" + self.get_wifi()
        sRet += "Battery: " + "\n" + self.get_battery()
        return sRet

    def get_macVer(self):
        return str(platform.mac_ver()[0])

    def get_model(self):
        return self.run_command("sysctl -n hw.model").decode('utf-8')

    def get_wifi(self):
        command = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I" # | grep -w SSID"
        return self.run_command(command).decode('utf-8')#.replace("SSID: ", "").strip()

    def get_battery(self):
        return self.run_command("pmset -g batt").decode("utf-8")# | egrep \"([0-9]+\\%).*\" -o | cut -f1 -d\';\'")