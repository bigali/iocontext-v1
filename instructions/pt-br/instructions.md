Introdução ao ${app}
-----------------------------------
Bem-vindo ao novo app Python!

Descrição do Python

1. [Instale a ferramenta de linha de comandos cf](${doc-url}/#starters/BuildingWeb.html#install_cf).
2. [Faça o download do pacote de aplicativo iniciador](${ace-url}/rest/apps/${app-guid}/starter-download).
3. Extraia o pacote e `cd` para ele.
4. Conecte-se ao Bluemix:

		cf api ${api-url}

5. Efetue login no Bluemix:

		cf login -u ${username}
		cf target -o ${org} -s ${space}

6. Implemente seu app:

		cf push ${app}

7. Acesse seu app: [${route}](//${route})

