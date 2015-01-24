開始使用 ${app}
-----------------------------------
歡迎使用您的新 Python 應用程式！

Python 說明

1. [安裝 cf 指令行工具](${doc-url}/#starters/BuildingWeb.html#install_cf)。
2. [下載入門範本應用程式套件](${ace-url}/rest/apps/${app-guid}/starter-download)。
3. 解開套件並 `cd` 到該處。
4. 連接至 Bluemix：

		cf api ${api-url}

5. 登入 Bluemix：

		cf login -u ${username}
		cf target -o ${org} -s ${space}

6. 部署您的應用程式：

		cf push ${app}

7. 存取您的應用程式：[${route}](//${route})

