#### This is a project to measure and graph various gasses in our flat.

To install the prerequisites one needs sth like the following:
* apt install python3-pip
* pip3 install adafruit-circuitpython-mcp3xxx

##### Many thanks to Adafruit for all the wonderful docs, boards, and examples.
* Docs can be found here:
  * https://learn.adafruit.com/mcp3008-spi-adc?view=all
  * https://cdn-shop.adafruit.com/datasheets/MCP3008.pdf

Example output looks sth like:
![This for all Gasses](https://darkdata.org/ghz/images/docs/all_gasses.png)
![And like this for individual gasses](https://darkdata.org/ghz/images/docs/mq-137.png)

to do:
- [x] lic
- [x] readme
- [x] prototype hardware
- [ ] build hardware
- [x] hook up plotting
- [x] webpage
- [ ] calibrate
