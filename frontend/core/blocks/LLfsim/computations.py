def compute(archModel, floorplan, prog):
    """Simulate the program on the archModel with the floorplan and return the occupancy logs.

    Inputs:
        archModel: A Yaml file containing the archModel
        floorplan: A Yaml file containing the floorplan matching the archModel
        prog : A Yaml file containing the program to be simulated

    Outputs:
        occupancy : fsim sends logs of data to a postgres DB already

    Requirements:
    """
    
    occupancy = "Json file logged at the postgres DB... TODO... Reroute a copy locally...?"

    return {"occupancy": occupancy}


def test():
    """Test the compute function."""

    print("Running test")
