# Vota Informado Web Scraper
WebScraper service for the [Vota Informado](https://votainformado.com.ar) project.

<div style="text-align: center;">
    <img src="https://www.votainformado.com.ar/static/media/logo.b3817a447af529aca95c3d065b7c48e1.svg" alt="Vota Informado" width="200"/>
</div>

### Description

The web scraper is just a service to extract information from a specific site (https://votaciones.hcdn.gob.ar) using Selenium, since it's the only way to get the information we need.

### Requirements
To run the project you need to have installed:
 - Python (v3.8 or higher)
 
### Running the project
To run the project you need to execute the following command:

```bash
python manage.py runserver --port {DESIRED_PORT}
```
Where `{DESIRED_PORT}` is the port where you want to run the server
