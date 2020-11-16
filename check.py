import hcskr

import discord
from env import CHECK_NAME, CHECK_SCHOOL_NAME, CHECK_SCHOOL_AREA, CHECK_SCHOOL_LEVEL, CHECK_BIRTH


def check():
    return_data = hcskr.selfcheck(CHECK_NAME, CHECK_BIRTH, CHECK_SCHOOL_AREA, CHECK_SCHOOL_NAME, CHECK_SCHOOL_LEVEL)
    if return_data['code'] == 'SUCCESS':
        print("[!] 자가진단 성공")
        print("message: " + return_data['message'])
        discord.success(return_data['message'])
    else:
        print("[!] 자가진단 실패")
        print("message: " + return_data['message'])
        discord.failed(return_data['message'])
