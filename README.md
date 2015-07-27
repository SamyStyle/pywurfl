# pywurfl

<a href="http://celljam.net/api/index.html" title="pywurfl">pywurfl</a> is a <a href="http://www.python.org/" title="Python">Python</a> language package that makes dealing with the <a href="http://wurfl.sourceforge.net/" title="WURFL">WURFL</a> in Python a little easier. It contains tools that allow you to retrieve objects that represent devices defined in the WURFL or manipulate the WURFL device hierarchy by using a simple set of <a href="http://celljam.net/api/index.html" title="API documentation">API</a> functions or a pywurfl specific <a href="http://celljam.net/#query" title="Query Language">query language</a>. Also included within the package is a <a href="http://celljam.net/#processor" title="WURFL processor">WURFL processor</a> class that provides an event based API that can be used to alleviate some of the work when processing the WURFL sequentially.

###Requires
Python >= 2.6

### Required Modules
<a href="http://pypi.python.org/pypi/python-Levenshtein/" title="Levenshtein Module">Levenshtein Module</a> &gt;= 0.10.1 is required for the user agent similarity algorithms.

### Optional Modules
<a href="http://pyparsing.wikispaces.com/" title="pyparsing">pyparsing</a> &gt;= 1.5 is required if you want to use the pywurfl query language.

### Scripts
The pywurfl package contains a wurfl2python.py script that translates a WURFL compatible XML file into a python class hierarchy that the pywurfl API can use directly. The default name for the output file is wurfl.py. Type the following at the command line to produce it:

```
python wurfl2python.py wurfl.xml
```


###A quick usage example
After you have created the wurfl.py module, you can use the following code to get a device object based on a user agent and print it to stdout.

```python
from wurfl import devices
from pywurfl.algorithms import TwoStepAnalysis

user_agent = u"Nokia3350/1.0 (05.01)"
search_algorithm = TwoStepAnalysis(devices)

device = devices.select_ua(user_agent, search=search_algorithm)

#Print out the specialized capabilities for this device.
print device
```

###Patching
In order to <a href="http://wurfl.sourceforge.net/patchfile.php" title="What is a patch file">patch</a> your wurfl.xml file, use the <a href="http://wurfl.sourceforge.net/xslt/index.php" title="WURFL XSLT Tools">WURFL XSLT Tools</a>. Then run wurfl2python on the patched file.

##License
<p>pywurfl is Copyright 2004-2010, Armand Lynch (lyncha at users dot sourceforge dot net)
The code is free software; you can redistribute it and/or modify it under the terms of the <a href="http://www.opensource.org/licenses/lgpl-license.php" title="LGPL">LGPL</a> License (see the file LICENSE included with the distribution).</p>
