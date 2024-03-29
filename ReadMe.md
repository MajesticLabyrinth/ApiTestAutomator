# API Test Automator


This project uses pycurl to automate REST API testing tasks. 
Objective is to be able to send requests to REST API, capture response and determine outcome based on configured rules.



## Framework Operation Sequence

Figure below depicts the sequence of operations that execute when running a
typical test.

![alt text](/doc/apitestfwsopseq.drawio.png)

Typically each test is divided in following parts -
1. Configuration - This is where all configuration activities should go. Typically framework specific configuration
is separated from test specific configuration. During multiple test executions framework objects may or may not require
re-configuring.
2. Request formation - This is where actual request is constructed based on configuration.
3. Request execution - This is the smallest part as executing a request requires very small amount of work on framework's part.
4. Postprocessing - This is where captured response is analysed and matched against expected conditions.
4. Result - This phase largely belongs to pytest framework library.

## Framework Object Layers
Figure below shows object layers responsible for individual operations.
In order to separate responsibility of each operation in independent operational unit
layers have been designed in such a way that they take care of smallest possible
task.

![alt text](/doc/testframeworklayers.drawio.png)



## Core Classes

### Configuration Management
1. Input configuration schema

### Request Construction Classes

### Response Verification Classes

### Test Result Generation
1. Result output schema

## Using The Framework
1. Set up configuration parameters in config.json
2. Run main.py
3. Verify results

## Reference Material

Links below demonstrate how you can use requests and pycurl libraries.
1. https://stackabuse.com/using-curl-in-python-with-pycurl/
2. https://dev.to/m4rri4nne/automating-your-api-tests-using-python-and-pytest-23cc

Link below shows performance comparison between requests and pycurl libraries.

https://stackoverflow.com/questions/15461995/python-requests-vs-pycurl-performance

As it can be observed, requests has simple interface but is bit slower than pycurl. With the view that this framework
should be usable in CI, we have picked pycurl library since it will be much faster and can help save time in post-build execution.

Sharing logger across multiple Python Modules

https://stackoverflow.com/questions/15727420/using-logging-in-multiple-modules