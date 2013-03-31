from ._ import src as s
from ._ import output as o
from ._ import srcExt as se
from ._ import charset

from blog import Post

from os.path import join as j
from os import makedirs as mkdir
from os.path import exists
from os import system

helloworld = u"""
title = "hello World!"  # this is post's title
tags = ["unTaged", ]  # ["tag1", "tag2", ...]
----
## Hello World!
"""

conf = u"""
# config for this blog

# blog's name
name = "Hello golb!"
# blog's description
description = "Make difference"
# blog's author
author = "yourname"
# the directory of your templates(required!)
templates = "templates"
# the count of posts per page,  default: 12
posts_per_page = 12
# other settings ..
# other settings can be touched in template files in this way: blog.mysetting
"""


def init():

    if not exists(".git"):
        exit("Please init here a git repo first.")

    print "mkdir " + Post.sdir + ".."
    mkdir(Post.sdir)
    # write conf.toml
    print "write default config to conf.toml.."
    open("conf.toml", "w").write(conf.encode(charset))
    # write sample posts
    print "write you a sample post.."
    open(
        j(Post.sdir, "helloworld" + se), "w"
    ).write(helloworld.encode(charset))

    print "Fetch templates from github.com.."

    system("git submodule add git://github.com/hit9/golb-templates-classic.git templates")

    print "Init complete"
