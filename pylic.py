import pkg_resources
import sys
import os
import shutil
import requirements
import urllib
import urllib.error
import urllib.request
import email.parser

# trying most common license file names (at least on github)
licensenames = ["LICENSE", "LICENSE.TXT", "LICENSE.MD", "LICENSE.txt", "LICENSE.md", "License",
                "License.txt", "License.md", "license", "license.txt", "license.md"]

if len(sys.argv) > 3:
    print("Usage: get_license.py <requirements-file> <env path>")
    sys.exit(-1)

usereqlist = False
reqlist = {}
parsedlist = {}

if len(sys.argv) == 1:
    print("Processing current environment.")
if len(sys.argv) >= 2:
    with open(sys.argv[1], mode="r") as f:
        for req in requirements.parse(f):
            reqlist[req.name] = req
        usereqlist = True
    print("Processing packages in "+sys.argv[1])
if len(sys.argv) == 3:
    script = os.path.join(sys.argv[2], "Scripts")
    script = os.path.join(script, "activate_this.py")
    print("Using environment "+sys.argv[2])
    exec(open(script).read(), {"__file__": script})
    pkg_resources.working_set = pkg_resources.WorkingSet()


if not os.path.exists("licenses"):
    os.mkdir("licenses")

packages = sorted(pkg_resources.working_set,
                  key=lambda p: str.lower(p.project_name))

with open("licenses/licenses.txt", mode="w", encoding="UTF-8") as out:
    for p in packages:
        print("processing "+p.project_name)

        if usereqlist and p.project_name not in reqlist:
            print("skipped, not in package list")
            continue

        row = p.project_name
        row += " "
        row += p.parsed_version.public

        if (p.has_metadata(p.PKG_INFO)):
            parser = email.parser.FeedParser()
            parser.feed(p.get_metadata(p.PKG_INFO))
            headers = parser.close()

            if "license" in headers:
                row += " "+headers["license"]
            else:
                row += " unknown"

            if "home-page" in headers:
                url = urllib.parse.urlparse(headers["home-page"])

                row += " "+url.geturl()

                urlpath = url.path

                if not urlpath.endswith("/"):
                    urlpath += "/"

                if url.netloc == "github.com":
                    url = url._replace(netloc="raw.githubusercontent.com")
                    if urlpath.endswith(".git/"):
                        urlpath = urlpath[: -5]
                        urlpath += "/"

                    urlpath += "master/"

                for licensename in licensenames:
                    newurl = url._replace(path=urlpath+licensename)

                    try:
                        with urllib.request.urlopen(newurl.geturl()) as response:
                            filename = "licenses/"+p.project_name+".license.txt"
                            with open(filename, "wb") as licensefile:
                                shutil.copyfileobj(response, licensefile)

                        print("License downloaded.")
                        row += " (license: "+newurl.geturl()+")"
                        break
                    except ValueError:
                        pass
                    except urllib.error.HTTPError:
                        pass
                    except urllib.error.URLError:
                        pass
        else:
            row += " unknown"

        out.write(row+"\n")
