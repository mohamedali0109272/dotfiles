# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

###3from typing import List  # noqa: F401

#####from libqtile import bar, layout, widget
#####from libqtile.config import Click, Drag, Group, Key, Screen
#####from libqtile.lazy import lazy
#####from libqtile.utils import guess_terminal
#####from libqtile.config import Group, Match
#####from libqtile.dgroups import simple_key_binder


import os
import re
import socket
import subprocess
from libqtile.config import Drag, Key, Screen, Group, Drag, Click, Rule
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.widget import Spacer


#mod4 or mod = super key
mod = "mod4"
mod1 = "mod1"
mod2 = "control"
mod3 = "shift"
home = os.path.expanduser('~')
terminal = "st"

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

#############################################
############ SHORTCUTS ######################
#############################################


keys = [
#    Key([mod], "x", lazy.spawn("poweroff")),
    Key([mod, "shift"], "t", lazy.spawn("rofi -show drun")),
    Key([mod], "d", lazy.spawn("./git/polybar-themes/simple/shades/scripts/launcher.sh")),
    Key([mod], "x", lazy.spawn("./git/polybar-themes/simple/shapes/scripts/powermenu.sh")),
    #Key([mod, "shift"], "s", lazy.spawn("./git/polybar-themes/simple/scripts/color-switch.sh")),
    Key([mod, "shift"], "d", lazy.spawn("rofi -show window")),
    #Key([mod], "d", lazy.spawn("dmenu_run -h 25 -b -p 'Run: '")),
    

##################################################
################# MEDIA CONTROLS #################
##################################################

# INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 5")),



    # Switch between windows in current stack pane
###################################################    
################  SWITCH LAYOUT ###################
###################################################

# TOGGLE FLOATING LAYOUT
    Key([mod, "control"], "a", lazy.window.toggle_floating()),


    # CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "l", lazy.layout.down()),
    Key([mod], "o", lazy.layout.left()),
    Key([mod], "p", lazy.layout.right()),
    Key([mod], "j",lazy.layout.grow(), lazy.layout.increase_nmaster()),
    Key([mod], "m", lazy.layout.shrink(), lazy.layout.decrease_nmaster()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),
    Key([mod], "space", lazy.layout.next()),
    Key([mod, "shift"], "space", lazy.layout.rotate()),
    
#########################################
############### BSPWM ###################
#########################################


    Key([mod], "Down", lazy.layout.down()),
Key([mod], "Up", lazy.layout.up()),
Key([mod], "Left", lazy.layout.left()),
Key([mod], "Right", lazy.layout.right()),
Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
Key([mod, "shift"], "Left", lazy.layout.shuffle_left()),
Key([mod, "shift"], "Right", lazy.layout.shuffle_right()),
Key([mod, "mod1"], "Down", lazy.layout.flip_down()),
Key([mod, "mod1"], "Up", lazy.layout.flip_up()),
Key([mod, "mod1"], "Left", lazy.layout.flip_left()),
Key([mod, "mod1"], "Right", lazy.layout.flip_right()),
Key([mod, "control"], "Down", lazy.layout.grow_down()),
Key([mod, "control"], "Up", lazy.layout.grow_up()),
Key([mod, "control"], "Left", lazy.layout.grow_left()),
Key([mod, "control"], "Right", lazy.layout.grow_right()),
Key([mod, "shift"], "n", lazy.layout.normalize()),
Key([mod], "z", lazy.layout.toggle_split()),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod, "shift"], "q", lazy.shutdown()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod], "r", lazy.spawncmd()),
    Key([mod, "shift"], "x", lazy.spawn("poweroff")),
