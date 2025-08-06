#! /usr/bin/env python

import npyscreen
import requests

servers = {
    "ntfy.sh": "https://ntfy.sh",
    "chaco": "https://ntfy.chaco-vibes.ts.net",
    "custom": "https://my.custom.ntfy.server"
}

class NotifyForm(npyscreen.ActionForm):
    def create(self):
        self.server_choices = self.add(npyscreen.TitleMultiSelect, max_height=4,
                                       name="Select Servers", values=list(servers.keys()))
        self.topic = self.add(npyscreen.TitleText, name="Topic:")
        self.title = self.add(npyscreen.TitleText, name="Title (optional):")
        self.message = self.add(npyscreen.TitleText, name="Message:")

    def on_ok(self):
        selected = [list(servers.values())[i] for i in self.server_choices.value]
        headers = {}
        if self.title.value:
            headers["X-Title"] = self.title.value
        for url in selected:
            full_url = f"{url}/{self.topic.value}"
            try:
                r = requests.post(full_url, data=self.message.value.encode("utf-8"), headers=headers)
                npyscreen.notify_confirm(f"Sent to {url} - Status {r.status_code}", title="Success")
            except Exception as e:
                npyscreen.notify_confirm(f"Error sending to {url}: {e}", title="Error")

    def on_cancel(self):
        npyscreen.notify_confirm("Cancelled.", title="Bye")
        self.parentApp.setNextForm(None)

class NTFYApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', NotifyForm, name="ntfytui - Terminal Notifier")

if __name__ == "__main__":
    NTFYApp().run()

