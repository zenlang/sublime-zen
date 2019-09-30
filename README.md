Zen Language
============

Syntax highlighting for [Zen](http://zen-lang.org/).

This repository serves both as the grammar for
[github/linguist](https://github.com/github/linguist) (Github's site wide
syntax highlighting) and as a standalone Sublime Text package.

The source of truth is `Zen.YAML-tmLanguage`. This file is read by linguist
directly and used as the source to compile to `Zen.tmLanguage` using
[PackageDev](https://github.com/SublimeText/PackageDev) from within Sublime. Do
not edit `Zen.tmLanguage` directly.

Installation
-----------

Use [Package control](https://packagecontrol.io).

Or add `Zen.tmLanguage` to the packages directory. On OSX This is usually

```
~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
```

But to find the path on your machine go to `Preferences > Browse Packages` from
within Sublime Text.

Local Development
-----------------

Install https://github.com/SublimeText/PackageDev.

Clone or copy this repository to your local Sublime Text folder. e.g.

```
git clone https://github.com/zenlang/sublime-zen-language.git "/Users/$USER/Library/Application Support/Sublime Text 3/Packages/Zen Language"
```

Edit the YAML entry and use the `Convert (YAML, JSON, PList) to...` command
to generate the other entries. Sublime Text will automatically reload the plugin, showing changes in the build system, syntax highlighting, etc.


On Linux, this is located under `~/.config/sublime-text-3/`.

LICENSE
-------

Provided under an MIT License
