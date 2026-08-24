from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.utils import platform

if platform == 'android':
    from jnius import autoclass, cast
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Context = autoclass('android.content.Context')
    Intent = autoclass('android.content.Intent')
    ComponentName = autoclass('android.content.ComponentName')
    DevicePolicyManager = autoclass('android.app.admin.DevicePolicyManager')

class AutoLockApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.info_label = Label(text="Auto-Lock Timer (Python)", font_size='20sp')
        self.layout.add_widget(self.info_label)

        self.admin_btn = Button(text="1. Grant Admin Permission", size_hint=(1, 0.2))
        self.admin_btn.bind(on_press=self.request_admin)
        self.layout.add_widget(self.admin_btn)

        self.seconds_input = TextInput(text="10", multiline=False, input_filter='int', size_hint=(1, 0.2))
        self.layout.add_widget(self.seconds_input)

        self.start_btn = Button(text="2. Start Lock Countdown", size_hint=(1, 0.2))
        self.start_btn.bind(on_press=self.start_countdown)
        self.layout.add_widget(self.start_btn)

        if platform == 'android':
            self.activity = PythonActivity.mActivity
            self.dpm = cast(DevicePolicyManager, self.activity.getSystemService(Context.DEVICE_POLICY_SERVICE))
            self.admin_component = ComponentName(self.activity, "org.kivy.android.PythonDeviceAdminReceiver")

        return self.layout

    def request_admin(self, instance):
        if platform == 'android':
            if not self.dpm.isAdminActive(self.admin_component):
                intent = Intent(DevicePolicyManager.ACTION_ADD_DEVICE_ADMIN)
                intent.putExtra(DevicePolicyManager.EXTRA_DEVICE_ADMIN, self.admin_component)
                intent.putExtra(DevicePolicyManager.EXTRA_ADD_EXPLANATION, "Required to lock screen automatically.")
                self.activity.startActivity(intent)
            else:
                self.info_label.text = "Admin permission already active!"
        else:
            self.info_label.text = "[Desktop Test Mode] Admin requested."

    def start_countdown(self, instance):
        try:
            delay = int(self.seconds_input.text)
            self.info_label.text = f"Locking in {delay} seconds..."
            Clock.schedule_once(self.trigger_lock, delay)
        except ValueError:
            self.info_label.text = "Enter valid seconds!"

    def trigger_lock(self, dt):
        if platform == 'android':
            if self.dpm.isAdminActive(self.admin_component):
                self.dpm.lockNow()
                self.info_label.text = "Screen Locked!"
            else:
                self.info_label.text = "Error: Grant Admin First!"
        else:
            self.info_label.text = "[Desktop Test Mode] Timer ended - Screen Lock Triggered!"

if __name__ == '__main__':
    AutoLockApp().run()