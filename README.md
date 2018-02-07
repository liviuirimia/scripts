# scripts

# lazy.py
alias webscan="grep -r \"POST /wp-login\" /var/log/httpd/access_log | awk '{ print \$1 }' | sort | uniq -c | awk '{ if(\$1 > 5) print \$2 }'"

webscan | xargs -I{} /path/to/script {}