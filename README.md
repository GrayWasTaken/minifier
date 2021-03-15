# HTML, CSS, JS Minifier
**Author:** Gray

**License:** [GNU GENERAL PUBLIC LICENSE](#License "GNU GENERAL PUBLIC LICENSE")

**Description:** Simple minifier tool for HTML, CSS, and javascript. Supports recursion, ignore lists, pattern matching, and I have plans to add more.

## Installation
```sh
# Download the repository with
$ git clone https://github.com/GrayWasTaken/minifier.git
```

## Screenshots
![1](https://lambda.black/assets/portfolio/minifier/1.png "Help Screen")
![2](https://lambda.black/assets/portfolio/minifier/2.png "File processing")
![3](https://lambda.black/assets/portfolio/minifier/3.png "File processing with ignore")

## Features
- HTML, CSS, and JS support
- Recursion support
- File matching patterns
- Ignore patterns.

## Usage
***The help screen has all the information you'd need, but here are some hopefully useful examples:***

```py
# Prints help screen
$ ./minifier.py -h

# Minifies contents of file "./website/index.html"
$ ./minifier.py website/index.html

# Minifies contents of folder "./website/"
$ ./minifier.py -r website/

# Minifies contents of folder "./website/" and ignores all files that contain ".min"
$ ./minifier.py -r website/ -i .min
```

## Todo List
- Improve js minifier.
- Add an API to integrate with other applications.
- Add to AUR.

## License
GNU GENERAL PUBLIC LICENSE

Copyright (c) 2021 Gray

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.