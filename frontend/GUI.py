from tkinter import *
from backend.ps_commands import *


class WindowsAppRemover:

    def __init__(self):
        self.gui = Tk()

    def advanced_window(self):
        ad_window = Toplevel(self.gui)
        ad_window.focus()
        ad_window.title("Advanced")
        ad_window.configure(bg="white", pady=5)

        remove_groups = Label(ad_window, text="Remove Apps by Groups", background="white", foreground="blue",
                              font="bold")
        remove_groups.grid(row=0, column=0, columnspan=2, pady=5, padx=2)

        remove_utility_apps = Button(ad_window, text="Utility Apps", width=17, bg="blue", fg="white")
        remove_utility_apps.configure(command=remove_utilities)
        remove_utility_apps.grid(row=1, column=0, columnspan=2, pady=2, padx=2)

        remove_entertainment_apps = Button(ad_window, text="Entertainment Apps", width=17, bg="blue", fg="white")
        remove_entertainment_apps.configure(command=remove_entertainment)
        remove_entertainment_apps.grid(row=2, column=0, columnspan=2, pady=2, padx=2)

        remove_all_apps = Button(ad_window, text="All Apps", width=17, bg="blue", fg="white")
        remove_all_apps.configure(command=remove_all_applications)
        remove_all_apps.grid(row=3, column=0, columnspan=2, pady=2, padx=2)

    def run_program(self):
        self.gui.title("WAR")
        self.gui.minsize(width=240, height=700)
        self.gui.maxsize(width=240, height=700)
        self.gui.configure(bg="white", pady=5, padx=5)

        grouped_apps = Label(self.gui, text="Windows App Remover", background="white", foreground="blue", font="bold")
        grouped_apps.grid(row=0, column=0, pady=13, padx=2)

        remove_3dbuilder = Button(self.gui, text="3dbuilder", width=17, bg="blue", fg="white")
        remove_3dbuilder.configure(command=lambda: remove_app(all_applications["3dbuilder"]))
        remove_3dbuilder.grid(row=1, column=0, pady=2, padx=2)

        remove_windows_alarm = Button(self.gui, text="Windows Alarms", width=17, bg="blue", fg="white")
        remove_windows_alarm.configure(
            command=lambda: remove_app(all_applications["Alarm"]))
        remove_windows_alarm.grid(row=2, column=0, pady=2, padx=2)

        remove_calculator = Button(self.gui, text="Calculator", width=17, bg="blue", fg="white")
        remove_calculator.configure(command=lambda: remove_app(all_applications["Calculator"]))
        remove_calculator.grid(row=3, column=0, pady=2, padx=2)

        remove_skype = Button(self.gui, text="Skype", width=17, bg="blue", fg="white")
        remove_skype.configure(command=lambda: remove_app(all_applications["Skype"]))
        remove_skype.grid(row=4, column=0, pady=2, padx=2)

        remove_get_started = Button(self.gui, text="Get Started", width=17, bg="blue", fg="white")
        remove_get_started.configure(command=lambda: remove_app(all_applications["Get Started"]))
        remove_get_started.grid(row=5, column=0, pady=2, padx=2)

        remove_zune_music = Button(self.gui, text="Zune Music", width=17, bg="blue", fg="white")
        remove_zune_music.configure(command=lambda: remove_app(all_applications["Zune Music"]))
        remove_zune_music.grid(row=6, column=0, pady=2, padx=2)

        remove_windows_maps = Button(self.gui, text="Windows Maps", width=17, bg="blue", fg="white")
        remove_windows_maps.configure(command=lambda: remove_app(all_applications["Maps"]))
        remove_windows_maps.grid(row=7, column=0, pady=2, padx=2)

        remove_solitaire = Button(self.gui, text="Solitaire", width=17, bg="blue", fg="white")
        remove_solitaire.configure(
            command=lambda: remove_app(all_applications["Solitaire"]))
        remove_solitaire.grid(row=8, column=0, pady=2, padx=2)

        remove_bing_finance = Button(self.gui, text="Bing Finance", width=17, bg="blue", fg="white")
        remove_bing_finance.configure(command=lambda: remove_app(all_applications["Finance"]))
        remove_bing_finance.grid(row=9, column=0, pady=2, padx=2)

        remove_zune_video = Button(self.gui, text="Zune Video", width=17, bg="blue", fg="white")
        remove_zune_video.configure(command=lambda: remove_app(all_applications["Zune Video"]))
        remove_zune_video.grid(row=10, column=0, pady=2, padx=2)

        remove_bing_news = Button(self.gui, text="Bing News", width=17, bg="blue", fg="white")
        remove_bing_news.configure(command=lambda: remove_app(all_applications["Bing News"]))
        remove_bing_news.grid(row=11, column=0, pady=2, padx=2)

        remove_one_note = Button(self.gui, text="OneNote", width=17, bg="blue", fg="white")
        remove_one_note.configure(command=lambda: remove_app(all_applications["OneNote"]))
        remove_one_note.grid(row=12, column=0, pady=2, padx=2)

        remove_windows_phone = Button(self.gui, text="Windows Phone", width=17, bg="blue", fg="white")
        remove_windows_phone.configure(
            command=lambda: remove_app(all_applications["Windows Phone"]))
        remove_windows_phone.grid(row=13, column=0, pady=2, padx=2)

        remove_bing_sports = Button(self.gui, text="Bing Sports", width=17, bg="blue", fg="white")
        remove_bing_sports.configure(command=lambda: remove_app(all_applications["Bing Sports"]))
        remove_bing_sports.grid(row=14, column=0, pady=2, padx=2)

        remove_voice_recorder = Button(self.gui, text="Voice Recorder", width=17, bg="blue", fg="white")
        remove_voice_recorder.configure(
            command=lambda: remove_app(all_applications["Voice Recorder"]))
        remove_voice_recorder.grid(row=15, column=0, pady=2, padx=2)

        remove_bing_weather = Button(self.gui, text="Bing Weather", width=17, bg="blue", fg="white")
        remove_bing_weather.configure(command=lambda: remove_app(all_applications["Bing Weather"]))
        remove_bing_weather.grid(row=16, column=0, pady=2, padx=2)

        remove_xbox = Button(self.gui, text="Xbox App", width=17, bg="blue", fg="white")
        remove_xbox.configure(command=lambda: remove_app(all_applications["Xbox"]))
        remove_xbox.grid(row=17, column=0, pady=2, padx=2)

        remove_feedback_hub = Button(self.gui, text="Feedback Hub", width=17, bg="blue", fg="white")
        remove_feedback_hub.configure(command=lambda: remove_app(all_applications["Feedback Hub"]))
        remove_feedback_hub.grid(row=18, column=0, pady=2, padx=2)

        remove_wallet = Button(self.gui, text="Windows Wallet", width=17, bg="blue", fg="white")
        remove_wallet.configure(command=lambda: remove_app(all_applications["Wallet"]))
        remove_wallet.grid(row=19, column=0, pady=2, padx=2)

        remove_sway = Button(self.gui, text="Sway", width=17, bg="blue", fg="white")
        remove_sway.configure(command=lambda: remove_app(all_applications["Sway"]))
        remove_sway.grid(row=20, column=0, pady=2, padx=2)

        advanced_button = Button(self.gui, text="Advanced", bg="blue", fg="white")
        advanced_button.configure(command=self.advanced_window)
        advanced_button.grid(row=21, column=0, pady=10)

        self.gui.mainloop()


if __name__ == "__main__":
    WindowsAppRemover.run_program(WindowsAppRemover())
