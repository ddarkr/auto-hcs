from discord_webhook import DiscordWebhook, DiscordEmbed

from custom_time import KST
import env


def success(message):
    embed = DiscordEmbed(title=':white_check_mark: 자가진단 성공!', description='자동 자가진단이 완료되었습니다.', color=3066993)
    embed.add_embed_field(name='반환값', value=message)
    embed.set_footer(text='처리 기준 (KST): ' + KST.strftime('%Y-%m-%d %H:%M:%S'))
    embed.set_timestamp()
    webhook = DiscordWebhook(
        url=env.DISCORD_WEBHOOK)

    webhook.add_embed(embed)
    response = webhook.execute()
    print(response)


def failed(message):
    webhook = DiscordWebhook(
        url=env.DISCORD_WEBHOOK)
    embed = DiscordEmbed(title=':x: 자가진단 실패', description='자동 자가진단 프로세스에서 문제가 발생했습니다. 자가진단 결과를 확인해주세요.', color=15158332)
    embed.add_embed_field(name='반환값', value=message)
    embed.set_footer(text='처리 기준 (KST): ' + KST.strftime('%Y-%m-%d %H:%M:%S'))
    embed.set_timestamp()

    webhook.add_embed(embed)
    response = webhook.execute()
    print(response)
