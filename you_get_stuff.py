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

class You_Get_Stuff:
    def __init__(self, event):
        self.event = event;

    def you_check_it():
        pass;
    
    def you_pack_it():
        pass;

    def you_parse_it():
        pass;
        
def test_main():
    assert True; 