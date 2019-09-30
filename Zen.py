import sublime
import sublime_plugin

settings = sublime.load_settings('Zig.sublime-settings')


def get_setting(view, opt, default):
    return view.settings().get(opt, settings.get(opt, default))


class Zig(sublime_plugin.EventListener):
    def on_post_save_async(self, view):
        sel = view.sel()[0]
        region = view.word(sel)
        scope = view.scope_name(region.b)
        if scope.find('source.zen') != -1:
            should_fmt = get_setting(view, 'zen.fmt.on_save', True)
            should_build = get_setting(view, 'zen.build.on_save', False)

            if (should_fmt and not should_build):
                mode = get_setting(view, 'zen.fmt.mode', 'File').title()
                view.window().run_command('build', {'variant': 'Format ' + mode})
            elif (should_build and not should_fmt):
                view.window().run_command('build')
