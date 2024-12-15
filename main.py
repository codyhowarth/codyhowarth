from datetime import datetime, timezone
from infrastructure import get_nasa_data

from jinja2 import Environment, FileSystemLoader

def main():

  planet_count = get_nasa_data.get_exoplanet_count()

  last_update = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z")

  latest_earth_image = get_nasa_data.get_latest_earth_image()

  # Update templates/mail.html {{ total_exoplanets }} variable with planet_count
  template_variables = {
     "last_update": last_update,
      "total_exoplanets": planet_count,
      "image_url": latest_earth_image
  }

  # Load template, pass in variables, write to README.md
  env = Environment(loader=FileSystemLoader("templates"))
  template = env.get_template("main.html")
  output_from_parsed_template = template.render(template_variables)


  with open("README.md", "w+", encoding="utf-8") as fh:
      fh.write(output_from_parsed_template)

if __name__ == "__main__":
  main()