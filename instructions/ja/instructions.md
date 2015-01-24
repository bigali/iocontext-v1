${app}: 始めに
-----------------------------------
新しい Python アプリへようこそ

Python の説明

1. [cf コマンド・ライン・ツールをインストールします](${doc-url}/#starters/BuildingWeb.html#install_cf)。
2. [スターター・アプリケーション・パッケージをダウンロードします](${ace-url}/rest/apps/${app-guid}/starter-download)。
3. パッケージを解凍し、そのパッケージに `cd` で移動します。
4. Bluemix への接続:

		cf api ${api-url}

5. Bluemix へのログイン:

		cf login -u ${username}
		cf target -o ${org} -s ${space}

6. アプリのデプロイ:

		cf push ${app}

7. アプリへのアクセス: [${route}](//${route})

