













define config.name = _("Friends in Need")





define gui.show_name = False








define gui.about = _p("""
""")






define build.name = "FriendsinNeed"







define config.has_sound = True
define config.has_music = True
define config.has_voice = True
























define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 0





default preferences.afm_time = 15
















define config.save_directory = "FriendsinNeed2-1641753492"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/.png', 'images')
    build.classify('game/.jpg', 'images')
    build.classify('game/**.webp', 'images')
    build.archive('game/**.jpg', 'images')
    build.archive("images", "all")
    build.classify("game/.rpy", "scripts")
    build.classify("game/.rpyc", "scripts")
    build.archive("scripts", "all")
    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")
    build.classify("game/**.jpeg", "images")









    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