##############################################
############## SCREENSHOTS ###################
##############################################

    Key([], "Print", lazy.spawn("scrot 'screenshot_%Y%m%d_%H%M%S.png' -e 'mkdir -p ~/Pictures/screenshots && mv $f ~/Pictures/screenshots && xclip -selection clipboard -t image/png -i ~/Pictures/screenshots/`ls -1 -t ~/Pictures/screenshots | head -1`'")),

    Key(["shift"], "Print", lazy.spawn("scrot -s 'screenshot_%Y%m%d_%H%M%S.png' -e 'mkdir -p ~/Pictures/screenshots && mv $f ~/Pictures/screenshots && xclip -selection clipboard -t image/png -i ~/Pictures/screenshots/`ls -1 -t ~/Pictures/screenshots | head -1`'")),
#####################3#########################
############## APPLICATIONS ###################
###############################################
    
    Key([mod, "shift"], "h", lazy.spawn("kitty -e htop")),
    Key([mod], "t", lazy.spawn("alacritty")),
    Key([mod, "shift"], "Return", lazy.spawn("kitty -e ranger")),
    Key([mod, "shift"], "i", lazy.spawn("betterlockscreen -l blur")),
    Key([mod], "i", lazy.spawn("i3lock -c 000000")),
    Key([mod], "Return", lazy.spawn(terminal)),  
    Key([mod1, mod2], "v", lazy.spawn("vivaldi")),
    Key([mod], "v", lazy.spawn("pavucontrol")),
    Key([mod], "w", lazy.spawn("emacs")),
    Key([mod1, "control"], "n", lazy.spawn("nautilus")),
    Key([mod, "shift"], "p", lazy.spawn("qutebrowser")),
    ]
groups = []
groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

group_labels = ["WWW", "WEB", "TERM", "MP4", "TXT", "FILES", "SYS", "EDIT", "MEET", "MUS",]

group_layouts = ["monadtall", "monadtall", "monadtall", "max", "monadtall", "monadtall", "monadtall", "monadtall"
        , "monadtall", "monadtall",]

for i in range(len(group_names)):
        groups.append(
        Group(
        name=group_names[i],
        layout=group_layouts[i].lower(),
        label=group_labels[i],
    ))

for i in groups:
        keys.extend([

# CHANGE WORKSPACES
    Key([mod], i.name, lazy.group[i.name].toscreen()),
    # Key([mod], "Tab", lazy.screen.next_group()),
    Key(["mod1"], "Tab", lazy.screen.next_group()),
    Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),


    Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
        ])
