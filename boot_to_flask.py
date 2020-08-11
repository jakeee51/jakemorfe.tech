import os, sys, re

try:
   export_dir = sys.argv[1]
except:
   export_dir = "portfolio/templates/"
templates = os.listdir(export_dir)

for page in templates:
   template = "portfolio/templates/" + page
   with open(template, "r+") as f:
      html = f.read().replace("&quot;", '"')
      static_paths = re.findall(r'(?:(?<=href=")|(?<=src=")|(?<=url\())"?assets/.+?"', html)
      pages = re.findall(r'(?<=href=").+?.html"', html)
      for path in static_paths:
         print(path)
         if path[0] == '"':
            path = path.strip('"')
            html = re.sub(fr'"{path}"', f"{{{{ url_for('static',filename='{path}') }}}}", html)
         else:
            path = path.strip('"')
            html = re.sub(fr"{path}", f"{{{{ url_for('static',filename='{path}') }}}}", html)
      for page in pages:
         page = page.strip('"')
         route = re.sub(r'\.html', '', page)
         html = re.sub(fr"{page}", f"{{{{ url_for('{route}') }}}}", html)
      f.seek(0)
      f.write(html)
      f.truncate()
      #print(html)
