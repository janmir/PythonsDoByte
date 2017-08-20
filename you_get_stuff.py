#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Features
#1. Handle all incomming data from request and issue errors if needed
#2. Accept a list dictionary of parameters for checking request data, on initialization
#   - Dictionary is in {"event_name", "required", "type"} pair
#   - Check if all required events are present, issue an error if not.
#3. Accept a event dictionary when checking, should be called in the first parts of the program
#4. Do all format i.e number types should be a parsable number
#5. Change dictionary to object attibutes
#   - see https://goo.gl/WtXWe3

import pytest

class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

class You_Get_Stuff:
    stuff = {};
    valid = False;

    def __init__(self, event):
        self.event = event;

    def you_check_it(self, request):
        result = True;
        #iterate thru all values of the json dictionary
        for event in self.event:
            #convet the json to something like this -> name.key
            struct = Struct(**event);
            #check required
            if(struct.required.lower() in ("yes", "true", "1")):
                if(struct.name not in request):
                    print(struct.name + " not it request. Throw an error.");
                    result &= False;
            
            #check data type
            if(struct.type not in ("int", "float", "string", "bool")):
                print(struct.name + "datatype in request is invalid. Throw an error.");
                result &= False;
                
        self.valid = result;
        return result;
    
    def you_pack_it(self):
        return Struct(**self.stuff);

    def you_parse_it(self):
        #if precheck yeilds valid
        if(self.valid):
            print("request is valid... parsing now.");

            #check type of item then convert it
            for event in self.event:
                struct = Struct(**event);

                value = None;

                #Parse the value
                try:
                    if(struct.type == "int"):
                        value = int(struct.value);
                    elif(struct.type == "float"):
                        value = float(struct.value);
                    elif(struct.type == "bool"):
                        value = bool(struct.value);
                    elif(struct.type == "string"):
                        value = struct.value;
                except Exception as e:
                    print("Error: " + e.message);
                
                #Assign value
                self.stuff[struct.name] = value;

            print(self.stuff.keys());
        else:
            print("request not yet checked or invalid.")

        
def test_main():
    testEvent = [
                    {"name": "event1", "value":"1", "required": "true", "type": "string"},
                    {"name": "event2", "value":"2", "required": "true", "type": "bool"},
                    {"name": "event3", "value":"3", "required": "true", "type": "int"},
                    {"name": "event4", "value":"4", "required": "true", "type": "float"}
    ];
    testEventRequest ={"event1": "value herer", "event2": "value herer", "event3": "value herer", "event4": "value herer"}

    testClass = You_Get_Stuff(testEvent);
    testClass.you_check_it(testEventRequest);
    testClass.you_parse_it();
    assert testClass.you_pack_it().event1 == "1";
    assert testClass.you_pack_it().event2 == True;
    assert testClass.you_pack_it().event3 == 3;
    assert testClass.you_pack_it().event4 == 4.0;

#test_main();