# Broadlink Rest API

## Introduction

Broadlink API is a Rest bridge to control IR devices through Broadlink's RM/RM2/RM Pro/RM3/RM3 Mini/BlackBean/A1 products.

## Getting started

First, update your configuration and logging preferences:

1) Copy **config.sample.py** to **config.py**
2) Copy **logging.example.yml** to **logging.yml**
3) Update the new files created above with your preferences
4) Activate a virtualenv (*python3*) and install the **requirements.pip** (*pip install -r requirements.pip*)

Set your *CONTROLLERS* and *IR_PACKETS* configuration into **config.py**, there's sample configuration in the **config.sample.py** to follow.

### How to define IR_PACKETS:

You will need to define your *CONTROLLERS* first:

1) python3 scripts/discover_controllers.py
2) add discovered controllers to your config.py as below:
```
    CONTROLLERS = {
        "rmmini3_garage": (0x5f36, ("192.0.1.142", 80), "A143B14612B4")
    }
```

Then learn some IR commands, here's an example of adding a *power off* command to your configuration:

1) python3 scripts/dump_packet.py
2) Wait until it says *Learning.*
3) Push **once (!)** the *power off* button on your remote
4) Wait for max. 5s
5) Copy the binary hex. string and add it to your config.py as below:
```
    IR_PACKETS = {
        "tv_garage": {
            "power_off": b'26008c00909214361336133713121311141114111312133614351436141113111411141114111311143'
                         b'614111311141114111411131114361411133614351436143514361435140005fd969214351436143514'
                         b'11141114111311141114361336143514111411141113111411141114351411141114101411141114111'
                         b'336141114351436133614361336143514000d05'
        }
    }
```

### Start the API:

You can start it by **flask run** or using docker (c.f. **Dockerfile**).

## Send commands:

Power off the Garage's TV (based on the configuration defined above):

```
curl --location --request POST 'http://127.0.0.1:5000/control/rmmini3_garage/tv_garage' \
        --header 'Content-Type: application/json' \
        --data-raw '{"command": "power_off"}'
```
