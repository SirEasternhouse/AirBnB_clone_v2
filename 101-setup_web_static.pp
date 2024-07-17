exec { 'create_versions_directory':
  command => 'mkdir -p /path/to/your/versions/directory',
  creates => '/path/to/your/versions/directory',
}

exec { 'pack_web_static':
  command     => 'tar -cvzf /path/to/your/versions/web_static_%{timestamp}.tgz /path/to/your/web_static',
  environment => ['timestamp=$(date +%Y%m%d%H%M%S)'],
  creates     => '/path/to/your/versions/web_static_${timestamp}.tgz',
}
