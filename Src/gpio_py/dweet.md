### Dweet.io and Freeboard

This repository contains sample code to send data to cloud on freeboard.io and visualize the data in a dashboard on freeboard.io.

Dweet.io is a simple messaging service. Just like you can send a tweet on twitter, you can send a *dweet* from your device to the dweet.io platform.

##### Dweet.io

The messaging with dweet.io happens using publish / subscribe mechanism. Messages are published for a particular topic and receiving devices can listen on that particular topic. This topic is called as a '*thing*' in dweet.io's terminology.

There is no registration or login required to send data or consume data with dweet.io. Also there is no setup or download required.

Name of the thing to publish to can be decided at run time when calling the http post. This name can either be your own name or a random name assigned by dweet.io. Publishing and data is a simple http post operation while reading data is a http get operation.

Dweet.io is free to use with unlimited things. However, there are some important points to note.

1. The name of things chosen by you should be unique. It means that there should not be any existing thing on dweet.io with the same name. One way to ensure this uniqueness is choose as random a name as possible. The other way is to let dweet.io choose the name for you.

2. Data is stored on dweet.io only up to last 5 dweets for up to 24 hours only.

2. The data you post on dweet.io is by default public. This means that anyone with the thing name can see your data in real time. Moreover all the public things are listed on dweet.io website itself for anyone to see.

The only way to reserve a specific thing name and hide your data from public is to lock your thing and not surprising but you have to pay for that. With paid things, data is stored on dweet.io for up to 30 days.

##### Visualization options





Data sent to dweet.io can be visualized on their website https://dweet.io.

Freeboard.io is a companion tool for generating dashboards for data visualization using the data from dweet.io that your device sends.
