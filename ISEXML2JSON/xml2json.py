"""
Authors:
Emmanuel Cano - @EmmanuelCano

Co-Author:
Ryah Wehe
"""
import json
import xmltodict



with open("PolicyConfig.xml") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())

    xml_file.close()

    json_data = json.dumps(data_dict)
    
    ###Printing the result in a pretty format##
    #parsed = json.loads(json_data)
    #print(json.dumps(parsed, indent=4, sort_keys=True))
    
   
   #Note: The file will be save in the same location as this file.
   

   
    with open("ISEPolicies.json", "w") as json_file:
        
        parsed = json.loads(json_data)
        json_file.write(json.dumps(parsed, indent=4, sort_keys=True))

        json_file.close()
