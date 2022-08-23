import os
import subprocess

import sublime
import sublime_plugin

def plugin_loaded():
    """
    Hook that is called by Sublime when plugin is loaded.
    """
    pass


def plugin_unloaded():
    """
    Hook that is called by Sublime when plugin is unloaded.
    """
    for key in list(globals().keys()):
        if "imagepaste" in key.lower():
            del globals()[key]

class ImagePasteCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        def is_done(input_string):
            settings = sublime.load_settings("image-paste.sublime-settings")
            variables = self.view.window().extract_variables()
            name = input_string
            destination_folder = sublime.expand_variables(settings.get("folder"), variables) + "/screenshots/"
            
            if not os.path.isdir(destination_folder) or not os.path.exists(destination_folder):
                print(
                    "Could not paste image: "
                    "destination is not a folder: {}".format(destination_folder)
                )
                os.mkdir(destination_folder)

            destination = destination_folder + name + ".png"
            linux_cmd = "xclip -selection clipboard -t image/png -o > %s" % str(destination)
            linux_cmd_1 = "pngpaste %s" % str(destination)
            
            file = "![](./screenshots/" + name + ".png)"
            text_to_insert = file
         
            os.system(linux_cmd)
            os.system(linux_cmd_1)

            self.view.run_command("insert", {"characters": text_to_insert})

        def on_done(input_string):
            is_done(input_string)

        window = self.view.window()
        window.show_input_panel("Text to Insert:", "imagename",
                                on_done, None, None)

