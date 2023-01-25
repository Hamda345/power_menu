import os
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Power Menu")
        self.set_border_width(50)
        #Box
        self.box = Gtk.Box(spacing = 10)
        self.add(self.box)
        #Buttons
        self.button1 = Gtk.Button(label="Power Off")
        self.button1.connect("clicked", self.power_off)
        self.box.pack_start(self.button1, True, True, 0)
    
        self.button2 = Gtk.Button(label="Reboot")
        self.button2.connect("clicked", self.reboot)
        self.box.pack_start(self.button2, True, True, 0)
        
        self.button3 = Gtk.Button(label="Suspend")
        self.button3.connect("clicked", self.suspend)
        self.box.pack_start(self.button3, True, True, 0)
 
        self.button4 = Gtk.Button(label="Logout")
        self.button4.connect("clicked", self.log_out)
        self.box.pack_start(self.button4, True, True, 0)

     #user clicks the button
    def power_off(self, widget):
        os.system("shutdown now")
        quit()


    def reboot(self, widget):
        os.system("reboot")
        quit()

    def suspend(self, widget):
        os.system("systemctl suspend")
        quit()

    def log_out(self, widget):
        os.system("pkill -u $USER")
        quit()


window = MainWindow()
# window = Gtk.Window(title="Hello World")
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
