# workaholic-api
API for working time storage.

This application creates a service that accepts HTTP POST requests.

I use this to track my working time - for instance with MacOs [sleepwatcher](http://www.bernhard-baehr.de).

It launches a script every time I lock/unlock my PC.

This script contains curl command that posts data to this app like

```curl http://somehost/tracker/data --data kind={0 or 1}```

This app makes a record to the database.

Zabbix scrapes that data and draws a graph of my time I've spent working.
