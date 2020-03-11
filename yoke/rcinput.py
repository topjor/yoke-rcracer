from yoke import events

class rcinput:

    # input mapping
    input_default = {
        'ABS_X': 128,
        'ABS_Y': 128,

        'ABS_RX': 128,
        'ABS_RY': 128,

        'ABS_GAS': 0,

        'BTN_MODE': 0
    }
    input = dict(input_default)

    active = 0

    def __init__(self):
        1+1

    def destroy(self):
        1+1

    ## done foreach input => value every update
    ## updates the input object with the given input events
    def emit(self, event, value, nothing):
        # Mode button to toggle activation
        if event == events.BTN_MODE:
            if self.input['BTN_MODE'] != value:
                if value == 1:
                    self.active = not(self.active)
                    print("toggling active state")
            self.input['BTN_MODE'] = value
        # input axis
        elif event == events.ABS_X:
            self.input['ABS_X'] = value
        elif event == events.ABS_Y:
            self.input["ABS_Y"] = value
        elif event == events.ABS_RX:
            self.input["ABS_RX"] = value
        elif event == events.ABS_RY:
            self.input["ABS_RY"] = value
        # gas pedel if you may want to override the speed (not programmed yet)
        elif event == events.ABS_GAS:
            self.input["ABS_GAS"] = value

    ## done after each full update
    def syn(self):
        # get right Axis for the 2 modes
        if self.active == 1:
            X = self.input["ABS_X"]
            Y = self.input["ABS_Y"]
            RX = self.input["ABS_RX"]
            RY = self.input["ABS_RY"]
            G = self.input["ABS_GAS"]
        else:
            X = self.input_default["ABS_X"]
            Y = self.input_default["ABS_Y"]
            RX = self.input_default["ABS_RX"]
            RY = self.input_default["ABS_RY"]
            G = self.input_default["ABS_GAS"]

        #TODO put your processing under here
