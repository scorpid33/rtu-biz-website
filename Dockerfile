FROM wordpress

RUN cp /etc/skel/.bash* /root

RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get install -y bash-completion nano wget curl less

RUN wget -q https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar -O /usr/local/bin/wp
RUN chmod +x /usr/local/bin/wp

RUN mkdir -p /var/www/html/wp-content
COPY plugins /var/www/html/wp-content/plugins
