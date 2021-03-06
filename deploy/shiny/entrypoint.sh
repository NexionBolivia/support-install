 #!/bin/bash

set -e
echo "Registering Cron expression"
# Send backup installation process in background to avoid blocking PostgreSQL startup
bash ./shiny-scripts/register-cron.sh 

bash ./shiny-scripts/create-renviron-file.sh

echo "Launching official entrypoint..."
# `exec` here is important to pass signals to the database server process;
# without `exec`, the server will be terminated abruptly with SIGKILL (see #276)
exec bash /init