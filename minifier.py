#!/usr/bin/env python3
############################################################
# HTML, CSS, JS Minifier CLI Tool
# Copyright GrayWasTaken.club 2021
# Author.: Gray
# Website: https://lambda.black/
# Program is free to use the author is not responsible
# for how you choose to use it
############################################################
__author__  = 'Gray'
__version__ = 1.0
__license__ = 'GNU GENERAL PUBLIC LICENSE'
import re, sys, os
from glob import glob
del sys.argv[0]

class c:
  _ = "\033[0m"
  p = "\033[38;5;204m"
  o = "\033[38;5;208m"
  b = "\033[38;5;295m"
  c = "\033[38;5;299m"
  g = "\033[38;5;47m"
  r = "\033[38;5;1m"
  y = "\033[38;5;226m"

def help():
  width = int(os.popen('stty size', 'r').read().split()[1])
  if width > 100: width = 100
  print(c.o+"="*width)
  print(f"HTML, CSS, JS Minifier v{__version__}".center(width))
  print(f"Author: {__author__} | Website: https://lambda.black/ | license: {__license__}".center(width))
  
  print(f"\n{c.o}Usage:")
  print(f"  {c.y}$ minifier <html/css/javascript file>\n    {c.b}Minifies a single html, css, or javascript file.\n      {c.c}minifier -r /var/www/index.html")
  print(f"\n{c.o}Flags:")
  print(f"  {c.y}-h, --help, help\n    {c.b}Prints this help screen.{c.c}\n    Usage: minifier -h")
  print(f"  {c.y}-r <path to folder>\n    {c.b}Minifies all files ending with .css, .html, and .js recursively.{c.c}\n    Usage: minifier -r some/folder")
  print(f"  {c.y}-i <string>\n    {c.b}Ignores files and folders that match the string submitted.{c.c}\n    Usage: minifier -r /var/www/ -i ignoreFolder")
  print(c.o+"="*width)


if len(sys.argv) == 0 or '-h' in sys.argv or '--help' in sys.argv or 'help' in sys.argv:
  help()
  sys.exit()

class Parse:
  @staticmethod
  def html(data):
    # Parse script tags
    data=re.sub("(<script.*?>)(.*?)</script>",lambda x: f"{x.group(1)}{Parse.javascript(x.group(2))}</script>",data, flags=re.DOTALL)
    # Remove comments
    data=re.sub(r"<!--.+?(?=-->)-->","",data,flags=re.DOTALL)
    # Remove new lines and spaces
    data=re.sub(r"\n(\s)*","",data,flags=re.DOTALL)
    return data
  @staticmethod
  def css(data):
    # Remove comments
    data=re.sub(r"\/\*.+?(?=\*\/)\*\/","",data,flags=re.DOTALL)
    # Remove new lines and spaces
    data=re.sub(r"\n(\s)*","",data,flags=re.DOTALL)
    data=re.sub(r"}\s*","}",data,flags=re.DOTALL)
    # Final
    data=data.replace(": ",":").replace(" {","{")
    return data
  @staticmethod
  def javascript(data):
    # Set temp place holder for type declarations
    data=data.replace("var ","var_VAR_").replace("const ","const_VAR_").replace("let ","let_VAR_").replace("function ","function_VAR_").replace("class ","class_VAR_").replace("if ","if_VAR_").replace("else if ","else if_VAR_").replace("else ","else_VAR_").replace("for ","for_VAR_").replace("while ","while_VAR_").replace("new ","new_VAR_")
    # Remove comments
    data=re.sub(r"//.+?(?=\n)\n","",data,flags=re.DOTALL)
    # Remove all whitespace not in quote
    data=re.sub(r"\s+(?=([^\"`']*[\"`'][^\"`']*[\"`'])*[^\"`']*$)","",data,flags=re.DOTALL)
    # remove place holders
    data=data.replace("var_VAR_","var ").replace("const_VAR_","const ").replace("let_VAR_","let ").replace("function_VAR_","function ").replace("class_VAR_","class ").replace("if_VAR_","if ").replace("else if_VAR_","else if ").replace("else_VAR_","else ").replace("for_VAR_","for ").replace("while_VAR_","while ").replace("new_VAR_","new ")
    return data

if "-r" in sys.argv:
  for i in range(len(sys.argv)):
    if sys.argv[i] == "-r":
      full_path = sys.argv[i+1]
      break

  if full_path[0] != "/":
    full_path = os.getcwd() + "/" + full_path
  
  ignore = "/////"
  for i in range(len(sys.argv)):
    if sys.argv[i] == "-i":
      ignore = sys.argv[i+1]
      break

  files = {
    "html":[y for x in os.walk(full_path) for y in glob(os.path.join(x[0], '*.html'))],
    "css":[y for x in os.walk(full_path) for y in glob(os.path.join(x[0], '*.css'))],
    "js":[y for x in os.walk(full_path) for y in glob(os.path.join(x[0], '*.js'))],
  }
  print(f"{c.y}[*]{c._} Discovered the following amounts of files in {c.p}{full_path}{c._}")
  print(f"{c.g}[+]{c._} html..: {c.p}{len(files['html'])}{c._}")
  print(f"{c.g}[+]{c._} css...: {c.p}{len(files['css'])}{c._}")
  print(f"{c.g}[+]{c._} js....: {c.p}{len(files['js'])}{c._}")
  
  for x in files['html']:
    if ignore not in x:
      with open(x, "r") as f:
        content = f.read()
      with open(x, "w") as f:
        size = len(content)
        content = Parse.html(content)
        print(f"{c.g}[+]{c._} Minifed {c.p}{x}{c._}: {c.p}{size}{c._} --> {c.p}{len(content)}{c._}")
        f.write(content)
  for x in files['css']:
    if ignore not in x:
      with open(x, "r") as f:
        content = f.read()
      with open(x, "w") as f:
        size = len(content)
        content = Parse.css(content)
        print(f"{c.g}[+]{c._} Minifed {c.p}{x}{c._}: {c.p}{size}{c._} --> {c.p}{len(content)}{c._}")
        f.write(content)
  for x in files['js']:
    if ignore not in x:
      with open(x, "r") as f:
        content = f.read()
      with open(x, "w") as f:
        size = len(content)
        content = Parse.javascript(content)
        print(f"{c.g}[+]{c._} Minifed {c.p}{x}{c._}: {c.p}{size}{c._} --> {c.p}{len(content)}{c._}")
        f.write(content)





else:
  if sys.argv[0][0] == "/":
    full_path = sys.argv[0]
  else:
    full_path = os.getcwd() + "/" + sys.argv[0]
  if full_path.endswith(".html"):
    file_type = "HTML"
  elif full_path.endswith(".css"):
    file_type = "CSS"
  elif full_path.endswith(".js"):
    file_type = "javascript"
  else:
    sys.exit(f"{c.r}[+]{c._} Invalid filename or filepath.")


  try:
    with open(full_path, "r") as f:
      content = f.read()
  except Exception as e:
    sys.exit(f"{c.r}[+]{c._} Error reading file:\n{e}")

  size = len(content)

  if file_type == "HTML":
    content = Parse.html(content)
  elif file_type == "CSS":
    content = Parse.css(content)
  elif file_type == "javascript":
    content = Parse.javascript(content)

  print(f"{c.y}[*]{c._} Successfully minifed {c.p}{file_type}{c._} document {c.p}{sys.argv[0]}{c._}: {c.p}{size}{c._} --> {c.p}{len(content)}{c._}")
  with open(full_path, "w") as f:
    f.write(content)