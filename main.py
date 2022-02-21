#!/usr/bin/env python3

import gi
import os
import locale
import requests
import subprocess
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib, Gio
from locale import gettext as tr

# Tərcümə məlumatları
APPNAME = "pacperro-welcome"
TRANSLATIONS_PATH = "/usr/share/locale"
SYSTEM_LANGUAGE = os.environ.get("LANG")

# Tərcümə funksiyaları
locale.bindtextdomain(APPNAME, TRANSLATIONS_PATH)
locale.textdomain(APPNAME)
locale.setlocale(locale.LC_ALL, SYSTEM_LANGUAGE)

# GTK Builder
builder = Gtk.Builder()
builder.set_translation_domain(APPNAME)
builder.add_from_file("/usr/share/pacperro/proqramlar/pacperro-welcome/pacperro-welcome.glade")

window = builder.get_object("pəncərə")
window.show_all()

class Handler():
    pacperro_version = builder.get_object("pacperro-versiya")
    pacperro_version.set_text("PacPERRO Version: L4")

    def more_information(self, button):
        info = Gtk.Builder()
        info.add_from_file("/usr/share/pacperro/proqramlar/pacperro-welcome/pacperro-welcome.glade")
        info.connect_signals(Handler())
        məlumat = info.get_object("məlumat")
        məlumat.show_all()

    def start(self, button):
        Gtk.main_quit()

    def system_about(self, button):
        os.system("pacperro-about")

builder.connect_signals(Handler())
Gtk.main()