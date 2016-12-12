#!/bin/bash

now=$(date+"%Y-%m-%d")
path=/path/to/backup_folder
mysql_user=your_mysql_user
mysql_pass=your_mysql_pass

[ ! -d "$path"] && mkdir -p $path

dbs="$(mysql -u $myql_user -p$mysql_pass -Bse 'show databases')"

for i in $dbs; do
	[ "$i" == "information_schema" ] && continue
	[ "$i" == "performance_schema" ] && continue
	[ "$i" == "mysql" ] && continue

	file="${path}/${i}.sql"

	/usr/bin/mysqldump -u $mysql_user -p$mysql_pass $i > $file
done