# Automated UV-C Sanitizing Robot
2021.08.07

## Important Links
Google Drive for Project: https://drive.google.com/drive/folders/1ND2Xbyo4cFTanv-A_s6Lteof1k25Or21?usp=sharing

## Introduction
The AUV-CSR (Automated UV-C Sanitizing Robot) will be a robot designed to combat virus contamination in personal areas (e.g. homes). It will accomplish this using a compact fluorescent UV-C lamp (CFL) (or UV-C LEDs) to illuminate its surroundings with germicidal UV-C rays. This CFL will be attached to a mobile chassis that will move around in a similar fashion to how a cleaning roomba might move around; i.e. through infrared sensors (and potentially Visual Simultaneous Localization and Mapping (VSLAM)). However, because long term exposure to UV-C rays can be harmful to living organisms the AUV-CSR will be able to determine the presence of a living organism (e.g. a human or animal) and turn off its UV-C lamp accordingly. This process of live organism deduction can be done through infrared (IR) thermal cameras and machine learning. 


## Design Plan (Hardware)
The exterior design of the AUV-CSR will utilize a metal tank chassis modified with 3D printed components for its main body.\
The driving system will consist of:\
* 2 DC 12-24 V motors,\
* L298N Motor Driver,\
* Continuous track,\
* Raspberry Pi 4,\
* 12v 7Ah Sealed Lead Acid (SLA) Battery,\
* Infrared sensor(s) (or other) TBD.\
The UV-C CFL system will consist of:\
* 1-3 Osram UV-C HNS 15W G13 CFLs (Can be exchanged for 254nm or 222nm UV-C LEDs),\
* ECG(s) TBD,\
* 12v DC to 220v AC converter,\
* 12v 7Ah SLA Battery (Repeat),\
* Relay,\
* Raspberry Pi 4 (Repeat).\
The live organism detection system will consist of:\
* Thermal camera(s),\
* Raspberry Pi 4 (Repeat).\
All three systems will be controlled by the Raspberry Pi. The motor driver and sensors will be connected to the Raspberry Pi, thus the Raspberry Pi will be able to move the robot accordingly. The relay in the UV-C system will also be connected to the Raspberry Pi, allowing the Raspberry Pi to close or open the circuit and therefore turn on and off the UV-C light. The Raspberry Pi will also receive the camera inputs and determine whether it should stop shining the UV-C light and accordingly open or close the relay.

## Design Plan (Software)
The software of the robot will split into two main parts.\
The driving software and the live organism detection software.\
The former can be done by using the sensor inputs to detect obstacles (e.g. walls or furniture) while moving and avoid them by turning around and moving elsewhere. If possible, implementation of VSLAM would also be a goal.\
The latter can be done using a process of machine learning on thermal camera inputs to determine presence of living organisms.


## Goals (2021)
Hardware (if possible):\
* Create a final schematic for all components.\
Software:\
* Create a live organism detection program, with Infrared Camera and Raspberry Pi that will work with a fully assembled tank later.\
* Create a driving program that is able to input sensor data and use it to determine and drive the motors through the driver motor and Raspberry Pi.\

