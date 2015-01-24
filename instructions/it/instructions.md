Introduzione a ${app}
-----------------------------------
Benvenuti nella nuova app Python!

Descrizione di Python

1. [Installare lo strumento della riga di comando cf](${doc-url}/#starters/BuildingWeb.html#install_cf).
2. [Scaricare il package applicazione starter](${ace-url}/rest/apps/${app-guid}/starter-download).
3. Estrarre il package e `cd`.
4. Connetti a Bluemix:

		cf api ${api-url}

5. Accedi a Bluemix:

		cf login -u ${username}
		cf target -o ${org} -s ${space}

6. Distribuisci la app:

		cf push ${app}

7. Accedi alla app: [${route}](//${route})

