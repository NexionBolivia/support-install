version: "3.0"

services:
  dashboards:
    image: proagenda2030/dashboards:pa.0.0.1
    restart: always
    user: 'root'
    # Uncomment the lines below to disable application logs STDOUT output
    # environment:
    #   - APPLICATION_LOGS_TO_STDOUT=false
    ports:
      - '3838:3838'
    volumes:
      - 'shiny_logs:/var/log/shiny-server'
      # Comment the line below out for initial testing. With it commented out,
      # going to localhost:80 in one's web browser will show a "Welcome to
      # Shiny Server!" diagnostics page.
      - './dashboards:/srv/shiny-server'

volumes:
  shiny_logs: