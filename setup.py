from apiwrapper.utils.setup import Setup

"""
This setup file will configure everything for you to be able to
communicate with the Bunq API

If you already have an installation, check out the "Reuse Installation" 
section in the Readme of the GitHub Repository. 

Otherwise, lets begin:

First, set you api-key

You can either get it from the Bunq App or (and
it is recommended to do this if you use the API for the first time), contact
the Support and ask for a Sandbox api-key. The sandbox is a safer
environment to play around with.
"""
api_key = "YOUR API KEY HERE"
setup = Setup(api_key)


"""
Second, decide whether you want to store the setup parameters or not
  
These parameters (e.g. api-key, private/public key pair, session token, 
etc) are needed in order to connect to the API. You can save them to a local 
'config' file or, if you prefer to save them somewhere else, you can also 
simply write them down and copy&paste them into any script you might write 
later on. 

Set the following to True if you want to save the parameters to a config
file, otherwise set to False
"""
save_to_config = True


"""
Third, decide on whether to create a new private/public key pair or to
reuse an old one.

If you want to create a new private/public key pair uncomment the following:
"""
# setup.setup_w_new_key_pair(save_to_config)

"""Otherwise, to use an already existing key pair, uncomment the following:
"""
# private_key = "YOUR PRIVATE KEY HERE"
# setup.setup_w_existing_private_key(private_key, save_to_config)

"""
And that is it! The Setup-Class "should" now take care of everything for 
you! I say "should", because everything that can go wrong, will go wrong, 
and my code is not perfect. So please, if you encounter any problems, 
questions, or suggestions for improvements, create an issue on 
https://github.com/PJUllrich/Complete-Bunq-API-Python-Wrapper

Thank you!
"""
