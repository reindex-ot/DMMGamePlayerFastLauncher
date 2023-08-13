import os

import customtkinter as ctk
import i18n
from config import PathConfig
from customtkinter import CTk, CTkFrame
from lib.component import TabMenuComponent
from tab.account import AccountTab
from tab.help import HelpTab
from tab.home import HomeTab
from tab.setting import SettingTab
from tab.shortcut import ShortcutTab

i18n.load_path.append("assets/i18n")
i18n.set("locale", "ja")

os.makedirs(PathConfig.ACCOUNT, exist_ok=True)
os.makedirs(PathConfig.SHORTCUT, exist_ok=True)


class App(CTk):
    tab_frame: CTkFrame
    body_frame: CTkFrame

    def __init__(self):
        super().__init__()

        self.title("DMMGamePlayer Fast Launcher")
        self.geometry("900x600")

    def create(self):
        tab = TabMenuComponent(self)
        tab.add(text=i18n.t("app.word.home"), callback=self.home_callback)
        tab.add(text=i18n.t("app.word.shortcut"), callback=self.shortcut_callback)
        tab.add(text=i18n.t("app.word.account"), callback=self.account_callback)
        tab.add(text=i18n.t("app.word.setting"), callback=self.setting_callback)
        tab.add(text=i18n.t("app.word.help"), callback=self.help_callback)
        return self

    def home_callback(self, master: CTkFrame):
        HomeTab(master).create().pack(expand=True, fill=ctk.BOTH)

    def shortcut_callback(self, master: CTkFrame):
        ShortcutTab(master).create().pack(expand=True, fill=ctk.BOTH)

    def account_callback(self, master: CTkFrame):
        AccountTab(master).create().pack(expand=True, fill=ctk.BOTH)

    def setting_callback(self, master):
        SettingTab(master).create().pack(expand=True, fill=ctk.BOTH)

    def help_callback(self, master):
        HelpTab(master).create().pack(expand=True, fill=ctk.BOTH)


# ctk.set_default_color_theme("blue")
# ctk.set_default_color_theme("dark-blue")
ctk.set_default_color_theme("assets/themes/green.json")


# ctk.set_widget_scaling(1.0)
# ctk.set_window_scaling(5.0)
ctk.deactivate_automatic_dpi_awareness()
# ctk.set_appearance_mode("dark")
app = App()
app.create()
app.mainloop()
