from time import sleep
import xpc as xpc

def ex():
    print("X-Plane Connect example script")
    print("Setting up simulation")
    with xpc.XPlaneConnect() as client:
        # Verify connection
        try:
            # If X-Plane does not respond to the request, a timeout error
            # will be raised.
            client.getDREF("sim/test/test_float")
        except:
            print("Error establishing connection to X-Plane.")
            print("Exiting...")
            return

        #Show a message
        client.sendTEXT("Gear up!")

        # Stow landing gear using a dataref
        print("Stowing gear")
        gear_dref = "sim/cockpit/switches/gear_handle_status"
        client.sendDREF(gear_dref, 0)

        # Let the sim run for a bit.
        sleep(4)

        # Make sure gear was stowed successfully
        gear_status = client.getDREF(gear_dref)
        if gear_status[0] == 0:
            print("Gear stowed")
        else:
            print("Error stowing gear")

        print("End of Python client example")
        input("Press any key to exit...")

if __name__ == "__main__":
    ex()