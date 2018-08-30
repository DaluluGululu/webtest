#!usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import methods.readdb as mrd
import time

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        usernames=mrd.select_columns(table="users",column="username")
        one_user=usernames[0][0]
        self.render("index.html",user=one_user)

    def post(self):
        username=self.get_argument("username")
        password=self.get_argument("password")
        user_infos=mrd.select_table(table="users",column="*",condition="username",value=username)
        if user_infos:
            db_pwd=user_infos[0][2]
            if db_pwd==password:
                self.set_cookie(username,db_pwd)
                self.write(username)#delete "welcome you,otherwise the entire string will be treated as the username"
            else:
                self.write("your password was not right.")
        else:
            self.write("There is no this user.")
