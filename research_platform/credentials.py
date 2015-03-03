#!/usr/bin/env python
import os

def get_nova_creds():
    d = {}
    d['username'] = "Cloud_user_name"
    d['api_key'] = "Cloud_password" 
    d['auth_url'] = "Cloud_auth_url"
    d['project_id'] = "Cloud_project_id"
    d['region_name'] = "Cloud_region_name"
    return d
