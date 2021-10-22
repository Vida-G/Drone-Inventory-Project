import os

basedir = os.path.abspath(os.path.dirname(__file__))

# gives us access to this projects location in any OS we find ourselves in
# allows us access to other folders to be added into project from external sources

# Gives Flask access to relative filepath regardless of OS.
# Allows outside file/folders to imported as well
# can consider this a 'roadmap' we are giving flask for our operating system 

class Config:
    ''' Sets the configuration variables for our Flask app
        Eventually we will need hidden variable item, but for now we will leave them exposed. 
    '''
    SECRET_KEY = "You will never guess..." 
    SQLALCHEMY_DATABASE_URI= os.environ.get('DEPLOY_DATABASE_URI')

    SQLALCHEMY_TRACK_MODIFICATIONS = False # Decreases unnecessary output in terminal as we use the db
