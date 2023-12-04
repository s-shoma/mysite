import subprocess


def stop_minecraft_server():
    # Minecraftサーバーのコンソールへのアクセスを得るためのコマンド
    # ここでは例としてscreenを使用していますが、実際の環境に合わせて調整してください
    command = ["C:\Users\ssoud\minecraft_server\1_20_2_\server.jar", "-S", "MinecraftServer", "-X", "stuff", '"stop\n"']

    # コマンドを実行してサーバーを停止
    subprocess.run(command)


# サーバーを停止
stop_minecraft_server()