#LAYOUTS
layouts = [
    #layout.MonadWide(margin=7, border_width=4, border_focus="ffffff", border_normal="#4c566a" ),
    layout.MonadTall(margin=10, border_width=4, border_focus="#03ba89", border_normal="#3e4554" ),
    layout.Max()
    #layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    #layout.Bsp(margin=7, border_width=4, border_focus="ffffff", border_normal="4c566a" ),
    # layout.Columns(),
    #layout.Matrix()
    #layout.MonadWide(margin=15, border_width=4, border_focus="ffffff"),
    #layout.RatioTile(margin=7)
     layout.Tile(margin=7)
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

colors =  [["#706d6f", "#706d6d"], # color 0
           ["#080217", "#080217"], # color 1
           ["#8c8c8c", "#8c8c8c"], # color 2
           ["#ff5555", "#ff5555"], # color 3
           ["#7990b4", "#7990b4"], # color 4
           ["#ffffff", "#ffffff"], # color 5
           #["#adc2e0", "#adc2e0"], # color 6
           ["#89b8fd", "#89b8fd",],
           ["#ff79c6", "#ff79c6"], # color 7
           ["#d5b5f3", "#d5b5f3"], # color 8
           ["#0ee9af", "#0ee9af"]] # color 9


        


widget_defaults = dict(
    font='andale mono',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper='/home/trogdor/Pictures/wallpapers/minim.jpg',
        wallpaper_mode='fill',
        top=bar.Bar(
            [
             widget.Sep(
                 background = colors[1],
                 padding = 5,
                 linewidth = 0,
                 ),
                 widget.GroupBox(
                    font = "trebuchet ms",
                    #font = "inconsolata for powerline",
                    #font = "comic sans ms",
                    #font = "hack",
                    fontsize = 11,
                    margin_y = 3,
                    margin_x = 2,
                    padding_y = 5,
                    padding_x = 4,
                    borderwidth = 3,
                    active = colors[3],
                    inactive = colors[4],
                    rounded = True,
                    highlight_color = colors[1],
                    highlight_method = "block",
                    this_current_screen_border = colors[8],
                    this_screen_border = colors [6],
                    other_current_screen_border = colors[1],
                    other_screen_border = colors[1],
                    foreground = colors[8],
                    background = colors[1]),

                widget.Sep(
                linewidth = 4,
                padding = 10,
                foreground = colors[5],
                background = colors[1]),

                widget.Prompt(
                    background=colors[8],
                    foreground=colors[1],
                    font="novamono for powerline",
                    fontsize = 14,
                    ),
                
                widget.Spacer(
                        background = colors[1],
                        ),
                widget.Chord(
                            chords_colors={
                            'launch': ("#ff0000", "#ffffff"),
                        },
                            name_transform=lambda name: name.upper()),
                widget.TextBox(
                       text = '',
                       background = colors[1],
                       foreground = colors[8],
                       padding = 0,
                       fontsize = 60
                       ),
                
                widget.Memory(
                        background=colors[8],
                        foreground=colors[1],
                        font="novamono for powerline",
                        fontsize=14,
                        format='{MemUsed: .0f} MB',
                        ),
                widget.TextBox(
                       text = '',
                       background = colors[8],
                       foreground = colors[7],
                       padding = 0,
                       fontsize = 60
                       ),
                widget.CurrentLayout(
                font = "anonymous pro for powerline bold",
                fontsize = 15,
                foreground = colors[1],
                background = colors[7]
                ),

                widget.TextBox(
                       text = '',
                       background = colors[7],
                       foreground = colors[3],
                       padding = 0,
                       fontsize = 60
                       ),
                widget.Systray(
                        background=colors[3],
                        icons_size=20,
                        padding=4
                        ),
                widget.Sep(linewidth = 3,
                           padding = 10,
                           foreground = colors[5],
                           background=colors[3],
                           ),
                widget.Volume(
                    background = colors[1],
                    foreground = colors[5],
                    font="comic sans ms bold",
                    fontsize = 12,
                    ),

                widget.Sep(
                    linewidth = 3,
                    padding = 10,
                    foreground = colors[5],
                    background = colors[3],
                ),
                widget.TextBox(
                       text = '',
                       background = colors[3],
                       foreground = colors[7],
                       padding = 0,
                       fontsize = 60
                       ),
                widget.TextBox(
                    text=' ',
                    fontsize='16',
                    background=colors[7],
                    foreground=colors[1],
                    ),
                widget.Battery(
                    background=colors[7],
                    foreground=colors[1],
                    charge_char='↑',
                    discharge_char='↓',
                    fontsize=13,
                    update_interval=1,
                    format='{percent:2.0%}'
                ),
                widget.TextBox(
                       text = '',
                       background = colors[7],
                       foreground = colors[3],
                       padding = 0,
                       fontsize = 60
                       ),
                widget.Clock(
                    font = "novamono for powerline bold",
                    foreground = colors[1],
                    background = colors[3],
                    fontsize = 14,
                    format='%d-%m-%Y %a %I:%M %p'),
                widget.Sep(
                    padding = 6,
                    linewidth = 0,
                    background = colors[3],
                    foreground = colors[5],
                    ),
                
                ],
            31,
            background='#282a36',
            margin=[10,10,0,10],
            opacity=.75,
            ),
    ),
    ]
#############################################
############# AUTOSTART #####################
#############################################
@hook.subscribe.startup_once
def autostart():
    processes = [
        ['nm-applet'],
        ['blueman-applet'],
        ['picom']
    ]

    for p in processes:
        subprocess.Popen(p)


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
    {'wmclass': 'Alacritty'},
    {'wmclass': 'About Tor - Tor Browser'},
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"
