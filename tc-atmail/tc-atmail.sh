#!/bin/sh
# 
# peritus-tc-tools/tc-atmail.sh
# Count some tables from @mail MySQL database 
# and output it to OpenTSDB tcollector
# 
# 2014-04-06 Stian Øvrevåge <stian@peritusconsulting.no>
#
# This script will simply count the number of rows for some of the atmail
# tables and output the metrics in tcollector compatible format.
#
# It will also output a metric of its own running time in microseconds in
# order to evaluate performance over time as counting mysql-rows on huge
# databases might result in performance degradation.
#
# Instructions:
#   Put this file into a tcollector/collectors/XX/ folder where XX is how
#   often you want the script to run. 300 should be reasonable and gives
#   statistics every 5 minutes. Make sure the script is runnable.  
# 
#   You can run the script on the @mail server itself or another host.
#   Make sure you create a user with permissions to connect if using a 
#   remote host. And update the config below.
#
#   You can run the script itself on the command-line to verify that 
#   it is working properly.
#

MYSQL_USER=
MYSQL_PASS=
MYSQL_HOST=localhost
MYSQL_DB=atmail

TAG_HOST=`hostname`

STARTTIME=$(date +%s%N)

echo atmail.adminusers `date +%s` `echo "USE $MYSQL_DB; SELECT count(*) FROM AdminUsers;" | mysql --host $MYSQL_HOST --user $MYSQL_USER -p$MYSQL_PASS --skip-column-names` host=$TAG_HOST
echo atmail.domains `date +%s` `echo "USE $MYSQL_DB; SELECT count(*) FROM Domains;" | mysql --host $MYSQL_HOST --user $MYSQL_USER -p$MYSQL_PASS --skip-column-names` host=$TAG_HOST
echo atmail.mailrelays `date +%s` `echo "USE $MYSQL_DB; SELECT count(*) FROM MailRelay;" | mysql --host $MYSQL_HOST --user $MYSQL_USER -p$MYSQL_PASS --skip-column-names` host=$TAG_HOST
echo atmail.sharedfiles `date +%s` `echo "USE $MYSQL_DB; SELECT count(*) FROM SharedFiles;" | mysql --host $MYSQL_HOST --user $MYSQL_USER -p$MYSQL_PASS --skip-column-names` host=$TAG_HOST
echo atmail.users `date +%s` `echo "USE $MYSQL_DB; SELECT count(*) FROM Users;" | mysql --host $MYSQL_HOST --user $MYSQL_USER -p$MYSQL_PASS --skip-column-names` host=$TAG_HOST
echo atmail.usersessions `date +%s` `echo "USE $MYSQL_DB; SELECT count(*) FROM UserSession;" | mysql --host $MYSQL_HOST --user $MYSQL_USER -p$MYSQL_PASS --skip-column-names` host=$TAG_HOST
echo atmail.log.virus `date +%s` `echo "USE $MYSQL_DB; SELECT count(*) FROM Log_Virus;" | mysql --host $MYSQL_HOST --user $MYSQL_USER -p$MYSQL_PASS --skip-column-names` host=$TAG_HOST
echo atmail.log.spam `date +%s` `echo "USE $MYSQL_DB; SELECT count(*) FROM Log_Spam;" | mysql --host $MYSQL_HOST --user $MYSQL_USER -p$MYSQL_PASS --skip-column-names` host=$TAG_HOST
echo atmail.log.sentmail `date +%s` `echo "USE $MYSQL_DB; SELECT count(*) FROM Log_SendMail;" | mysql --host $MYSQL_HOST --user $MYSQL_USER -p$MYSQL_PASS --skip-column-names` host=$TAG_HOST
echo atmail.log.recvmail `date +%s` `echo "USE $MYSQL_DB; SELECT count(*) FROM Log_RecvMail;" | mysql --host $MYSQL_HOST --user $MYSQL_USER -p$MYSQL_PASS --skip-column-names` host=$TAG_HOST
echo atmail.log.logins `date +%s` `echo "USE $MYSQL_DB; SELECT count(*) FROM Log_Login;" | mysql --host $MYSQL_HOST --user $MYSQL_USER -p$MYSQL_PASS --skip-column-names` host=$TAG_HOST
echo atmail.log.errors `date +%s` `echo "USE $MYSQL_DB; SELECT count(*) FROM Log_Error;" | mysql --host $MYSQL_HOST --user $MYSQL_USER -p$MYSQL_PASS --skip-column-names` host=$TAG_HOST

ENDTIME=$(date +%s%N)

echo tcollector.collectors.atmail.elapsedtime `date +%s` "$((($ENDTIME - $STARTTIME) / 1000))" host=$TAG_HOST
