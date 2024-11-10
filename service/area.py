from PyQt5.QtCore import QVariant

def saf(input_grath, input_poi, cost):

    serviceareafromlayer = processing.run(
        "native:serviceareafromlayer", {
            'INPUT':input_grath,
            'STRATEGY':0,
            'DIRECTION_FIELD':'',
            'VALUE_FORWARD':'',
            'VALUE_BACKWARD':'','VALUE_BOTH':'',
            'DEFAULT_DIRECTION':2,
            'SPEED_FIELD':'',
            'DEFAULT_SPEED':5,'TOLERANCE':5,
            'START_POINTS':input_poi,
            # 'TRAVEL_COST2':400,
            'TRAVEL_COST2':cost,
            'INCLUDE_BOUNDS':False,
            'POINT_TOLERANCE':None,'OUTPUT_LINES':'TEMPORARY_OUTPUT'
        }
    )
    serviceareafromlayer = serviceareafromlayer.get("OUTPUT_LINES")
    serviceareafromlayer.setName(f"cost_{cost}")
    QgsProject.instance().addMapLayer(serviceareafromlayer)
    serviceareafromlayer.commitChanges()

