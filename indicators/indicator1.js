#!/usr/bin/gjs

imports.gi.versions.Gtk = '3.0'
imports.gi.versions.AppIndicator3 = '0.1'


const Gtk = imports.gi.Gtk
const AppIndicator3 = imports.gi.AppIndicator3

class IndicatorApp {
  constructor() {
    print("hi")
    this.indicator = new AppIndicator3.Indicator()
    //this.indicator.set_status()

  }
}

let app = new IndicatorApp()


