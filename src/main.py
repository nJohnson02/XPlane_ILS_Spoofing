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

        #Define relevant datarefs
        nav_override = "sim/operation/override/override_navneedles"
        nav1_gs_l = "sim/cockpit/radios/nav1_vdef_dot"
        nav1_gs_r = "sim/cockpit/radios/nav1_vdef_dot2"
        nav2_gs_l = "sim/cockpit/radios/nav2_vdef_dot"
        nav2_gs_r = "sim/cockpit/radios/nav2_vdef_dot2"

        #Add deviation
        while True:
            client.sendDREF(nav1_gs_l, client.getDREF(nav1_gs_r)[0] + 1)

        # Let the sim run for a bit.
        sleep(4)

        print("End of Python client example")
        input("Press any key to exit...")

if __name__ == "__main__":
    ex()