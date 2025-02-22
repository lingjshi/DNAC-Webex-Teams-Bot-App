"""
Copyright (c) 2018 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""


class DnacClientClass(object):
    condition = 'New'
    def __init__(self, score ,name, mac, ipv4, connection,status):
        self.healthscore = score
        self.hostName = name
        self.macAddress = mac
        self.ipv4 = ipv4
        self.connection = connection
        self.status = status

    def __str__(self):
        return '\n'.join(
            ('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))


class DnacNetworkDeviceClass(object):
    def __init__(self, name, ip, platformId, nwDeviceId, sysUptime
                 , nwDeviceRole, nwDeviceFamily, macAddress, softwareVersion,
                 nwDeviceType, reachabilityStatus, series):
        self.name = name
        self.ip = ip
        self.platformId = platformId
        self.nwDeviceId =  nwDeviceId
        self.upTime =  sysUptime
        self.nwDeviceRole =  nwDeviceRole
        self.deviceFamily = nwDeviceFamily
        self.macAddress = macAddress
        self.softwareVersion = softwareVersion
        self.nwDeviceType = nwDeviceType
        self.reachabilityStatus = reachabilityStatus
        self.series = series
    def __str__(self):
        return '\n'.join(
            ('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))

class DnacSiteHierarchyClass(object):
    condition = 'New'
    def __init__(self, name, id, parentId, networkhealth, clienthealth,totalDevCount,healthyDevCount):
        self.name = name
        self.id = id
        self.parentId = parentId
        self.networkHealth = networkhealth
        self.clienthealth = clienthealth
        self.totalDevCount = totalDevCount
        self.healthyDevCount = healthyDevCount


    def __str__(self):
        return '\n'.join(
            ('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))


class DnacNetworkDeviceDetailClass(object):
    def __init__(self, name,id,family,type,macAddress,serialNum):
        self.name = name
        self.id = id
        self.family = family
        self.type = type
        self.macAddress = macAddress
        self.serialNum = serialNum
    def __str__(self):
        return '\n'.join(
            ('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))
