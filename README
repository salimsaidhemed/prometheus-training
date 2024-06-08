# Prometheus and Grafana Monitoring Project
This project provides a sample setup to help you learn and understand Prometheus and Grafana for monitoring applications. It includes a Docker Compose file that defines three containers: Prometheus, Grafana, and a sample application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Project Structure

- **Prometheus**: An open-source monitoring and alerting toolkit.
- **Grafana**: An open-source platform for monitoring and observability, which integrates with Prometheus.
- **Sample Application**: A simple web application to generate metrics for monitoring.

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/salimsaidhemed/prometheus-training
cd prometheus-training
```

2. Launch the Containers

```bash
docker-compose up -d
```

3. Access Prometheus
Open your browser and navigate to [http://localhost:9090](http://localhost:9090).

4. Access Grafana:
Open your browser and navigate to [http://localhost:3000](http://localhost:3000)

- Login: The default username and password are both admin. You will be prompted to change the password on the first login.
- Add Prometheus as a data source:
    1. Click on the gear icon (⚙️) to open the Configuration menu.
    2. Click on "Data Sources".
    3. Click on "Add data source".
    4. Select "Prometheus" from the list.
    5. Set the URL to http://prometheus:9090 and click "Save & Test".

5. Access the Sample Application:
Open your browser and navigate to [http://localhost:9000](http://localhost:9000)

6. Import Grafana Dashboards:

    - Go to the Dashboard icon (📊) and click on "Manage".
    - Click on "Import".
    - Enter the dashboard ID (e.g., 1860 for the Prometheus 2.0 Overview) and click "Load".
    - Select "Prometheus" as the data source and click "Import".

## Stopping the Containers
To stop and remove the containers, run:

```bash
docker-compose down
```

## Project Directory

```text
.
├── README
├── config
│   └── prometheus.yml
├── config.yml
├── delete_all_data.sh
├── docker-compose.yml
├── promql tidbit
├── request_simulator.sh
└── webapp
    ├── Dockerfile
    ├── app.py
    └── requirements.txt
```

## Notes
- The sample application is configured to expose metrics that Prometheus will scrape.
- You can customize the Prometheus and Grafana configurations as needed.

## References

- [Prometheus Documentation](https://prometheus.io/docs/introduction/overview/)
- [Grafana Documentation](https://grafana.com/docs/grafana/latest/)