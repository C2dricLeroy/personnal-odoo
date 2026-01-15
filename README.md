Install the project : 

mkdir -p odoo_source

docker cp odoo:/usr/lib/python3/dist-packages/odoo ./odoo_source

npx tailwindcss \
  -i ./celer-addons/celer_website/static/src/css/main.css \
  -o ./celer-addons/celer_website/static/src/css/tailwind.out.css \
  --minify