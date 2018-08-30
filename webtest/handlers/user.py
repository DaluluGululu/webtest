#!usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import methods.readdb as mrd

class UserHandler(tornado.web.RequestHandler):
    def get(self):
        username=self.get_argument("user")
        print username
        user_infos=mrd.select_table(table="users",column="*",condition="username",value=username)
        print user_infos
        if user_infos:
            self.render("user.html",users=user_infos)
