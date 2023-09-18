# Script to install nginx using puppet

package {'nginx':
  ensure => 'present',
}

exec {'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,

}

exec {'Hello':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec {'run':
  command  => 'sudo sed -i '37i\rewrite ^/redirect_me http://driiis.tech permanent;' /etc/nginx/sites-available/default,
  provider => shell,
}


exec {'Ceci n\'est pas une page':
  command  => 'echo "Ceci n\'est pas une page" | sudo tee /var/www/html/error_404.html',
  provider => shell,
}

exec {'run':
  command  => 'sudo sed -i '38i\error_page 404 /error_404.html;' /etc/nginx/sites-available/default',
  provider => shell,
}

exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}
