# -*- coding: utf-8 -*-
'''
Provides PHP namespace insertion in SublimeText

Config summary (see README.md for details):

    # key binding
    { "keys": ["ctrl+alt+n"], "command": "php_namespace" }
²
@author: Alexandre Salomé <alexandre.salome@gmail.com>
@license: MIT (http://www.opensource.org/licenses/mit-license.php)
@since: 2012-03-15
'''

import re, sublime, sublime_plugin, os

class PhpNamespaceCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        # Filename to namespace
        filename = self.view.file_name()

        if (not filename.endswith(".php")):
            sublime.error_message("No .php extension")
            return

        for breakword in [ "src", "tests"]:
            segment = os.sep + breakword + os.sep
            pos = filename.find(segment)
            if (pos != -1):
                break

        if (pos == -1):
            sublime.error_message("No folder " + breakwords.join(" or ") + "in file:\n" + filename)
            return

        className = filename[pos+len(segment):-4].replace("/", "\\")
        namespace = re.sub(r'\\\w+$', '', className)

        sels = self.view.sel()
        for sel in sels:
            self.view.erase(edit, sel)
            self.view.insert(edit, sel.begin(), "namespace " + namespace + ";\n")
