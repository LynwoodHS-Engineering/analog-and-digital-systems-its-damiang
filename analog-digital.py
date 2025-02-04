# Reset encoder position

encoder_a.set_position(0, DEGREES)



def move_motor_with_encoder():


    while True:

        # Check if the kill switch is pressed

        if bumper_c.pressing():

            brain.screen.clear_screen()

            brain.screen.print("Kill Switch!")

            motor_1.stop()

           
            wait(3,SECONDS)

            brain.screen.clear_screen()

        

    
        
        encoder_angle = encoder_a.position(DEGREES)

        

        # Move motor to match encoder position

        motor_1.spin_to_position(encoder_angle, DEGREES, wait=False)




    


        wait(0.1, SECONDS)  
            



move_motor_with_encoder()
